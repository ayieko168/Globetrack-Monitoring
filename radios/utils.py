
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from datetime import datetime
import os
import subprocess


def open_rms_links_from_list():

    """ Similar to open_rms_radio_links but opens the links from a list of indises provides """

    page_indices = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    base_url = "https://viusasa.com/radio"  # https://viusasa.com/radio/<page_number>

    for page in page_indices:

        ## Ignore tv links
        tv_ids = []

        formated_url = f"{base_url}/{page}"
        webbrowser.open_new_tab(formated_url)

        print(f"Openning URL: {formated_url}...")


def get_rms_radio_links():

    """ This will get links to individual page for the radio links in the viusasa RMS website """

    page_indices = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    base_url = "https://viusasa.com/radio"  # https://viusasa.com/radio/<page_number>

    urls_list = []

    for page in page_indices:
        
        formated_url = f"{base_url}/{page}"

        urls_list.append(formated_url)

    # print(urls_list)
    return urls_list


def extract_stream_links(radio_links=[]):

    WAIT_RENDER = 60
    radio_links = get_rms_radio_links()
    random.shuffle(radio_links)
    stream_links = []

    # print(radio_links)

    for i, link in enumerate(radio_links):

        print(f"Processing {link} - [{i} of {len(radio_links)}]")
        driver = webdriver.Chrome()
        # driver.minimize_window()
        driver.get(link)

        print(f"Waiting for {WAIT_RENDER} Secs to render page...")
        time.sleep(WAIT_RENDER)

        print("trying to get link...")
        try:
            html_source = driver.page_source
            elem = driver.find_element(By.XPATH, "//*[@id='playlists']/li")
            stream_link = elem.get_attribute("data-video-source")
            print(f"Got stream link... {stream_link}")
            stream_links.append(stream_link)

        except Exception as e:
            print(f"Could not get the stram link for {link}")
            print(f"Error is ... \n{'#'*60} \n{e} \n{'#'*60} \n")


        driver.quit()

        # break

    ## Save the links to a text file
    print(f"\n\nWriting the stream urls to file")
    with open("stream_links.txt", 'w') as fo:
        for li in stream_links:
            fo.writelines(li+"\n")


def record_radio_station(args):
    """ This will start recording a radio station stream. Is designed to be used with threading. """

    ## Get the args
    stream_link, channel_name = args

    ## Clean the args
    channel_name = channel_name.upper().replace(' ', '_')

    root_dir = f"{os.sep}".join(os.path.abspath(__file__).split(os.sep)[:-1])

    ## Recording format and directory
    FORMAT = 'MP3'.lower()
    recording_path = f"{root_dir}/RADIO_RECORDINGS/{channel_name}"

    if not os.path.exists(recording_path):
        print(f"[{channel_name}] Recording directory not found for {channel_name}, creating one...")
        os.makedirs(recording_path)

    ## Start recording loop, records in 10 minute intervals
    while True:
        start_time = time.time()

        command = f"""ffmpeg -y -i {stream_link} "{recording_path}/{datetime.now().strftime('%a-%d-%b-%Y_%I-%M%p')}.{FORMAT}" """
        print(command)

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:
            print(line)

            if int(time.time() - start_time) > 300:
                print(f"[{channel_name}] terminating...")
                process.terminate()
                record_radio_station((stream_link, channel_name))




record_radio_station(("https://61115b0a477b5.streamlock.net:8443/radiocitizen/radiocitizen/playlist.m3u8", "radio citizen"))















