from pytube import YouTube 
from sys import argv 

print(argv[0])
video_link = argv[1]
download_path = argv[2]


yt = YouTube(video_link)
downloader = yt.streams.filter(file_extension='mp4').get_highest_resolution()
downloader.download(download_path)