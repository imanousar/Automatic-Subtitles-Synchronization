import sys
import pysubs2

# check if the input data is exactly 2 subtitle files
if(len(sys.argv) != 3):
    sys.exit("Expected 2 arguments only and not NULL!")
elif(True):
    # check if they are .srt files
    subtitles1 = sys.argv[1]
    subtitles2 = sys.argv[2]
    if((not subtitles1.endswith(".srt")) or (not subtitles2.endswith(".srt"))):
        sys.exit("Expected .srt files!")

try:
    subs1 = pysubs2.load(subtitles1)
except Exception as ex_1:
    try:
        subs1 = pysubs2.load(subtitles1, encoding="iso8859_7")
    except Exception as ex_2:
            print("Exceptions"+ex_1+ex_2)
            sys.exit("Use utf-8 or iso8859_7 encoding for .srt file 1")

try:
    subs2 = pysubs2.load(subtitles2)
except Exception as ex_1:
    try:
        subs2 = pysubs2.load(subtitles2, encoding="iso8859_7")
    except Exception as ex_2:
            print("Exceptions"+ex_1+ex_2)
            sys.exit("Use utf-8 or iso8859_7 encoding for .srt file 2")

if len(subs2) > len(subs1):
    subs1, subs2 = subs2, subs1

score = 0

threshold = 1500  # msec

j = 0
k = 0

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

        while subs2[k].end < subs1[i].end - threshold:
            k = k + 1

        if subs2[k].end > subs1[i].end + threshold:
            startFlag = False
            k = k - 1

        if startFlag is True and endFlag is True:
            score = score + 1
        else:
            score = score - 1
    except IndexError:
        print("Subs out of index")
        break

print("Total Score: ", score)

NormalizedScore = (score+(len(subs1)-1))/(2*(len(subs1)-1))
print("Accuracy: ", NormalizedScore*100, "%")
