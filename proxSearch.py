import os
import sys
#lowercase everything
arg1 = sys.argv[2]
arg2 = sys.argv[3]
arg1Arr = []
arg2Arr = []
proxArr = []



def timeStamp(str): #Finding the timestamp of video
    ind = str.find(":")
    return str[0:ind+3]

# make a check for both words in 1
def checkProx(word1, word2, arr1, arr2, proxarr, line):
    arr1.append(timeStamp(line))
    count = 0
    while(count <= 2):
        linefunc = transcript.readline()
        if word1 in linefunc and word2 in linefunc:
            proxarr.append(timeStamp(line))
            line = linefunc
            arr1, arr2, proxarr = checkSameLine(word1, word2, arr1, arr2, proxarr, line)
            break
        elif word1 in linefunc:
            count = 0
            arr1.append(timeStamp(linefunc))
            line = linefunc
        elif word2 in linefunc:
            proxarr.append(timeStamp(line))
            line = linefunc
            arr2, arr1, proxarr = checkProx(word2, word1, arr2, arr1, proxarr, line)
            break
        else:
            count += 1
    return arr1,arr2,proxarr    

def checkSameLine(word1, word2, arr1, arr2, proxarr, line):
    arr1.append(timeStamp(line))
    arr2.append(timeStamp(line))
    proxarr.append(timeStamp(line))
    count = 0
    while(count <= 2):
        linefunc = transcript.readline()
        if word1 in linefunc and word2 in linefunc:
            proxarr.append(timeStamp(line))
            line = linefunc
            arr1, arr2, proxarr = checkSameLine(word1, word2, arr1, arr2, proxarr, line)
            break
        elif word1 in linefunc:
            proxarr.append(timeStamp(line))
            line = linefunc
            arr1, arr2, proxarr = checkProx(word1, word2, arr1, arr2, proxarr, line)
            break
        elif word2 in linefunc:
            proxarr.append(timeStamp(line))
            line = linefunc
            arr2, arr1, proxarr = checkProx(word2, word1, arr2, arr1, proxarr, line)
            break   
        else:
            count += 1
    return arr1,arr2,proxarr



transcript = open(sys.argv[1],"r")

# two words in the same line
line = transcript.readline()
while(line):
    if arg1 in line:
        arg1Arr, arg2Arr, proxArr = checkProx(arg1,arg2,arg1Arr,arg2Arr,proxArr, line)
    elif arg2 in line:
        arg2Arr, arg1Arr, proxArr = checkProx(arg2,arg1,arg2Arr,arg1Arr,proxArr, line)
    
    line = transcript.readline()

print(arg1Arr)
print(arg2Arr)
print(proxArr)


transcript.close()