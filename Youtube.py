import os
from pytube import YouTube

try:
    newpath = r'Youtube Downloaded videos'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


    link = input("youtube link: ")
    video = YouTube(link).streams.filter(res="720p").first()
    print("downloading")
    video.download(r'Youtube Downloaded videos')
    print("Downloaded!")

except SyntaxError:
    print("error happened please reset program")