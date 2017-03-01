import os
import pytube
from pytube import YouTube
from pyvirtualdisplay import Display
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

##Uncomment fo run without opening chrome window
display = Display(visible=0,size=(800,600))
display.start()

driver = webdriver.Chrome()

def downup(link,videocount):
    filetype = 'mp4'
    directory = './batch1/'
    description = ""
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
    downup(driver.find_element_by_class_name("watch-sidebar-body").get_attribute('href'),videocount+1)


downup("https://www.youtube.com/watch?v=FWkDYkPyvNM",1)
