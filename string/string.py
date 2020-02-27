from rgbstring import RGBString, RGBStringOptions
from video import playVideo, loopVideo
from frame import displayImage

import logging
import threading
import re

import board
import neopixel

class String:
    currentThread = None
    threadStop = False

    def __init__(self):
        print("String initialized")
        self.pixels = neopixel.NeoPixel(board.D25, 32)
    
    def stopThread(self):
        if not self.currentThread is None:
            print("Stopping running thread...")
            self.threadStop = True
            self.currentThread.join()
            self.threadStop = False
            print("Stopped thread")
    
    def display(self, mediaType, file):
        result = False
        if mediaType == "image":
            # Display image
            try:
                self.stopThread()
                print("Displaying image")
                displayImage(file, 0, self.string)
                result = True
            except Exception, e:
                print("Could not display image: " + str(e))
                logging.error('Could not display image file %s. Exception: ' + str(e), file)
        elif mediaType == "video" or mediaType == "video-one":
            # Create a new thread to display
            # the video (currentThread) and run it
            try:
                print("Displaying video")
                video = open("./" + file + "/video", "r")
                videoInfo = video.read()
                print("Video info:")
                print(videoInfo)
                basename = re.search("basename \\w*", videoInfo).group()[9:] # Regex search, then get everything past `basname `
                fileext = re.search("fileext \\w*", videoInfo).group()[8:]
                frames = int(re.search("frames \\d*", videoInfo).group()[7:])
                fps = int(re.search("fps \\d*", videoInfo).group()[4:])
                print()
                print("basename: " + basename)
                print("fileext: " + fileext)
                print("frames: " + str(frames))
                print("fps: " + str(fps))
                self.stopThread()
                if mediaType == "video":
                    print("Video loops. Creating thread...")
                    self.currentThread = threading.Thread(target=loopVideo, args=(self.string, file, basename + "." + fileext, frames, fps, self))
                else:
                    print("Video is one-off. Creating thread...")
                    self.currentThread = threading.Thread(target=playVideo, args=(self.string, file, basename + "." + fileext, frames, fps, self))
                print("Thread created. Starting thread...")
                self.currentThread.start()
                print("Thread started")
                result = True
            except Exception, e:
                print("Could not display video: " + str(e))
                logging.error('Could not display the video. Exception: ' + str(e))
        else:
            # Blank the display
            print("Media type " + mediaType + " not recognized. Blanking screen...")
            self.stopThread()
            self.string.fill(0, 0, 0)
            result = True
            print("Screen blanked")
        return result
