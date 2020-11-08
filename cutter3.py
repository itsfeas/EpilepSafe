import cv2
import datetime
from frame_gaze2 import *

def clip_cut(videoFile, sensitivity):
	count = 0
	cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	frameRate = round(cap.get(5)) #frame rate
	ranges = range(0,total_frames,frameRate)

	bounds = []
	second_ratings=[]
	i=0
	while i<len(ranges)-1:
		clip = [0]*frameRate
		bounds.append(range(ranges[i],ranges[i+1]))
		j=0
		for n in bounds[i]:
			cap.set(cv2.CAP_PROP_POS_FRAMES,n)
			trial, frame = cap.read()
			clip[j] = frame
			j+=1
		i+=1
		second_ratings.append(rate_risk(clip, 5,30))
		print(''.join(["Segment ", str(i), " out of ", str(len(ranges)), " processed!"]))
	cap.release()
	print("Video Processed!")
	print("Risk Analysis Start!")
	return(relative_risk(second_ratings, sensitivity))

def relative_risk(ratings, sensitivity):
	definite = [x>((4-sensitivity)*60000) for x in ratings]
	indefinite = [x>((4-sensitivity)*15000) for x in ratings]
	time = range(len(definite))
	risk = [[a,b,c] for (a, b, c) in zip(definite, indefinite, time)]
	#print(risk)
	
	return(intervals(risk,0), intervals(risk, 1))

def intervals(risk, probability):
	interval_list = []
	true_list = []
	
	for x in risk:
		if x[0]==True and probability==0:
			true_list.append('{0:04d}'.format(x[2]))
		elif x[0]==False and probability ==0:
			true_list.append('.')
		elif x[0]==False and x[1]== True and probability==1:
			true_list.append('{0:04d}'.format(x[2]))
		elif x[1]==False and probability ==1:
			true_list.append('.')

	true_list= ''.join(true_list)
	true_list = true_list.split('.')
	while('' in true_list) : 
	    true_list.remove('')

	for x in true_list:
		interval = []
		if len(x)==4:
			interval_list.append(convert_to_time(int(x)))
		else:
			n = len(x)
			x = list(x)
			x1 = ''.join(x[0:4])
			x2 = ''.join(x[n-3:n])
			interval.append(convert_to_time(int(x1)))
			interval.append(convert_to_time(int(x2)))
			interval_list.append(interval)
	return(interval_list)

def convert_to_time(time):
	return(str( datetime.timedelta(seconds=time)))

def return_ratings(videoFile, sensitivity):
	#ratings = clip_cut(videoFile, sensitivity)
	print("Video Processing Start!")
	ratings = clip_cut(videoFile, sensitivity)

	output = []
	if len(ratings[0])>0:
		output.append("There is a high risk of an epileptic trigger at the following points in the video: ")
		for interval in ratings[0]:
			if len(interval)==2:
				output.append(''.join([interval[0], " - ", interval[1]]))
			else:
				output.append(interval)

	if len(ratings[1])>0:
		output.append("There is a small risk of an epileptic trigger at the following points in the video: ")
		for interval in ratings[1]:
			if len(interval)==2:
				output.append(''.join([interval[0], " - ", interval[1]]))
			else:
				output.append(interval)

	if len(ratings[0])==0 and len(ratings[1])==0:
		output.append("There are no potential epileptic triggers detected")
	print("Risk Analysis Completed!")
	return(output)


if __name__ == '__main__':
	#clip_cut("TestVid.mp4", 3)

	return_ratings("TestVid.mp4", 3)