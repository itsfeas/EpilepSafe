EpilipSafe version 1.0.0

THIS WAS CREATED USING PYTHON 3.8.6, SOME MODULES MIGHT NOT WORK WITH PREVIOUS OR MORE RECENT VERSIONS.

This script is designed to give warnings with timestaps for scenes in videos that have sudden color changes or flashing imagery.
------------------------------------------------------------------------------------------------------------------------------------------------------------
To be able to run this code, please install the following modules (Command Prompt guide to downloading them provided):
OpenCV: 
  pip install opencv-python

pytube:
  pip3 install pytube
------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to run this code, please open and run EpilepSafe.py. Also, please make sure all py files are in the same directory ***

------------------------------------------------------------------------------------------------------------------------------------------------------------
To get started you simply need to input how sensitive you are to these types of sudden changes. (must be an integer from 1 to 3, inclusive)


You then have an option of either choosing a video you already have downloaded or a youtube link. (If you choose youtube, then a video will be momentairly 
downloaded onto your system until the script is over)
Keep in mind that sometimes establishing a connection with youtube from python might fail and you might get an error message 'Invalid URL'. If that happens,
please just try again.


IMPORTANT NOTES: 
-If you decide to pick a video that you already have downloaded, please make sure it's in the same directory/location as this script.
-The maximum video length this program is one hour. The program may crash if a video longer than that is used.

Another mini note: both colorloop.mp4 and TestVid.mp4 were the videos that were used for testing, therefore we included them incase they were needed.
