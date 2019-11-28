import sys
import pysubs2
import chardet    
import codecs
import os

def encodeToUTF8(oldFile,newFile):

    # Initial Encoding - Detection
    rawdata = open(oldFile, 'rb').read()
    result = chardet.detect(rawdata)
    old_enc = result['encoding']
    
    # Converting to UTF-8
    with codecs.open(oldFile, 'r', encoding = old_enc) as file:
      lines = file.read()
    with codecs.open(newFile, 'w', encoding = 'utf8') as file:
      file.write(lines)



# check if the input data is exactly 2 subtitle files
if(len(sys.argv) != 3):
    sys.exit("Expected 2 arguments only and not NULL!")
elif(True):
    # check if they are .srt files
    subtitles1 = sys.argv[1]
    subtitles2 = sys.argv[2]
    if((not subtitles1.endswith(".srt")) or (not subtitles2.endswith(".srt"))):
        sys.exit("Expected .srt files!")

encodeToUTF8(subtitles1,"sub1.srt")
encodeToUTF8(subtitles2,"sub2.srt")
subtitles1 = "sub1.srt"
subtitles2 = "sub2.srt"

subs1 = pysubs2.load(subtitles1)
subs2 = pysubs2.load(subtitles2)


if subs2[0].start  > subs1[0].start:
    subs1, subs2 = subs2, subs1

score = 0

threshold = 1500  # msec

j = 0
k = 0
maxReward = 1.5

print("\nUnsynchronized Subs\n")

for i in range(len(subs1)-1):

    startFlag = True
    endFlag = True

    # if srt files have different number of subs
    if j >= len(subs2)-1 or k >= len(subs2)-1:
        score = score - (len(subs1)-len(subs2))
        break
    try:
        while subs2[j].start < subs1[i].start - threshold:
            j = j + 1
    
        if subs2[j].start > subs1[i].start + threshold:
            startFlag = False
            j = j - 1
        else:
            d = abs(subs2[j].start - subs1[i].start)/2
    
        while subs2[k].end < subs1[i].end - threshold:
            k = k + 1
    
        if subs2[k].end > subs1[i].end + threshold:
            startFlag = False
            k = k - 1
        else:
            d = d + abs(subs2[k].end - subs1[i].end)/2
    
        if startFlag == True and endFlag == True:
            score = score + 1 # maxReward*(1-d/threshold) # + 1
        else:
            score = score - 1
            print("Check sub",i,"( minute:", int(subs1[i].start/60000),")",":",subs1[i].text )
    except IndexError:
        print("Subs out of index ",i)
        break

NormalizedScore = (score+(len(subs1)-1))/(2*(len(subs1)-1))

if NormalizedScore>1:
    NormalizedScore = 1

print("\nAccuracy: ", NormalizedScore*100, "%")

if NormalizedScore > 0.9:
    print("Perfect Synchronization")
elif NormalizedScore > 0.6:
    print("Good Synchronization")
elif NormalizedScore > 0.4:
    print("Not Good Synchronization")
else:
    print("Not Synchronized")

os.remove("sub1.srt")
os.remove("sub2.srt")
