import speech_recognition as sr
from moviepy.editor import *
import sys
import os
from pydub import AudioSegment

fileName = sys.argv[1]
fullAudio = "fullAudio.wav"
tempAudio = "tempAudio.wav"
div = 10000 #clip division in milliseconds
 

if fileName[len(fileName)-4] == ".":
    txtfile = fileName[:-4] + ".txt"
else:
    txtfile = fileName + ".txt"

video = VideoFileClip(fileName) # 2.

audio = video.audio # 3.
audio.write_audiofile(fullAudio) # 4.

audio = AudioSegment.from_wav(fullAudio)
clips = len(audio)//div

text = open(txtfile,"w+")


r = sr.Recognizer()
print("Number of clips: " + str(clips))
for x in range(clips+1):
    begValue = x*div
    if x == clips:
        clipAudio = audio[(begValue):]
    else:
        clipAudio = audio[(begValue):(x+1)*div-1]
    clipAudio.export(tempAudio,format="wav")

    minute = begValue//60000
    second = (begValue%60000)//1000

    with sr.AudioFile(tempAudio) as source: #ISSUE HERE, find way to not have to write a file every time
        audioOut = r.record(source)
    text.write(str(minute) + ":" + f"{second:02d}"+ "    " + r.recognize_google(audioOut) + "\n")
    print("Current clip: " + str(x),end="\r")

text.close

os.remove(fullAudio)
os.remove(tempAudio)
