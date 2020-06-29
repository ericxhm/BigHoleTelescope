import cv2
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np

def main():
    ### video capture to get fps, # of frames, and first frame ###
    vidcap = cv2.VideoCapture('Lec_examp.mp4')
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

    plt.imshow(first_frame)

    ### converting image into grayscale image (np array) ###
    ff = np.array(first_frame)
    d = np.array([0.2989, 0.5870, 0.1140])

    gff = np.dot(ff, d) #grayscale version of first frame

    ### plotting in jupyter notebook ###
    # fig, (ax1, ax2) = plt.subplots(2, 1)
    # ax1.imshow(ff)
    # ax2.imshow(gff,cmap = plt.get_cmap("gray"))

    scr_shot = gff
    interval = 15                              # take screenshot every second

    ### video capture to go through whole video
    vidcap = cv2.VideoCapture('Lec_examp.mp4')
    success = True 
    start = 0   # variable to check if this is the first frame
    slides = [] # list to add time stamps and norm values to
    f = 0       # current frame value
    prev = 0    # previous frame value

    while success:
        success, image = vidcap.read()
        if (f%interval == 0):
            new = np.array(image)
            gnew = np.dot(new, d)
            diff = np.subtract(scr_shot, gnew)
            norm = np.linalg.norm(diff)
            slides.append(((prev//fps, f//fps), norm))
            prev = f
            
        f += 1 
        scr_shot = gnew
        
        
    ### create txt file of frames and norms ###    
    with open("norms_1.2.txt", "w") as output:
        for listitem in slides:
            output.write('%s\n' % str(listitem))


main()
