from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtMultimedia, QtCore

import datetime
import vlc
import sys
import ftplib
import json
import time
import os
import subprocess
import shutil
import urllib.request as request
from contextlib import closing
import string
import random


from utils import main_ui

## Config file
HOST_IP = "192.168.0.27"
HOST_PORT = 2151


## IN File
FIRST_TIME_BOOT = True
INITIAL_PAGE = 0
SLIDER_RANGE = 30
PLAY_SPEED = 1
DESCENDING = True


class MainApplication(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        ## Variables
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.isPaused = False
        self.position = int
        self.player_volume = 50
        self.records_dictionary = {}
        self.root_recordings_dir = f"C:/Users/royalstate/Videos/Tv_Recordings/"
        self.all_data = {}
        self.clip_stamps = [0, 0]
        self.threadpool = QThreadPool()
        self.media = None

        ## Qt Processes
        self.downloader_process = QtCore.QProcess()
        self.downloader_process.readyRead.connect(self.downloader_process_stdout_func)
        self.downloader_process.finished.connect(self.downloader_process_finished_func)

        ## Startup Functions
        self.set_up_ui()
        self.ui_connections()
        self.get_channels_path()
        self.populate_side_panel_combo()

    def set_up_ui(self):

        ## Set the initial start page
        self.ui.stackedWidget.setCurrentIndex(INITIAL_PAGE)

        ## Clear all testing data
        self.ui.channels_combo.clear()
        self.ui.channel_recordings_listwidget.clear()
        self.ui.timer_slider.setValue(0)
        self.ui.timer_label.setText("00:00:01")
        self.ui.seek_to_entry.clear()

        ## Set place holder text
        self.ui.channels_combo.setPlaceholderText("Select Channel")

        ## Configure the player frame
        self.palette = self.ui.videoframe.palette()
        self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.ui.videoframe.setPalette(self.palette)
        self.ui.videoframe.setAutoFillBackground(True)
        self.ui.timer_slider.setRange(0.0, SLIDER_RANGE)

        ## Configure Update Timer
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateUI)

        ## Set timer shot for moving to next page
        QTimer.singleShot(3000, lambda: self.ui.stackedWidget.setCurrentIndex(1))

    def ui_connections(self):

        ## Player
        self.ui.play_button.clicked.connect(self.PlayPause)
        self.ui.increase_playback_speed_button.clicked.connect(self.increase_playback_speed)
        self.ui.normalize_playback_speed_button.clicked.connect(self.normalize_playback_speed)
        self.ui.decrease_playback_speed_button.clicked.connect(self.decrease_playback_speed)
        self.ui.mark_in_button.clicked.connect(self.mark_in_slot)
        self.ui.mark_out_button.clicked.connect(self.mark_out_slot)
        self.ui.export_button.clicked.connect(self.export_splot)

        ## Side panel
        self.ui.channels_combo.currentIndexChanged.connect(self.populate_side_panel_recordings_slot)
        self.ui.channel_recordings_listwidget.doubleClicked.connect(self.recording_double_click_slot)

    ## Video Player Methods
    def PlayPause(self):
        """Toggle play/pause status
        """

        self.mediaplayer.set_rate(PLAY_SPEED)

        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.ui.play_button.setText("Play")
            self.isPaused = True
        else:
            if self.mediaplayer.play() == -1:
                # self.OpenFile()
                self.ui.statusbar.showMessage("Select a channel then a clip to play from the side panel.", 2000)
                return
            self.mediaplayer.play()
            self.ui.play_button.setText("Pause")
            self.timer.start()
            self.isPaused = False

    def Stop(self):
        """Stop player
        """
        self.mediaplayer.stop()
        self.ui.play_button.setText("Play")

    def updateUI(self):
        """updates the user interface"""
        # setting the slider to the desired position
        self.ui.timer_slider.setValue( (self.mediaplayer.get_position() * 30.0) )

        # Set the timer label
        millis = self.mediaplayer.get_time()
        self.ui.timer_label.setText(f"{int((millis/(1000*60*60))%24):02}:{int((millis/(1000*60))%60):02}:{int((millis/1000)%60):02}")

        if not self.mediaplayer.is_playing():
            # no need to call this function if nothing is played
            self.timer.stop()
            if not self.isPaused:
                # after the video finished, the play button stills shows
                # "Pause", not the desired behavior of a media player
                # this will fix it
                self.Stop()

    def increase_playback_speed(self):

        current_rate = self.mediaplayer.get_rate()
        print(current_rate)

        self.mediaplayer.pause()
        self.mediaplayer.set_rate( (current_rate + 1.0) )
        time.sleep(0.25)
        self.mediaplayer.play()

        current_rate = self.mediaplayer.get_rate()
        self.ui.play_back_speed_label.setText(f"X{current_rate}")

    def normalize_playback_speed(self):

        current_rate = self.mediaplayer.get_rate()
        print(current_rate)

        self.mediaplayer.pause()
        self.mediaplayer.set_rate(PLAY_SPEED)
        self.mediaplayer.play()

        current_rate = self.mediaplayer.get_rate()
        self.ui.play_back_speed_label.setText(f"X{current_rate}")

    def decrease_playback_speed(self):

        current_rate = self.mediaplayer.get_rate()
        print(current_rate)

        if (current_rate - 1) == 0:
            self.mediaplayer.pause()
            self.mediaplayer.set_rate(PLAY_SPEED)
            self.mediaplayer.play()
        else:
            self.mediaplayer.pause()
            self.mediaplayer.set_rate( (current_rate - 1.0) )
            self.mediaplayer.play()

        current_rate = self.mediaplayer.get_rate()
        self.ui.play_back_speed_label.setText(f"X{current_rate}")


    ## Side panel methods
    def get_channels_path(self):

        try:
            ftp = ftplib.FTP()
            ftp.connect(HOST_IP, port=HOST_PORT)
            ftp.login()
        except Exception as e:
            print(f"FTP list Error :: {e}")
            self.setWindowTitle(f"FTP list Error :: {e}")
            return

        self.all_data = {}

        ## Get the recorded channels
        files = []
        try:
            files = ftp.nlst()
        except ftplib.error_perm as resp:
            if str(resp) == "550 No files found":
                print("No files in this directory")
            else:
                raise


        ## Loop thru all the channels and get the individual recorded clips
        for path in files:

            ftp.cwd(f'/{path}')
            # print(path)

            files = []
            try:
                files = ftp.nlst()
            except ftplib.error_perm as resp:
                if str(resp) == "550 No files found":
                    print("No files in this directory")
                else:
                    raise

            # for f in files:
                # print(f"\t- {f}")

            ## Populate the dictionary
            self.all_data[path] = files

        print(json.dumps(self.all_data, indent=2))

        if FIRST_TIME_BOOT:
            self.finished_setup()
        return self.all_data

    def finished_setup(self):

        ## Go to the main content page
        pass

    def populate_side_panel_combo(self):

        ## Get the keys of the all data dict
        recorded_channels = self.all_data.keys()

        ## Populate channels
        self.ui.channels_combo.addItems(recorded_channels)

    def populate_side_panel_recordings_slot(self):

        ## Get the current selected channel
        selected_channel = self.ui.channels_combo.currentText()

        ## Get the recordings
        recordings = sorted(self.all_data[selected_channel], reverse=DESCENDING)

        ## Clear and Populate the list widget with this data
        self.ui.channel_recordings_listwidget.clear()
        self.ui.channel_recordings_listwidget.addItems(recordings)

    def recording_double_click_slot(self):

        # self.download_videos_cmd()

        ## Get the selected recording
        selected_file = self.ui.channel_recordings_listwidget.currentItem().text()

        ## Get channel name
        channel_name = self.ui.channels_combo.currentText()

        ## Create the streaming url -- ftp://192.168.0.27:2151/KTN/Sat-03-04-2021_08-38PM_702684.avi
        stream_url = f"ftp://{HOST_IP}:{HOST_PORT}/{channel_name}/{selected_file}"
        print(stream_url)

        ## Set created URL as media source for player
        # Pause the player if was playing
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.ui.play_button.setText("Play")
            self.isPaused = True

        self.media = self.instance.media_new(stream_url, '--prefetch-seek-threshold=5000')
        self.mediaplayer.set_media(self.media)
        self.media.parse()
        self.setWindowTitle(f"Ready to play {self.media.get_meta(0)}")
        self.mediaplayer.set_rate(PLAY_SPEED)

        if sys.platform.startswith('linux'):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.ui.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.ui.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(int(self.ui.videoframe.winId()))

        # Initialize the player
        self.PlayPause()

    def mark_in_slot(self):

        ## Verify if the player has something playing
        if self.mediaplayer.get_time() == -1:
            self.ui.statusbar.showMessage("Select a valid clip to play before marking in or out", 2000)
            return

        ## Get the current time position
        seconds_time = (self.mediaplayer.get_time() / 1000.0)
        print(seconds_time)

        ## Set the times list
        self.clip_stamps[0] = seconds_time
        print(self.clip_stamps)

    def mark_out_slot(self):

        ## Verify if the player has something playing
        if self.mediaplayer.get_time() == -1:
            self.ui.statusbar.showMessage("Select a valid clip to play before marking in or out", 2000)
            return

        ## Get the current time position
        seconds_time = (self.mediaplayer.get_time() / 1000.0)
        print(seconds_time)

        ## Get -to time duration
        to_duration = seconds_time - self.clip_stamps[0]

        ## Set the times list
        self.clip_stamps[1] = to_duration
        print(self.clip_stamps)

        ## Show message
        self.ui.statusbar.showMessage("Ready to export", 2000)

    def export_splot(self):

        if self.media is None:
            self.ui.statusbar.showMessage(f"No clipped file to cut", 2000)
            return

        clip = f"{self.media.get_mrl().split('/')[-2]}-{self.media.get_mrl().split('/')[-1]}-{datetime.datetime.now().strftime('%A-%d-%m_%H-%M-%f')}"
        clip_dest = f"C:/Users/{os.getlogin()}/Desktop"


        worker = SplitWorker(
                                (self.clip_stamps, self.media.get_mrl(), clip, clip_dest, self.ui.statusbar)
                            )
        ## Add the worker to the threadpool
        self.threadpool.start(worker)

    ## File downloader
    def download_video_cmd(self, stream_url):

        print("Download files")

        #### create command
        # command = f"ffmpeg -h"
        command = f"youtube-dl {stream_url}"


        print(command)
        #### Run the command
        self.downloader_process.start(command)
        self.ui.statusbar.showMessage(f"Getting desired file from the server", 2000)

    def downloader_process_stdout_func(self):
        output = str(self.downloader_process.readAll(), encoding='utf-8')
        print(output)

        if output.strip() != '':
            _time = datetime.datetime.now().strftime("%H:%M:%S")
            log_text = f"[{_time}] ==> {output.strip()}\n"
            print(log_text)

    def downloader_process_finished_func(self):

        self.ui.statusbar.showMessage("All Files are downloaded!", 2000)
        print("All Files are downloaded!")


