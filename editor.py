from moviepy.editor import *


# clip = VideoFileClip("video1/clip1.mp4").margin(20)
# clip2 = VideoFileClip("video1/clip2.mp4").margin(20)
# final = CompositeVideoClip([clip,clip2])
# final.write_videofile("final.mp4",fps=24)

final = VideoFileClip("video2/clip1.mp4").margin(20)
final.write_videofile("video2/final.mp4")

# videonumber = 1
# numberofclips = 2
#
# cliplist = []
# for num in range(numberofclips):
#     cliplist.append(VideoFileClip("video"+str(videonumber)+"/clip"+str(num+1)+".mp4"))
#
# video = concatenate_videoclips(cliplist)
# video.fps=30
# video.write_videofile("video"+str(videonumber)+".MP4")
