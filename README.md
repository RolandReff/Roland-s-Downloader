# Roland's Downloader
This is a personal project made and designed to simplify the process of downloading vidoes 
from various websites usin pytube and youtube-dl. 


## Functions
Download youtube videos in the following formats with Pytube:
- MP4
- Mp3

Download videos from a [variety of websites](https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md) in the following formats with youtube-dl and ffmpeg:
- MP4
- MP3

## Requirements
- [The listed python libraries](https://github.com/RolandReff/Roland-s-Downloader/blob/main/requirements.txt)
- FFMPEG and FFPROBE


## To-DO!
- Add WAV (audio only) and WAV (Video and Audio) Formats
- Add M4A format download option
- Add FFMPEG and FFPROBE check to prevent error codes at encoding attempts without them
- Improve ease of editing (restructure and split up in smaller Functions)
- Add Playlist download option
- Add easy-to-use video encoding options with FFMPEG (bulk and single)


## Bugs
- Encountring an error that crashes the script on my desktop at the moment of creating the path for downloaded 
  video, due to WinError 5 and 13, can be fixed if you run the script with the following on win10 Home 64-bit,
  "python -i PATH\main.py",seems to be a local problem, based on the fact it runs perfectly on my laptop
  which is running Win11 Home 64-bit. Has to be tested on other devices.