class SplitWorker(QRunnable):

    def __init__(self, argts, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """

        super(SplitWorker, self, *args, **kwargs).__init__()
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.clip_stamps = argts[0]
        self.videofile_path = argts[1]
        self.clip = argts[2]
        self.final_dest = argts[3]
        self.status_bar = argts[4]

    @pyqtSlot()
    def run(self):

        ## Start the downloader
        print(f"Worker started..\n")

        self.status_bar.showMessage(f"Creating {self.clip}", 2000)

        ## Create the command
        # command = f"ffmpeg -i \"{videofile_path}\" -ss {clip_stamps[0]} -to {clip_stamps[1]} -c copy -map 0 {clip}.mp4"
        # command = f"ffmpeg {spliter_ffmpeg_ops_string} -ss {clip_stamps[0]} -to {clip_stamps[1]} -i \"{videofile_path}\" -c copy -map 0 {clip}.mp4"
        # command = f"ffmpeg {self.spliter_ffmpeg_ops_string} -ss {self.clip_stamps[0]} -to {self.clip_stamps[1]} -i \"{self.videofile_path}\" {self.clip}.mp4"
        self.command = f"ffmpeg.exe -y -ss {self.clip_stamps[0]} -to {self.clip_stamps[1]} -i \"{self.videofile_path}\" {self.clip}.mp4"

        print(f"command = {self.command}")

        previous = os.getcwd()
        os.chdir(self.final_dest)
        # self.process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.process = subprocess.run(self.command, shell=True)
        os.chdir(previous)

        ## Start the info parser
        self.status_bar.showMessage(f"Finished {self.clip}", 2000)
        print(f"Finished {self.clip}")


class WorkerSignals(QObject):
    """
    update_from: tuple of (url_from)
    """
    started = pyqtSignal()
    update_from = pyqtSignal(object)
    data_ready = pyqtSignal(object, object)
    error = pyqtSignal()
    finished = pyqtSignal()















if __name__ == "__main__":

    w = QApplication([])
    app = MainApplication()
    app.show()
    w.exec_()
















































































































































































































































































































