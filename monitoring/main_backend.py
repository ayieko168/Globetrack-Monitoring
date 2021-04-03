from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtMultimedia, QtCore

import datetime
import vlc
import sys
import ftplib
import json


from utils import main_ui

## Config file
INITIAL_PAGE = 1
SLIDER_RANGE = 30
PLAY_SPEED = 1
HOST_IP = "192.168.0.27"
HOST_PORT = 2151

## IN File
FIRST_TIME_BOOT = True


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

        ## Qt Processes
        self.recordings_getter_process = QtCore.QProcess()

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
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateUI)

    def ui_connections(self):

        ## Player
        self.ui.play_button.clicked.connect(self.PlayPause)

        ## Side panel
        self.ui.channels_combo.currentIndexChanged.connect(self.populate_side_panel_recordings_slot)

    ## Video Player Methods
    def PlayPause(self):
        """Toggle play/pause status
        """

        self.media = self.instance.media_new("ftp://192.168.0.27:2151/KTN/Sat-03-04-2021_08-38PM_702684.avi")
        self.mediaplayer.set_media(self.media)
        self.media.parse()
        self.setWindowTitle(self.media.get_meta(0))
        self.mediaplayer.set_rate(PLAY_SPEED)

        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.ui.videoframe.winId())
        elif sys.platform == "win32": # for Windows
            self.mediaplayer.set_hwnd(self.ui.videoframe.winId())
        elif sys.platform == "darwin": # for MacOS
            self.mediaplayer.set_nsobject(int(self.ui.videoframe.winId()))

        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.ui.play_button.setText("Play")
            self.isPaused = True
        else:
            if self.mediaplayer.play() == -1:
                # self.OpenFile()
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
        self.ui.timer_slider.setValue(self.mediaplayer.get_position() * 30)

        # Set the timer label
        millis = self.mediaplayer.get_time()
        self.ui.timer_label.setText(f"{int((millis/(1000*60*60))%24):02}:{int((millis/(1000*60))%60):02}:{int((millis/1000)%60):02}")
        # print(f"get_length: {self.mediaplayer.get_position() * 30}, get_time: {time_stmp}")
        if not self.mediaplayer.is_playing():
            # no need to call this function if nothing is played
            self.timer.stop()
            if not self.isPaused:
                # after the video finished, the play button stills shows
                # "Pause", not the desired behavior of a media player
                # this will fix it
                self.Stop()

    ## Side panel methods
    def get_channels_path(self):

        ftp = ftplib.FTP()
        ftp.connect(HOST_IP, port=HOST_PORT)
        ftp.login()

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

        # ftp.cwd('/KTN')

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

        ## Populate the
























if __name__ == "__main__":

    w = QApplication([])
    app = MainApplication()
    app.show()
    w.exec_()
















































































































































































































































































































