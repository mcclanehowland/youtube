import os

title = "Meme compilation"
tags = "memes, meme compilation, meme"
client_secrets = "client_secrets.json"
description = "best memes you ever saw"
videopath = "video9/clip1.mp4"

os.system("youtube-upload --title=\""+title+"\" --description=\""+description+"\" --client-secrets="+client_secrets+" "+videopath)
