import os
import pytube
import pytranscoder as pytr #Not used at thhe moment
import youtube_dl

#Yet to add the For loop for multiple uses
#Add playlist download compatebility
#Add WAV, M4A true format downloads
#Yet to add a check to see if the url and formats are valid, nest that within the mp4 format so auto picks if it uses other or mp4 download method 
#Seems to crash when launching as a normal py file outside of vscode, do that tomorrow when i have gotten some sleep. 
#Check if it can be downloaded and placed in another path and still works.

def YoutubeDownloader(URL, Mode):
    Link = URL
    yt = pytube.YouTube(Link)
    directory_path = os.getcwd()
    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4":
        yt.streams.get_highest_resolution().download(directory_path+'\Download')
        videoTitle = yt.title
        print(videoTitle +"has been downloaded")
    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3": #Downloads only audio as a MP4 file, need conversion to MP3
        yt.streams.filter(only_audio=True).first().download(directory_path+'\Download')
        videoTitle = yt.title
        
        print(videoTitle +" has been downloaded")
        #videoLocation = directory_path +'\Download' +'\\'+ videoTitle # exists for later implementation of the mp4 to mp3 converter.
        #Yes i can be lazy and have it just be renamed, but where is the challange in that.
    elif Mode == "other" or Mode == "Other": #Add this under the Mp4 function, if not youtube.com then youtube-dl --best
       
        ydl_opts = {format: 'bestaudio/bestvideo'} #Video quality is not optimal despit having but bestaudio/bestvideo, may be me getting
        with youtube_dl.YoutubeDL(ydl_opts) as ydl: # the syntax of the options wrong, or the need for a encoder method in the options
            ydl.extract_info(Link,download=True)
    else:
        print("There has been a problem")
    print("Download is now done")

if __name__ == "__main__":
    while True:
        URL = input("Enter URL: ")
        Mode = input("Enter format:")
        YoutubeDownloader(URL, Mode)


