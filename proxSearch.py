import os
import sys


arg1Count = 0
arg2Count = 0
prox = 0


def timeStamp(str): #Finding the timestamp of video
    ind = str.find(":")
    return str[0:ind+3]

def checkProx(word1, word2, arr1, arr2, prox, proxarr):
    arr1[len(arr1)] = timeStamp(line)
    count = 0
    while(count <= 2):
        linefunc = transcript.readline()
        if word1 in linefunc:
            count = 0
            arr1[len(arr1)] = timeStamp(linefunc)
            line = linefunc
        elif word2 in linefunc:
            arr2[len(arr2)] = timeStamp(linefunc)
            break
        else:
            count += 1
    





transcript = open(sys.argv[1],"r")

line = transcript.readline()
while(not line):
    if sys.argv[2] in line:


transcript.close()