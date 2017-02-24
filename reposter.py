import os
import pytube
from pytube import YouTube

title = "Meme compilation v"
tags = "dank memes vine compilation,dank memes,dank,memes,meme,dankest memes,best memes,dankest,kek,edgy,dank meme vine,dank vines,meme vines,stolen memes for stolen kids,dank meme songs,dank meme music,dank music,dank songs,dank meme compilation,dank compilation,meme compilation,funny,MLG,dank memes v5,dank memes vine compilation v5,fresh memes,try not to laugh challange,meme vine,funny meme,try not to laugh,Shocker,v16,fresh dank memes vine compilation v16"
client_secrets = "client_secrets.json"
description = "best memes you ever saw"
videopath = ""




filetype = 'mp4'
# directory = './video1/'
directory = './video10/'


urllist = ["https://www.youtube.com/watch?v=EC-5PyzH7ew","https://www.youtube.com/watch?v=xzGynDnKst8","https://www.youtube.com/watch?v=SMxIHalZHyE&t=2s","https://www.youtube.com/watch?v=wqPpHh20jK8","https://www.youtube.com/watch?v=dprHL6nm18o"]
videolist = []
for url in urllist:
    videolist.append(YouTube(url))

############################
# find and get highest quality video
############################
qualitylist = ['1440p','1080p','720p','480p','360p','240p','144p']
videocount = 1;
for vid in videolist:
    print('Video '+str(videocount))
    filename = 'clip'+str(videocount)
    vid.set_filename(filename)
    videocount = videocount + 1
    for quality in qualitylist:
        try:
            video = vid.get(filetype,quality)
            print(video)
            video.download(directory)
            print('Download succesful')
            print('starting upload')
            videopath = directory+filename+"."+filetype
            title = title+" "+str(videocount)
            os.system("youtube-upload --title=\""+title+"\" --description=\""+description+"\" --client-secrets="+client_secrets+" "+videopath)
            break;

        except pytube.exceptions.DoesNotExist:
            # print("ERROR: Video does not exist")
            continue
        except FileNotFoundError:
            print("ERROR: No such file or directory")
            break;
