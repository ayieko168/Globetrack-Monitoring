
import subprocess
import datetime
import concurrent.futures
import os
import cv2
import pprint, json
from PyQt5.QtCore import QDir, Qt, QUrl


def capture_video(args_tup):

    video, audio, channel_name = args_tup

    print(f"[{channel_name}] Start recording process")
    ## Check if recording dirs are available
    recording_path = f"C:/Users/royalstate/Videos/Tv_Recordings/{channel_name.upper()}"
    if not os.path.exists(recording_path):
        print(f"[{channel_name}]Recording directory not found for {channel_name}, creating one...")
        os.makedirs(recording_path)

    while True:

        cmd = f"""ffmpeg -y -f dshow -i video="{video}":audio="{audio}" {recording_path}/{datetime.datetime.now().strftime("%a-%d-%m-%Y_%I-%M%p_%f")}.avi"""
        # cmd = f"""ffmpeg -y -f avfoundation -i video="{video}":audio="{audio}" {channel_name.upper()}_{datetime.datetime.now().strftime("%a-%d-%m-%Y_%I-%M%p_%f")}.avi"""
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:
            if line.startswith('frame'):
                _hr, _min, _sec = line.split('time=')[-1].split()[0].split(':')  # frame= 1570 fps= 30 q=29.0 size=    5376kB time=00:00:52.26 bitrate= 842.7kbits/s dup=304 drop=5 speed=1.01x
                if _min == '01':
                    print(f"[{channel_name}]terminating...")
                    process.terminate()
                    capture_video((video, audio, channel_name))

                print(f"[{channel_name}] {_min}")


def get_video_devices():

    lines = []
    cmd = "ffmpeg -list_devices true -f dshow -i dummy"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    out = False
    for line in process.stdout:
        if "DirectShow video devices".upper() in line.upper():
            out = True
            continue
        if "DirectShow audio devices".upper() in line.upper():
            out = False

        if out:
            line = line.splitlines()[0]
            line = line.split(']')[-1].strip()
            line = line.replace("Alternative name", '').replace("\"", '').strip()
            lines.append(line)
            # print(line)

    groups = {}
    indi_names = []
    for i in range(len(lines)):
        # print(lines[i])
        indi_names.append(lines[i])
        if ((i+1) % 2) == 0:
            groups[f"Channel-{i}"] = indi_names
            indi_names = []
            # print("\n")

    print(json.dumps(groups, indent=2))
    return groups


def get_audio_devices():

    lines = []
    cmd = "ffmpeg -list_devices true -f dshow -i dummy"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    out = False
    for line in process.stdout:
        if "DirectShow audio devices".upper() in line.upper():
            out = True
            continue
        if "Immediate exit requested".upper() in line.upper():
            out = False

        if out:
            line = line.splitlines()[0]
            line = line.split(']')[-1].strip()
            line = line.replace("Alternative name", '').replace("\"", '').strip()
            lines.append(line)
            # print(line)

    groups = {}
    indi_names = []
    for i in range(len(lines)):
        # print(lines[i])
        indi_names.append(lines[i])
        if ((i+1) % 2) == 0:
            groups[f"Channel-{i}"] = indi_names
            indi_names = []
            # print("\n")

    print(json.dumps(groups, indent=2))
    return groups







channels_list = [("Logitech Webcam C925e", "Microphone (Logitech Webcam C925e)", "ktn"),
                 ("AV TO USB2.0", "Microphone (USB2.0 MIC)", "ntv"),
                 ("Iriun Webcam", "Microphone (Iriun Webcam)", "kBc")]




# get_video_devices()
# get_audio_devices()
# capture_video("Logitech Webcam C925e", "Microphone (Logitech Webcam C925e)", "ktn")

with concurrent.futures.ThreadPoolExecutor(max_workers=25) as excecutor:
    excecutor.map(capture_video, channels_list)

