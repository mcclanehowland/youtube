import pytube
from pytube import YouTube



filetype = 'mp4'
# directory = './video1/'
directory = './video9/'


urllist = ["https://www.youtube.com/watch?v=EC-5PyzH7ew"]
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


#video = yt.get(yt.filter('.mp4'[-1]))

# try:
#     video = yt.get('mp4')
#     video.download('./')
#
# except pytube.exceptions.DoesNotExist:
#     print("ERROR: Video does not exist")
# except FileNotFoundError:
#     print("ERROR: No such file or directory")
