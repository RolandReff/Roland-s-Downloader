import unittest
import subprocess
import main
import os

class test_main(unittest.TestCase):
    def test_yt_dl_installed(self):
        self.assertNotEqual(subprocess.check_output("where youtube-dl"),"INFO: Could not find files for the given pattern(s).")

    def test_ffprobe_installed(self):
        self.assertNotEqual(subprocess.check_output("where ffprobe"),"INFO: Could not find files for the given pattern(s).")

    def test_ffmpeg_installed(self):
        self.assertNotEqual(subprocess.check_output("where ffmpeg"),"INFO: Could not find files for the given pattern(s).")

    def test_files_youtube_downloaded(self):
        main.YoutubeDownloader("https://www.youtube.com/watch?v=vGyHXW0lwZY","mp4")
        self.assertTrue(os.path.isfile(r".\download\Doggo Takes Flight.mp4"))
    
        main.YoutubeDownloader("https://www.youtube.com/watch?v=zdeZwAk6ULE","mp3")
        self.assertTrue(os.path.isfile(r".\download\Undertale OST 024 - Bonetrousle.mp3"))

    def test_files_other_downloader(self):
        main.OtherDownloader("https://tv.nrk.no/serie/foerstegangstjenesten/ekstramateriale/KMNO10007421/avspiller","mp4")
        self.assertTrue(os.path.isfile(r".\download\Førstegangstjenesten.mp4"))
        
        main.OtherDownloader("https://soundcloud.com/rick-astley-official/never-gonna-give-you-up-4","mp3")
        self.assertTrue(os.path.isfile(r".\download\Never Gonna Give You Up.mp3"))

if __name__ == '__main__':
    unittest.main()
    