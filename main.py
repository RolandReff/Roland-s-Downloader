import os
import pytube
import youtube_dl
from ffmpeg import FFmpeg, Progress

from config import config


# 18/8/2023
#TLDR, Google enginers are at warfare with the devs, use this ciper for the pytube downnload function to work with 15.0.0
# https://github.com/oncename/pytube/blob/master/pytube/cipher.py

#Add playlist download compatebility
#Add WAV, M4A true format downloads

def is_supported(URL): #https://stackoverflow.com/a/61489622
    try:
        extractors = youtube_dl.extractor.gen_extractors()
        for e in extractors:
            if e.suitable(URL) and e.IE_NAME != 'generic':
                return True
        return False
    except:
        return False

def Menu(): 
    global mainConfig 
    mainConfig = config()
    mainConfig.createDownloadFolder()
    
    APPSTATE = True
    while APPSTATE == True: 
        print('URL example: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        URL = input("Enter URL: ")
        print('Options:\n1-MP4\n2-MP3') #\n3-WAV not added yet to both downloaders
        Mode = input("Enter format:")
        DownloaderChoice(URL, Mode)

def TestMenu(): #Reserved funtion for testing
    print("Hei Verden")
    
def DownloaderChoice(URL, Mode):
    if ("www.youtube.com" in URL):
        YoutubeDownloader(URL, Mode)
    elif is_supported(URL) == True:
       OtherDownloader(URL, Mode)
    else:   
        print("The URL is not valid")

def YoutubeDownloader(URL, Mode):    
    yt = pytube.YouTube(URL)
    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1):
        input1 = yt.streams.get_by_itag(ItagChecker(yt,False)).download()
        base, ext = os.path.splitext(input1)
        os.rename(input1,os.path.join(mainConfig.downloaldFolderPath,"input-a"))
        input2 = yt.streams.get_by_itag(ItagChecker(yt,True)).download(output_path=mainConfig.downloaldFolderPath, filename="input-b")
        ffmpeg = (FFmpeg(executable=mainConfig.ffmpegPath)
            .option("y")
            .input(os.path.join(mainConfig.downloaldFolderPath,"input-a"))
            .input(os.path.join(mainConfig.downloaldFolderPath,"input-b"))
            .output(os.path.join(mainConfig.downloaldFolderPath,"output.mp4"),
            map=["0:v","1:a"], vcodec = 'copy', crf = 'copy', acodec = 'copy',

             )
        )

        @ffmpeg.on("progress")
        def on_progress(progress: Progress):
            print(progress)
    
        ffmpeg.execute() #The program pauses on this line until the encoding is done
    
        os.remove(os.path.join(mainConfig.downloaldFolderPath,"input-a"))
        os.remove(os.path.join(mainConfig.downloaldFolderPath,"input-b"))
    
        try:
         os.rename(os.path.join(config["download__folder_path"],"output.mp4"),os.path.join(mainConfig.downloaldFolderPath,base+".mp4"))
         print('"'+yt.title+'"'+ " has been downloaded")
        except:
            os.remove(os.path.join(config["download__folder_path"],"output.mp4"))
            print("Video already exists") 

    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2): #Downloads only audio as a MP4 file, need conversion to MP3
        out_file= yt.streams.filter(only_audio=True).get_by_itag(ItagChecker(yt,True)).download(mainConfig.downloaldFolderPath)
        NewTitle = out_file.replace('.mp4','')
        os.rename((out_file),(NewTitle+'.mp3'))
        print(yt.title +" has been downloaded") #Be aware that newtitle is not orignal path when file is downloaded
    else:
        print("There has been a problem")
    

def ItagChecker(yt,audioTrueOrFalse): #Need to swap around the lists so i search the most common itags first so it does not take ages.
    if audioTrueOrFalse == False:
        print("Finding optimal video files...")
        itags = [699,399,335,303,248,299,137,698,398,334,302,247,298,136] #Video itags from youtube.com
    else:
        print("Finding optimal audio files...")
        itags = [140,141,139] #Audio itags from yotube.com

    for Fitag in itags:
        yt.streams.get_by_itag(Fitag)
        if yt.streams.get_by_itag(Fitag) is not None:
            itag = Fitag
            break
    return itag


def OtherDownloader(URL, Mode):
    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1):
        ydl_opts = {format: 'bestvideo+bestaudi','outtmpl': os.path.join(mainConfig.downloaldFolderPath,'%(title)s.%(ext)s'), 'ffmpeg-location': mainConfig.ffmpegPath,'ffprobe-loocation': mainConfig.ffprobePath,'postprocessors': [{ 'key': 'FFmpegVideoConvertor','preferedformat': 'mp4', }],} #Format is quality of download, outtmpl is where downloaded video end up 
    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2):
        ydl_opts = {'format': 'bestaudio/best','outtmpl': os.path.join(mainConfig.downloaldFolderPath,'%(title)s.%(ext)s'), 'ffmpeg-location': mainConfig.ffmpegPath,'ffprobe-loocation': mainConfig.ffprobePath ,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3', 'preferredquality': '192',}],} #Format is quality of download, outtmpl is where downloaded video end up
    elif Mode == "wav" or Mode == "WAV" or Mode == "Wav" or Mode == str(3):
        ydl_opts = {'format': 'bestaudio/best','outtmpl': os.path.join(mainConfig.downloaldFolderPath,'%(title)s.%(ext)s'), 'ffmpeg-location': mainConfig.ffmpegPath,'ffprobe-loocation':mainConfig.ffprobePath,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'wav',}],} #WAV template for later use

    else:
        print("There has been a problem")
        return

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        download = ydl.extract_info(URL,download=True)
        print(str('"'+download.get('title', None)) + '" has been downloaded')

if __name__ == "__main__":
    Menu()
    
    


    
    
