import os
import pathlib as path
import pytube
import youtube_dl
import yt_dlp

# 15/7/2023 2:30
#TLDR, Google enginers are at warfare with the devs, use this ciper for the pytube downnload function to work with 15.0.0
# https://github.com/oncename/pytube/blob/master/pytube/cipher.py

#Add playlist download compatebility
#Add WAV, M4A true format downloads
#Yet to add a check to see if the url and formats are valid, nest that within the mp4 format so auto picks if it uses other or mp4 download method 
#Works almost perfect in VSCODE, fucking useless outside due to lack of premissions

        
def boot(): #This boot function is peak spaghetti code, have a look to make it better when I've gotten it to work. 
    
    if not  os.path.isdir(config_folder_path): #Makes the config folder 
        os.makedirs(config_folder_path)
        print("Config folder created!")
   
    if not os.path.isfile(config_path): #Makes the config.txt file withinh the config folder 
        with open(config_path,"w") as config_file:
            config_file.write("FFMPEGPATH = \n")
            config_file.write("FFPROBEPATH =\n")
            config_file.write("configState = ")
            print("config.txt has been created within " + config_path)

    if not os.path.isdir(download__folder_path): # Makes a download path if there isn't one
        os.makedirs(download__folder_path)
        print("download folder created!")
    
    with open(config_path,"a+") as config_file: #NOT DONE, what checks the location of key folder and files, and writes it to a txt that will be used by the script.
        for line in config_file:
            if line == "FFMPEGPATH = \n":
                config_file.write(find("ffmpeg.exe",directory_path))
            if line == "FFPROBEPATH =\n":
                config_file.write(find("ffprobe.exe", directory_path))
            


def find(name, path): #Shameless yoink from Stackoverflow user Nadia Alramli, used for finding the path of ffmpeg and ffprobe. 
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)




def Menu(): #VERY ROUGH DRAFT, ONLY USED FOR TESTING CURRENTLY
    APPSTATE = True #Need to make something that closes the program from inputs...
    while APPSTATE == True: 
        print('URL example: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        #URL = "https://www.youtube.com/watch?v=Z0oU5k2ECIQ1"
        URL = input("Enter URL: ")
        print('Options:\n1-MP4\n2-MP3')
        Mode = input("Enter format:")
        #Mode = "1"
        DownloaderChoice(URL, Mode)

def DebugMenu(): #Reserved funtion for later implementation when program is ready for deployment for other users.
    print("Hei Verden")

def DownloaderChoice(URL, Mode):
    if "www.youtube.com" in URL:
        YoutubeDownloader(URL, Mode)
    #else:
    #    OtherDownloader(URL, Mode)

def YoutubeDownloader(URL, Mode):
    
    Mode  = str(Mode)
    directory_path = os.getcwd()
    download_path = directory_path+'\\Download'
    yt = pytube.YouTube(URL)
    
    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1):
        yt = pytube.YouTube(URL)
        stream =yt.streams.get_highest_resolution() #Gives only 1080P on certion videos, needs to be fixed.
        finished = stream.download(download_path)
        videoTitle = yt.title
        print(videoTitle +" has been downloaded")

    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2): #Downloads only audio as a MP4 file, need conversion to MP3
        yt = pytube.YouTube(URL)
        out_file= yt.streams.filter(only_audio=True).first().download(directory_path+'\\Download')
        NewTitle = out_file.replace('.mp4','')
        os.rename((out_file),(NewTitle+'.mp3'))
        print(yt.title +" has been downloaded") #Be aware that newtitle is not orignal path when file is downloaded
    else:
        print("There has been a problem")

def OtherDownloader(URL, Mode):
    Mode  = str(Mode)
    directory_path = os.getcwd()
    download_path = directory_path+'\\Download'
    
        
    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1): 
        ydl_opts = {format: 'bestvideo+bestaudi','outtmpl': download_path+'\\'+'%(title)s.%(ext)s'} #Format is quality of download, outtmpl is where downloaded video end up
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(URL,download=True)

    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2): #MP3 placeholder, needs actual code tho
    
         #ydl_opts = {'format': 'bestaudio/best','outtmpl': download_path+'\\'+'%(title)s.%(ext)s', 'ffmpeg-location': str(directory_path+'\\venv\\Scripts\\ffmpeg'),'ffprobe-loocation':str(directory_path+'\\venv\\Scripts\\ffprobe') ,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'wav'}],} #WAV template for later use
        ydl_opts = {'format': 'bestaudio/best','outtmpl': download_path+'\\'+'%(title)s.%(ext)s', 'ffmpeg-location': str(directory_path+'\\venv\\Scripts\\ffmpeg'),'ffprobe-loocation':str(directory_path+'\\venv\\Scripts\\ffprobe') ,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3', 'preferredquality': '192',}],} #Format is quality of download, outtmpl is where downloaded video end up
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(URL,download=True)
    else:
        print("There has been a problem")

if __name__ == "__main__":
    directory_path = os.getcwd()
    config_folder_path = os.path.join(directory_path,"config") 
    config_path = os.path.join(config_folder_path, "config.txt") 
    download__folder_path = os.path.join(directory_path, "download")
    boot()

