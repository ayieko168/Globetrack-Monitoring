
import subprocess
import datetime
import concurrent.futures
import os


def capture_video(video, audio, channel_name):

    while True:
        cmd = f"""ffmpeg -y -f dshow -i video="{video}":audio="{audio}" {channel_name.upper()}_{datetime.datetime.now().strftime("%a-%d-%m-%Y_%I-%M%p_%f")}.avi"""
        # cmd = f"""ffmpeg -y -f avfoundation -i video="{video}":audio="{audio}" {channel_name.upper()}_{datetime.datetime.now().strftime("%a-%d-%m-%Y_%I-%M%p_%f")}.avi"""
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:
            if line.startswith('frame'):
                _hr, _min, _sec = line.split('time=')[-1].split()[0].split(':')  # frame= 1570 fps= 30 q=29.0 size=    5376kB time=00:00:52.26 bitrate= 842.7kbits/s dup=304 drop=5 speed=1.01x
                if _min == '01':
                    print("terminating...")
                    process.terminate()
                    capture_video(video, audio, channel_name)

                print(_min)


capture_video("USB2.0 PC CAMERA", "Microphone (2- USB2.0 MIC)", "ktn")

