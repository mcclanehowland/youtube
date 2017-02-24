import pytube
from pytube import YouTube
from moviepy.editor import *




filetype = 'mp4'
directory = './video7/'

links = open('links.txt')
urllist = []

for line in links:
    urllist.append(line)



# urllist = ["https://www.youtube.com/watch?v=bwTTd0kQZKE","https://www.youtube.com/watch?v=p3HxIpiIh6w"]
# urllist = ["https://www.youtube.com/watch?v=AWLH6m5kyQY&t=3s"]
# urllist = ["https://www.youtube.com/watch?v=f9b7G2khidY"]
videolist = []
for url in urllist:
    videolist.append(YouTube(url))


# print(yt.get_videos())
#
# print(yt.filename)
#
# yt.set_filename('newname')
#
# print(yt.filter('mp4'))

############################
# find and get highest quality video
############################
qualitylist = ['1440p','1080p','720p','480p','360p','240p','144p']
videocount = 1;
for vid in videolist:
    print('Video '+str(videocount))
    vid.set_filename('clip'+str(videocount))
    videocount = videocount + 1
    for quality in qualitylist:
        try:
            video = vid.get(filetype,quality)
            print(video)
            video.download(directory)
            print('Download succesful')
            break;

        except pytube.exceptions.DoesNotExist:
            # print("ERROR: Video does not exist")
            continue
        except FileNotFoundError:
            print("ERROR: No such file or directory")
            break;

cliplist = []
clipnumber = 1
# print(range(videocount-1))
for clip in range(videocount-1):
    # cliplist.append(VideoFileClip(directory+"clip"+str(clipnumber)+"."+filetype))
    # cliplist.append(VideoFileClip('./video4/clip1.mp4'))
    cliplist.append(VideoFileClip(directory+'clip'+str(clipnumber)+'.'+filetype))
    clipnumber = clipnumber+1


finalvideo = concatenate_videoclips(cliplist)
finalvideo.fps=30
finalvideo.write_videofile(directory+"finalvideo."+filetype)

# final = VideoFileClip("video2/clip1.mp4").margin(20)
# final.write_videofile("video2/final.mp4")




#video = yt.get(yt.filter('.mp4'[-1]))

# try:
#     video = yt.get('mp4')
#     video.download('./')
#
# except pytube.exceptions.DoesNotExist:
#     print("ERROR: Video does not exist")
# except FileNotFoundError:
#     print("ERROR: No such file or directory")
