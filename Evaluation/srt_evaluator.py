import sys
import pysubs2

# check if the input data is exactly 2 subtitle files
if(len(sys.argv) != 3):
    sys.exit("Excepted 2 arguments only and not NULL!")
elif(True):
    # check if they are .srt files
    subtitles1 = sys.argv[1]
    subtitles2 = sys.argv[2]
    if((not subtitles1.endswith(".srt")) or (not subtitles2.endswith(".srt"))):
        sys.exit("Expected .srt files!")

subs1 = pysubs2.load(subtitles1)
subs2 = pysubs2.load(subtitles2)


if len(subs2) > len(subs1):
    subs1, subs2 = subs2, subs1

score = 0

threshold = 500  # msec

j = 0
k = 0

for i in range(len(subs1)-1):

    startFlag = True
    endFlag = True

    # if srt files have different number of subs
    if j >= len(subs2)-1 or k >= len(subs2)-1:
        score = score - (len(subs1)-len(subs2))
        break

while subs2[j].start < subs1[i].start - threshold:
        j = j + 1

    if subs2[j].start > subs1[i].start + threshold:
        startFlag = False
        j = j - 1

    while subs2[k].end < subs1[i].end - threshold:
        k = k + 1

    if subs2[k].end > subs1[i].end + threshold:
        startFlag = False
        k = k - 1

    if startFlag == True and endFlag == True:
        score = score + 1
    else:
        score = score - 1

print("Total Score: " , score)

NormalizedScore =  ( score+(len(subs1)-1) )/( 2*(len(subs1)-1) )
print("Accuracy: " , NormalizedScore*100 , "%")
