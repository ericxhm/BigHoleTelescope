import cv2
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np

### video capture to get fps, # of frames, and first frame ###
vidcap = cv2.VideoCapture('Lec_examp.mp4')
success = True

# interval = 5610 # just to take screenshot at 6:14 mark of video

frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))   # number of frames
fps = vidcap.get(cv2.CAP_PROP_FPS)                   # frame rate

numsec = frames//fps                                 # duration of video (sec)


rval, frame = vidcap.read()                          # gets first frame
first_frame = frame
vidcap.release()


manual = 12*60 + 29
print(numsec, 'seconds, ', manual,'seconds, ',frames, 'frames, ', fps, 'fps')

plt.imshow(first_frame)

scr_shot = np.zeros((first_frame.shape))             # creates array to save previous image in
interval = 15                                        # take screenshot every second

### video capture to go through whole video
vidcap = cv2.VideoCapture('Lec_examp.mp4')
success = True
start = 0                                            # variable to check if this is the first frame
slides = []                                          # list to add time stamps and norm values to
f = 0                                                # current frame value
prev = 0                                             # previous frame value

while success:
    success,image = vidcap.read()
    if (f%interval == 0):
        new = np.array(image)
        diff = np.subtract(scr_shot,new)
        norm = np.linalg.norm(diff)
        if(start == 0):
            start += 1
        else:
            slides.append(((prev//fps,f//fps),norm))
            prev = f
        
    f +=1
    scr_shot = image
    
    
### create txt file of frames and norms ###    
with open("norms.txt", "w") as output:
    for listitem in slides:
        output.write('%s\n' % str(listitem))
