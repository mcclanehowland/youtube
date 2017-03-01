import os
import pytube
from pytube import YouTube
from pyvirtualdisplay import Display
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

filetype = 'mp4'
directory = './batch1/'
client_secrets = "client_secrets.json"

description = "subscribe"
videopath = ""

##Uncomment fo run without opening chrome window
display = Display(visible=0,size=(800,600))
display.start()


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q=Remy+Ma") #search result link


videoobjects = driver.find_elements_by_class_name("yt-uix-tile-link")
videolinks = []
for video in videoobjects:
    videolinks.append(video.get_attribute('href'))

del videolinks[0] ##it's an ad


#
# videos = []
# for link in videolinks:
#     try:
#         driver.get(link)
#         title = driver.find_element_by_id("eow-title").get_attribute('title')
#         keywords = driver.find_element_by_name("keywords").get_attribute('content')
#         videos.append({'ytobject':YouTube(link),'link':link,'title':title,'keywords':keywords})
#         print(title)
#     except pytube.exceptions.AgeRestricted:
#         print("age restriction, moving on")
qualitylist = ['1440p','1080p','720p','480p','360p','240p','144p']
def downup(link,videocount):
    filetype = 'mp4'
    directory = './batch1/'
    client_secrets = "client_secrets.json"
    qualitylist = ['1440p','1080p','720p','480p','360p','240p','144p']
    try:
        driver.get(link)
        title = driver.find_element_by_id("eow-title").get_attribute('title')
        keywords = driver.find_element_by_name("keywords").get_attribute('content')
        filename = 'clip'+str(videocount)

        ytobject = YouTube(link)
        ytobject.set_filename(filename)
        print(title)

    except pytube.exceptions.AgeRestricted:
        print("age restriction, moving on")
    ##Find, get, and upload
    for quality in qualitylist:
        try:
            video = ytobject.get(filetype,quality)
            print(video)
            video.download(directory)
            print('Download succesful')
            print('starting upload')
            videopath = directory+filename+"."+filetype
            # title = vid['title']
            os.system("youtube-upload --title=\""+title+"\" --tags=\""+keywords+"\" --description=\""+description+"\" --client-secrets="+client_secrets+" "+videopath)
            break;

        except pytube.exceptions.DoesNotExist:
            # print("ERROR: Video does not exist")
            continue
        except FileNotFoundError:
            print("ERROR: No such file or directory")
            break;

videocount = 1
for link in videolinks:
    downup(link,videocount)
    videocount = videocount+1
# ##################################################
# # find and get highest quality video and upload it
# ##################################################
# qualitylist = ['1440p','1080p','720p','480p','360p','240p','144p']
# videocount = 1;
# for vid in videos:
#     print('Video '+str(videocount))
#     filename = 'clip'+str(videocount)
#     vid['ytobject'].set_filename(filename)
#     videocount = videocount + 1
#     for quality in qualitylist:
#         try:
#             video = vid['ytobject'].get(filetype,quality)
#             print(video)
#             video.download(directory)
#             print('Download succesful')
#             print('starting upload')
#             videopath = directory+filename+"."+filetype
#             # title = vid['title']
#             os.system("youtube-upload --title=\""+vid['title']+"\" --tags=\""+vid['keywords']+"\" --description=\""+description+"\" --client-secrets="+client_secrets+" "+videopath)
#             break;
#
#         except pytube.exceptions.DoesNotExist:
#             # print("ERROR: Video does not exist")
#             continue
#         except FileNotFoundError:
#             print("ERROR: No such file or directory")
#             break;
