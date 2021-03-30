
import subprocess
import datetime
import threading


def capture_video(video, audio, channel_name):


    cmd = f"""ffmpeg -y -f dshow -i video="{video}":audio="{audio}" {channel_name.upper()}_{datetime.datetime.now().strftime("%a-%d-%m-%Y_%I-%M%p_%f")}.avi"""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in process.stdout:
        print(line)  # frame= 1570 fps= 30 q=29.0 size=    5376kB time=00:00:52.26 bitrate= 842.7kbits/s dup=304 drop=5 speed=1.01x


th1 = threading.Thread(target=capture_video, args=("USB2.0 PC CAMERA", "Microphone (2- USB2.0 MIC)", "ktn"), name=)
th1.start()
