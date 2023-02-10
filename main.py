import os
import pytube
import youtube_dl
import datetime #For later use 

#Add playlist download compatebility
#Add WAV, M4A true format downloads
#Yet to add a check to see if the url and formats are valid, nest that within the mp4 format so auto picks if it uses other or mp4 download method 
#Seem to lack the premissions to write to the download folder outside of VSCODE, error code 5 and 13
#Works almost perfect in VSCODE, fucking useless outside due to lack of premissions


def YoutubeDownloader(URL, Mode):
    Link = URL
    Mode  = str(Mode)
    directory_path = os.getcwd()
    download_path = directory_path+'\\Download'
   
    if "www.youtube.com" in Link:
        yt = pytube.YouTube(Link)
        if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1):
            yt = pytube.YouTube(Link)
            yt.streams.get_highest_resolution().download(download_path) 
            videoTitle = yt.title
            print(videoTitle +" has been downloaded")

        elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2): #Downloads only audio as a MP4 file, need conversion to MP3
            yt = pytube.YouTube(Link)
            out_file= yt.streams.filter(only_audio=True).first().download(directory_path+'\\Download')
            NewTitle = out_file.replace('.mp4','')
            os.rename((out_file),(NewTitle+'.mp3'))
            print(yt.title +" has been downloaded") #Be aware that newtitle is not orignal path when file is downloaded

    elif "www.youtube.com" not in Link:    
        if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1): 
            ydl_opts = {format: 'bestvideo+bestaudi','outtmpl': download_path+'\\'+'%(title)s.%(ext)s'} #Format is quality of download, outtmpl is where downloaded video end up
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(Link,download=True)

        elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2): #MP3 placeholder, needs actual code tho
            
            #ydl_opts = {'format': 'bestaudio/best','outtmpl': download_path+'\\'+'%(title)s.%(ext)s', 'ffmpeg-location': str(directory_path+'\\venv\\Scripts\\ffmpeg'),'ffprobe-loocation':str(directory_path+'\\venv\\Scripts\\ffprobe') ,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'wav'}],} #WAV template for later use
            ydl_opts = {'format': 'bestaudio/best','outtmpl': download_path+'\\'+'%(title)s.%(ext)s', 'ffmpeg-location': str(directory_path+'\\venv\\Scripts\\ffmpeg'),'ffprobe-loocation':str(directory_path+'\\venv\\Scripts\\ffprobe') ,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3', 'preferredquality': '192',}],} #Format is quality of download, outtmpl is where downloaded video end up
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(Link,download=True)
    
    else:
        print("There has been a problem")

if __name__ == "__main__":
    #help(youtube_dl)
    #print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    APPSTATE = True #Need to make something that closes the program from inputs...
    while APPSTATE == True: 
        print('URL example: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        URL = input("Enter URL: ")
        print('Options:\n1-MP4\n2-MP3')
        Mode = input("Enter format:")
        YoutubeDownloader(URL, Mode)
