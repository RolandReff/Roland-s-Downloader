import os
import pytube
import youtube_dl

# 18/8/2023
#TLDR, Google enginers are at warfare with the devs, use this ciper for the pytube downnload function to work with 15.0.0
# https://github.com/oncename/pytube/blob/master/pytube/cipher.py

#Add playlist download compatebility
#Add WAV, M4A true format downloads
#Works almost perfect in VSCODE, fucking useless outside due to lack of premissions

def boot(): 
    #creates the config dictonary that the rest of the program uses and checks if ffpmeg and ffprobe is installed
    #Sucks that i have to drag the config var around, but it is what it is 
    #This could be done in another way if I made a class, but i cant be asked 
    
    print("TLDR, Google enginers are at warfare with the devs, change the pytube cipher to this for the pytube downnload function to work with 15.0.0 \n https://github.com/oncename/pytube/blob/master/pytube/cipher.py")
    
    config = {
        "directory_path":os.getcwd(),
        "download__folder_path":os.path.join(os.getcwd(), "download"),
        "ffmpeg_path":"",
        "ffprobe_path":"",
        "allowOtherDownloader":False
    }
    config["ffmpeg_path"] = find("ffmpeg.exe", config["directory_path"])
    config["ffprobe_path"] = find("ffprobe.exe", config["directory_path"])

    if not config["ffmpeg_path"] == None and not config["ffprobe_path"] == None:
        config["allowOtherDownloader"] = True
    elif config["ffmpeg_path"] == None:
        print("ffmpeg not found in the directory, you wont be able to download from outside of youtube")
    elif config["ffprobe_path"] == None:
        print("ffprobe not found in the directory, you wont be able to download from outside of youtube")

    if not os.path.isdir(config["download__folder_path"]): # Makes a download path if there isn't one
        os.makedirs(config["download__folder_path"])
        print("download folder created!")
    return config

def find(name, path): #used for finding the path of ffmpeg and ffprobe. 
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def is_supported(URL): #https://stackoverflow.com/a/61489622
    extractors = youtube_dl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(URL) and e.IE_NAME != 'generic':
            return True
    return False

def Menu(): #VERY ROUGH DRAFT, ONLY USED FOR TESTING CURRENTLY
    config = boot()
    
    APPSTATE = True
    while APPSTATE == True: 
        print('URL example: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
        URL = input("Enter URL: ")
        print('Options:\n1-MP4\n2-MP3')
        Mode = input("Enter format:")
        DownloaderChoice(URL, Mode, config)

def DebugMenu(): #Reserved funtion for later implementation when program is ready for deployment for other users.
    print("Hei Verden")

def DownloaderChoice(URL, Mode, config): #need to add a check to see if it is actually a valid url so it doesn't just chuck nonesense at it
    if "www.youtube.com" in URL:
        YoutubeDownloader(URL, Mode,config)
    elif is_supported(URL) == True and config["allowOtherDownloader"] == True:
       OtherDownloader(URL, Mode, config)
    else:   
        print("Sorry, not a valid URL")
def YoutubeDownloader(URL, Mode, config):
    
    yt = pytube.YouTube(URL)
    
    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1):
        yt = pytube.YouTube(URL)
        stream =yt.streams.get_highest_resolution() #Gives only 1080P on certion videos, needs to be fixed.
        finished = stream.download(config["download__folder_path"])
        videoTitle = yt.title
        print(videoTitle +" has been downloaded")

    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2): #Downloads only audio as a MP4 file, need conversion to MP3
        yt = pytube.YouTube(URL)
        out_file= yt.streams.filter(only_audio=True).first().download(config["download__folder_path"])
        NewTitle = out_file.replace('.mp4','')
        os.rename((out_file),(NewTitle+'.mp3'))
        print(yt.title +" has been downloaded") #Be aware that newtitle is not orignal path when file is downloaded
    else:
        print("There has been a problem")

def OtherDownloader(URL, Mode,config):

    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1): #The video download does not seem to work
        ydl_opts = {format: 'bestvideo+bestaudi','outtmpl': config["download__folder_path"]+'\\'+'%(title)s.%(ext)s', 'ffmpeg-location': config["ffmpeg_path"],'ffprobe-loocation': config["ffprobe_path"],'postprocessors': [{ 'key': 'FFmpegVideoConvertor','preferedformat': 'mp4', }],} #Format is quality of download, outtmpl is where downloaded video end up
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(URL,download=True)

    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2):
         #ydl_opts = {'format': 'bestaudio/best','outtmpl': download_path+'\\'+'%(title)s.%(ext)s', 'ffmpeg-location': str(directory_path+'\\venv\\Scripts\\ffmpeg'),'ffprobe-loocation':str(directory_path+'\\venv\\Scripts\\ffprobe') ,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'wav'}],} #WAV template for later use
        ydl_opts = {'format': 'bestaudio/best','outtmpl': config["download__folder_path"]+'\\'+'%(title)s.%(ext)s', 'ffmpeg-location': config["ffmpeg_path"],'ffprobe-loocation': config["ffprobe_path"] ,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3', 'preferredquality': '192',}],} #Format is quality of download, outtmpl is where downloaded video end up
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(URL,download=True)
    else:
        print("There has been a problem")

if __name__ == "__main__":
    Menu()
    
