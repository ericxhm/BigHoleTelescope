import speech_recognition as sr
from moviepy.editor import *
import sys
import os
from pydub import AudioSegment

fileName = sys.argv[1]
fullAudio = "fullAudio.wav"
tempAudio = "tempAudio.wav"
div = 60000 #clip division in milliseconds

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

for x in range(clips+1):
    if x == clips:
        clipAudio = audio[(x*div):]
    else:
        clipAudio = audio[(x*div):(x+1)*div-1]
    clipAudio.export(tempAudio,format="wav")

    with sr.AudioFile(tempAudio) as source: #ISSUE HERE, find way to not have to write a file every time
        audioOut = r.record(source)
    text.write(r.recognize_google(audioOut))

text.close

os.remove(fullAudio)
os.remove(tempAudio)

# notes at 7/5
# need to shorten the divisions, it only seems to transcribe 10 seconds worth of audio at a time, we need a lot more. might be because of print limitation?
# look into putting it into a text file, that might be next step
# very slow, look into sphinx detection.
# find better way to save audio files