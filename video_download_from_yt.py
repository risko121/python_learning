#video_download_from_yt

!apt install pytube
import pytube 

def download(link):
  videoobj = youtube(link)
  videoobj = youtube.streams.get_highest_resolution()
  try:
    videoobj.download()
  except:
    print("error")
  print("video downloaded")


link = input("paste your video link here:")
download(link)
