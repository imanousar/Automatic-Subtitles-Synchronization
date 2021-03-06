import sys
import shutil
import pysubs2
import random
import chardet
import codecs
import os


def encodeToUTF8(oldFile, newFile):

    # Initial Encoding - Detection
    rawdata = open(oldFile, 'rb').read()
    result = chardet.detect(rawdata)
    old_enc = result['encoding']
    # Converting to UTF-8
    with codecs.open(oldFile, 'r', encoding=old_enc) as file:
        lines = file.read()
    with codecs.open(newFile, 'w', encoding='utf8') as file:
        file.write(lines)


# check if the input data is only a subtitle file
if(len(sys.argv) != 2):
    sys.exit("Excepted 1 argument only and not NULL!")
elif(True):
    # check if its an .srt file
    subtitle = sys.argv[1]
    if(not subtitle.endswith(".srt")):
        sys.exit("Expected .srt file!")

# shift the subtitles of the 3 seconds later - Window shifting
subtitle = shutil.copyfile(subtitle, subtitle.split('.')[0]+"_shift_3sec.srt")


encodeToUTF8(subtitle, "sub1.srt")  # convert srt file in utf-8 encoding
subs = pysubs2.load(subtitle)


for line in subs:
    line.start -= 3000
    line.end -= 3000
subs.save(subtitle)

# create a copy of the original file
for i in range(1, 4):
    shift_rand = shutil.copyfile(subtitle, subtitle.split('_')[0]+"_shift%d_rand.srt" % i)

    limit = 0
    offset = 0
    try:
        subs = pysubs2.load(shift_rand)
    except Exception as ex_1:
        try:
            subs = pysubs2.load(shift_rand, encoding="iso8859_7")
        except Exception as ex_2:
                print("Exceptions"+ex_1+ex_2)
                sys.exit("Use utf-8 or iso8859_7 encoding")

    for line in subs:
        offset = int((line.start - limit) * random.uniform(0.3, 0.7)) + 1000
        if(offset > 6000):
            offset = int((line.start - limit) * random.uniform(0.01, 0.2)) + 1000
        elif(offset < 1250):
            offset = int((line.start - limit) * random.uniform(0.8, 1)) + 1000
        line.start -= offset
        line.end -= offset
        limit = line.end

    subs.save(shift_rand)

os.remove("sub1.srt")
