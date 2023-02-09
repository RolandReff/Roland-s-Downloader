import os
import pytube
import pytranscoder as pytr #Not used at thhe moment
import youtube_dl

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
    #f  = open(download_path,"w+")
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
            videoTitle = yt.title
            #os.rename((download_path+'\\' +yt.title+'.mp4'),(yt.title+'.mp3')) #Error on renaming to change file.
            print(videoTitle +" has been downloaded")
    elif "www.youtube.com" not in Link:    
        if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1): 
            ydl_opts = {format: 'bestvideo+bestaudi','outtmpl': download_path+'\\'+'%(title)s.%(ext)s'} #Format is quality of download, outtmpl is where downloaded video end up
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(Link,download=True)
        elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2): #MP3 placeholder, needs actual code tho
            print("Hello world")
    
    else:
        print("There has been a problem")
    #f.close()

if __name__ == "__main__":
    #help(youtube_dl)
    APPSTATE = True #Need to make something that closes the program from inputs...
    while APPSTATE == True: 
        URL = input("Enter URL: ")
        print('Options:\n1-MP4\n2-MP3')
        Mode = input("Enter format:")
        YoutubeDownloader(URL, Mode)
