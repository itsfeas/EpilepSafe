import cv2
		
def frame_format(frame):
	frame = cv2.resize(frame, (50,50), interpolation = cv2.INTER_AREA)
	return frame_convert(frame)

def frame_convert(frame):
	gaze = []
	for x in range(50):
		column = []
		for y in range(50):
			column.append(frame[x,y])
		gaze.append(column)
	return(gaze)

def rate_at_nfreq(clip, frequency):
	n_frames = len(clip)
	rating = 0
	frame_indexes = range(0, n_frames, frequency)

	i=0
	while i<len(frame_indexes)-1:
		rating+=compare_frame(clip[i], clip[i+1])
		i+=1
	return(rating)


def rate_risk(clip, lbound_freq, ubound_freq):
	rating=0
	if ubound_freq>len(clip):
		ubound_freq=len(clip)

	frequencies = range(lbound_freq, ubound_freq+1, 1)
	for frequency in frequencies:
		rating+=rate_at_nfreq(clip,frequency)
	return(rating)


def compare_frame(gaze1, gaze2):
	rating = 0
	variance = 150
	compared_frame = []
	for x in range(50):
		diff_column = [subtract_pixels(a, b) for (a, b) in zip(gaze1[x], gaze2[x])]
		diff_column = [a**2>variance**2 for a in diff_column]
		rating+=sum(diff_column)
		compared_frame.append(diff_column)
	return(rating)

def subtract_pixels(p1, p2):
	return(abs(int(p2[0])-int(p1[0]))+abs(int(p2[2])-int(p1[2])))


if __name__ == '__main__':
	a = frame_format(cv2.imread('frame380.jpg', cv2.IMREAD_UNCHANGED))
	b = frame_format(cv2.imread('frame387.jpg', cv2.IMREAD_UNCHANGED))
	print(compare_frame(a, b))

"""
	capframes = cv2.VideoCapture('TestVid.mp4')
	ret, frames = capframes.read()
	print(frames[1])
"""