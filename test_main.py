import unittest
import subprocess
import main

class test_main(unittest.TestCase):
    def test_yt_dl_installed(self):
        self.assertEqual(subprocess.check_call("where youtube-dl"),0)

    def test_ffprobe_installed(self):
        self.assertEqual(subprocess.check_call("where ffprobe"),0)

    def test_ffmpeg_installed(self):
        self.assertEqual(subprocess.check_call("where ffmpeg"),0)

    
    