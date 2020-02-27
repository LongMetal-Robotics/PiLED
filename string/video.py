import time
from PIL import Image

def loopVideo(string, folder, filename, frames, fps, callingString):
    while not callingMatrix.threadStop:
       playVideo(string, folder, filename, frames, fps, callingString)

def playVideo(string, folder, filename, frames, fps, callingString):
    for frame in range(frames):
        if not callingString.threadStop:
            displayImage(folder + "/" + filename, frame, string)
            time.sleep(1.0/fps)