import os
import pytube
import youtube_dl
import ffmpeg

def is_supported(URL): #https://stackoverflow.com/a/61489622 <3
    try:
        extractors = youtube_dl.extractor.gen_extractors()
        for e in extractors:
            if e.suitable(URL) and e.IE_NAME != 'generic':
                return True
        return False
    except:
        return False
    
def DownloaderChoice(URL, Mode):
    if ("www.youtube.com" in URL):
        YoutubeDownloader(URL, Mode)
    elif is_supported(URL) == True:
       OtherDownloader(URL, Mode)
    else:   
        print("The URL is not valid or not supported.")

def YoutubeDownloader(URL, Mode):    
    yt = pytube.YouTube(URL)
    if Mode == "mp4" or Mode == "MP4" or Mode == "Mp4" or Mode == str(1):
        input1 = yt.streams.get_by_itag(ItagChecker(yt,"video")).download(output_path=".\download")
        base1, ext1 = os.path.splitext(input1)
        os.rename(input1,os.path.join(".\download",'input-a'+ext1))
        input2 = yt.streams.get_by_itag(ItagChecker(yt,"audio")).download(output_path=".\download")
        base2, ext2 = os.path.splitext(input2)
        os.rename(input2,os.path.join(".\download",'input-b'+ext2))

        input_video = ffmpeg.input(r'./download/input-a'+ext1)
        input_audio = ffmpeg.input(r'./download/input-b'+ext2)

        stream = ffmpeg.output(input_video, input_audio,'./download/output.mp4',vcodec = 'copy', crf = 'copy', acodec = 'copy')
        ffmpeg.run(stream)

        os.rename(os.path.join(".\download","output.mp4"),os.path.join(".\download",base1+".mp4"))

        os.remove(os.path.join(".\download","input-a"+ext1))
        os.remove(os.path.join(".\download","input-b"+ext2))
    
        print('"'+yt.title+'"'+ " has been downloaded")

    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2):
        input = yt.streams.get_by_itag(ItagChecker(yt,"audio")).download(output_path=".\download")
        base, ext = os.path.splitext(input)
        
        os.rename(input,os.path.join(".\download",'input'+ext))
        input_audio = ffmpeg.input(r'./download/input'+ext)
        
        stream = ffmpeg.output(input_audio, './download/output.mp3',crf = 'copy', acodec = 'libmp3lame', format = 'mp3')
        ffmpeg.run(stream)
       
        os.rename(os.path.join(".\download","output.mp3"),os.path.join(".\download",base+".mp3"))
        os.remove(os.path.join(".\download","input"+ext))
        
        print(yt.title +" has been downloaded") 
    else:
        print("There has been a problem")
    

def ItagChecker(yt,audioOrVideo): #TO-DO: Make it so older videos where audio and video is in a single file can be downloaded without bricking the script. 
    if audioOrVideo == "video":
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
        ydl_opts = {format: 'bestvideo+bestaudi','outtmpl': os.path.join("\download",'%(title)s.%(ext)s'),'postprocessors': [{ 'key': 'FFmpegVideoConvertor','preferedformat': 'mp4', }],} #Format is quality of download, outtmpl is where downloaded video end up 
    elif Mode == "mp3" or Mode == "MP3" or Mode == "Mp3" or Mode == str(2):
        ydl_opts = {'format': 'bestaudio/best','outtmpl': os.path.join("\download",'%(title)s.%(ext)s'),'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3', 'preferredquality': '192',}],} #Format is quality of download, outtmpl is where downloaded video end up
    elif Mode == "wav" or Mode == "WAV" or Mode == "Wav" or Mode == str(3):
        ydl_opts = {'format': 'bestaudio/best','outtmpl': os.path.join("\download",'%(title)s.%(ext)s'),'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'wav',}],} #WAV template for later use

    else:
        print("There has been a problem")
        return

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        download = ydl.extract_info(URL,download=True)
        print(str('"'+download.get('title', None)) + '" has been downloaded')

if __name__ == "__main__":
    if not os.path.isdir("download"): # Makes a download path if there isn't one
            os.makedirs("download")
            print("download folder created!")
    
    APPSTATE = True
    while APPSTATE == True: 
        print('URL example: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        URL = input("Enter URL: ")
        if URL == "exit":
            APPSTATE = False
            break
        print('Options:\n1-MP4\n2-MP3') #\n3-WAV not added yet to both downloaders
        Mode = input("Enter format:")
        

        DownloaderChoice(URL, Mode)
    
    
