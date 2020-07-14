import cv2
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import time

SLIDEENDS = []

# RUN = 1

# function to check if new slide should be saved
# x = new slide, y = end of prev slide
# returns true if slide is not a repeat, false otherwise
def new_checks(x,y):
    if (len(SLIDEENDS) == 0):
        SLIDEENDS.append(y)
        return True
    else:
        diffs = np.subtract(SLIDEENDS,x)
        l = diffs.shape[0]
        norm = np.zeros(l)
        
        for i in range(l):
            norm[i] = np.linalg.norm(diffs[i,:])
        # print(norm)
        SLIDEENDS.append(y)
        if(np.amin(norm) <= 10000):
            return False
        else:
            
            return True
    # print(RUN)
    # RUN += 1

        

def main():
    ### video capture to get fps, # of frames, and first frame ###
    vidcap = cv2.VideoCapture('zoom_0.mp4')
    success = True

    # interval = 5610 # just to take screenshot at 6:14 mark of video

    frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))   # number of frames
    fps = vidcap.get(cv2.CAP_PROP_FPS)                   # frame rate

    numsec = frames//fps  # duration of video (sec)

    rval, frame = vidcap.read()  # gets first frame
    first_frame = frame
    vidcap.release()

    manual = 12*60 + 29
    print(numsec, 'seconds, ', manual,'seconds, ',frames, 'frames, ', fps, 'fps')

    #plt.imshow(first_frame)

    ## // New worse converting image into grayscale image (np array) ###
    # gray_ff = cv2.cvtColor(first_frame,cv2.COLOR_RGB2GRAY)
    # gff = np.array(gray_ff)
    

    ### OLD better converting image into grayscale image (np array) ###
    ff = np.array(first_frame)
    d = np.array([0.2989, 0.5870, 0.1140])
    gff = np.dot(ff, d) #grayscale version of first frame

    ##// plotting in jupyter notebook ###
    # fig, (ax1, ax2) = plt.subplots(2, 1)
    # ax1.imshow(ff)
    # ax2.imshow(gff,cmap = plt.get_cmap("gray"))


    scr_shot = gff
    interval = 5*fps  # k*fps = take screenshot every k seconds

    ### video capture to go through whole video
    vidcap = cv2.VideoCapture('zoom_0.mp4')
    success = True 
    # start = 0   # variable to check if this is the first frame
    timestamps = [] # list to add time stamps and norm values to
    slides = [] # list to add predicted slide change times to
    f = 0       # current frame value
    prev = 0    # previous frame value

    while success:
        success, image = vidcap.read()
        if (f%interval == 0):
            ## // New Worse convert to gray ###
            # gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
            # gnew = np.array(gray) # grayscale numpy version of image
            

            ### old better convert to gray ###
            new = np.array(image)
            gnew = np.dot(new, d) # grayscale numpy version of image 

            diff = np.subtract(scr_shot, gnew) # difference between two images
            norm = np.linalg.norm(diff) # norm of difference
            timestamps.append(((prev//fps, f//fps), norm))

            if (norm >= 10000):
                # start_time = time.time()
                check = (new_checks(gnew,scr_shot))
                # print("--- %s seconds ---" % (time.time() - start_time))
                if(check == True):
                    start_time_min = int((prev//fps)//60)
                    start_time_sec = int((prev//fps)-(60*start_time_min))
                    end_time_min = int((f//fps)//60)
                    end_time_sec = int((f//fps)-(60*end_time_min))
                    mmss = f"{start_time_min}:{start_time_sec} - {end_time_min}:{end_time_sec}" 
                    slides.append(mmss)

            prev = f
            
        f += 1 
        scr_shot = gnew
        
        
    ### create txt file of frames and norms ###    
    with open("norms_2.2.txt", "w") as output:
        for listitem in timestamps:
            output.write('%s\n' % str(listitem))

    print(slides)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
