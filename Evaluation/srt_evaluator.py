import sys
import pysubs2 # Needs to be installed
import chardet # Needs to be installed
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



# Check number of arguments
if(len(sys.argv) != 3):
    sys.exit("Expected 2 arguments only and not NULL!")
elif(True):
    # Check file extentions (.srt files)
    subtitles1 = sys.argv[1]
    subtitles2 = sys.argv[2]
    if((not subtitles1.endswith(".srt")) or (not subtitles2.endswith(".srt"))):
        sys.exit("Expected .srt files!")

# Create temporary srt files with UTF-8 Encoding
encodeToUTF8(subtitles1,"sub1.srt")
encodeToUTF8(subtitles2,"sub2.srt")
subtitles1 = "sub1.srt"
subtitles2 = "sub2.srt"

# Load the temporary subtitle files
subs1 = pysubs2.load(subtitles1)
subs2 = pysubs2.load(subtitles2)

# File subs2 must have the first timestamp
if subs2[0].start  > subs1[0].start:
    subs1, subs2 = subs2, subs1

# Initialize Parameters & Indices
score = 0
threshold = 1000  # msec
maxReward = 1.5
j = 0
k = 0

print("\nReporting problematic subs\n")

# Evalutation Process
for i in range(len(subs1)-1):
    d = 0
    startFlag = True
    endFlag = True

    try:
        while subs2[j].start < subs1[i].start - threshold:
            j = j + 1
		
        if subs2[j].start > subs1[i].start + threshold:
            startFlag = False
            j = j - 1
        else:
            d = d + abs(subs2[j].start - subs1[i].start)/2
    
        while subs2[k].end < subs1[i].end - threshold:
            k = k + 1
    
        if subs2[k].end > subs1[i].end + threshold:
            startFlag = False
            k = k - 1
        else:
            d = d + abs(subs2[k].end - subs1[i].end)/2
    
        if startFlag == True and endFlag == True:
            score = score +  maxReward*(1-d/threshold) # + 1
        else:
            score = score - 1
            print("Check sub",i+1,"( minute:", int(subs1[i].start/60000),")",":",subs1[i].text )
    except IndexError:
        print("Subs out of Index. Last Index: ",i+1)
        break

# Calculate Accuray
NormalizedScore = (score+(len(subs1)-1))/(2*(len(subs1)-1))

# Accuray may become greater than 100% --> max{Accuracy}=99%
if NormalizedScore>1:
    NormalizedScore = 0.99

print("\nAccuracy: ", NormalizedScore*100, "%")

# Draw a Conclusion
if NormalizedScore > 0.9:
    print("Conclusion: Perfect Synchronization")
elif NormalizedScore > 0.6:
    print("Conclusion: Good Synchronization")
elif NormalizedScore > 0.4:
    print("Conclusion: Not Good Synchronization")
else:
    print("Conclusion: Not Synchronized")

# Delete the temporary subtitle files
os.remove("sub1.srt")
os.remove("sub2.srt")
