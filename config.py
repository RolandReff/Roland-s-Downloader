import os

def find(name, path): #used for finding the path of ffmpeg and ffprobe. 
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


class config:
    def __init__(self):
        self.directory_path = os.getcwd()
        self.downloaldFolderPath = os.path.join(os.getcwd(), "download")
        self.ffmpegPath = find("ffmpeg.exe", self.directory_path)
        self.ffprobePath = find("ffprobe.exe", self.directory_path)

    def checkFfmpegAndFfprobeStatus(self):
        if self.ffmpeg_path == None:
             print("ffmpeg not found in the directory, you wont be able to download files")
        if self.ffprobePath == None:
             print("ffprobe not found in the directory, you wont be able to download files")
    
    def createDownloadFolder(self):
        if not os.path.isdir(self.downloaldFolderPath): # Makes a download path if there isn't one
            os.makedirs(self.downloaldFolderPath)
            print("download folder created!")
    


