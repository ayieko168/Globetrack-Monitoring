# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from pynput.keyboard import Key, Controller
#
# from time import sleep
# import time
# from requests_html import HTMLSession, HTML
# import pprint
# import requests
# import shutil
#
# chrome_options = webdriver.ChromeOptions()
# prefs = {'download.default_directory': r'C:/Users/royalstate/Projects and Research/Python Projects/Globetrack-Monitoring/Newspaper'}
# chrome_options.add_experimental_option('prefs', prefs)
#
# keyboard = Controller()
# browser = webdriver.Chrome(options=chrome_options)
#
#
# browser.get('https://safaricom.com/discover/e-newspaper/my-newspapers/')
# # browser.maximize_window()
# user_agent = browser.execute_script("return navigator.userAgent;")
# print(user_agent)
#
# # print("Sleeping for 10 seconds...")
# # input("Done?")
# # # html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
# # source = browser.execute_script("return document.body.innerHTML")
# #
# # read_button = browser.find_element_by_css_selector('#read-newspaper')
# # read_button.click()
# #
# # print("Sleeping for 10 seconds...")
# # input("Done?")
# # source = browser.execute_script("return document.body.innerHTML")
# # # print(source)
# #
# # browser.switch_to.window(browser.current_window_handle)
# # input("Done?")
# #
# # with keyboard.pressed(Key.ctrl):
# #     keyboard.press('s')
# #     keyboard.release('s')
# #
# # keyboard.type(f"The Star - {time.time_ns()}")
# #
# # keyboard.press(Key.enter)
# # keyboard.release(Key.enter)
#
#
#
#
# # html = HTML(html=source)
# #
# # hs = html.find('div.MuiGrid-root.MuiGrid-container.MuiGrid-align-items-xs-center.MuiGrid-justify-xs-center')
# # for h in hs:
# #     print(h)
#
# headers = {'User-Agent': user_agent}
# print(headers)
# r = requests.get('https://cp.safaricom.com/static-assets/publications/optimized/3/1837/oiG7SYNNY-WEEKEND STAR 17th April 2021-1.jpg',
#                  headers=headers)
# print(r.status_code)
# if r.status_code == 200:
#     with open("img.png", 'wb') as f:
#         r.raw.decode_content = True
#         shutil.copyfileobj(r.raw, f)
#
