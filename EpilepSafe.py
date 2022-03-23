import os, os.path
import pytube
from pytube import YouTube
from cutter3 import *

border = '-'*105
title_border = '='*105
print(title_border)
print((' '*48)+'EpilepSafe'+(' '*47))
print(title_border)

#return_ratings(name of the video, sensitivity 1 to 3)
#return ratings for youtube video

sens = None
while sens not in [1, 2, 3]:
    try:
        sens = int(input('On a scale of 1 to 3, how sensitive are you to flashing imagery or changing colors? '))
        if sens>3 or sens<1:
            print(border)
            print(('!'*16)+'Invalid number, please make sure you pick a number between 1 and 3 please'+('!'*16))
            print(border)
    except: 
        print(border)
        print(('!'*24)+'Invalid character, please make sure you type in a number.'+('!'*24))
        print(border)
print(border)
    
decision = None
while decision!= 'Y' and decision!='P':
    decision = (input('For scanning a pre-downloaded video please type "P", or for scanning a Youtube video please type "Y": ')).upper()
    print(border)
    if decision!= 'Y' and decision!='P':
        print(('!'*36)+'Invalid input, please try again.'+('!'*37))
        print(border)
    

if decision == "Y":
    no_error = True
    while no_error:     
        url = input("Please copy the YouTube video's URL and paste it here: ")
        try:
            vsetup = pytube.YouTube(url)
            no_error = False
        except:
            print(border)
            print('Invalid input or connection to YouTube not established, please try again.')
            print(border)
        
    vid_name = (vsetup.title)    
    print(vid_name)
    video = vsetup.streams.first()
    video.download(filename='epilepsafe_scan')
    vid_name = 'epilepsafe_scan.mp4'
    
    print(border)
else:
    list_vid_types = ['webm' ,'.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.mov', '.flv', '.swf', 'vchd']
    condition = False
    while not condition:
        print("Please input the exact name of the video including it's format. (e.g.TestVidName.mp4 , TestVidName.avi)")
        vid_name = input('Name of video: ')        
        vid_type = vid_name[len(vid_name)-4 : len(vid_name)]
        
        if os.path.isfile(vid_name):
            if vid_type not in list_vid_types:
                print('Invalid file type. File type either not supported or is not a video, Sorry!')
                print(border)
            else:
                condition = True
        else:
            print("File not found. Please make sure you typed the name correctly and included the format.")
            print(border)
            

ratings = return_ratings(vid_name, sens) 
for x in ratings:
    print(x)

if decision == 'Y':
    os.remove('epilepsafe_scan.mp4')
