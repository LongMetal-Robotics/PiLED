# PiLED
 
## NT API Documentation
When `main.py` is running, it will read 3 NetworkTable keys for commands. (They are in `PiLED/matrix` and `PiLED/string` respectively)
- `type` is a string that determines the type of media to display. The acceptable values are `image`, and `video`
- `file` is a string that determines the file to read. For `image` mode, it is the name of the file to display. In `video` mode, it is the name of the folder the images are stored in.
- `trigger` is a number that, when changed, will trigger an update of the screen, determined by the above values.
When it receives a command, it will write a boolean to `result`. True if it worked, false if it didn't.

## Video Format
`video` mode expects the name of the folder to play. In the folder should be a file called `video`. It needs four lines with configuration information:
```
basename {basename}
fileext {ext}
frames {frames}
fps {fps}
```
[Example](matrix/MatrixWarmup/video)
- `{basename}` is replaced with the base name of the file (if the images are imageXXXX.png, `basename` will be `image`).  
- `{ext}` is the file extension. If the images are `.png` format, `{ext}` would be `png`.  
- `{frames}` is the number of frames in the animation.  
- `{fps}` is the framerate to run the animation at.  
  
**Of Note**: The code expects the images to be formatted `{basename}XXXX.{ext}`. Therefore there is a maximum of 10,000 frames per video (5:33.0 at 30fps) which should be more than enough.