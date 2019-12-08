import os
import pysubs2  # Needs to be installed
import csv


def test():
    srts = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".srt")]
    accuracy = []
    ref = srts[0]
    srts = srts[1:]

    for i in range(len(srts)):
        acc = evaluate(ref, srts[i])
        accuracy.append(acc)

    with open("evaluation.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(accuracy)
        wr.writerow(srts)
    return


def evaluate(subtitles1, subtitles2):

    # Load the temporary subtitle files
    subs1 = pysubs2.load(subtitles1)
    subs2 = pysubs2.load(subtitles2)

    # File subs2 must have the first timestamp
    if subs2[0].start > subs1[0].start:
        subs1, subs2 = subs2, subs1

    # Initialize Parameters & Indices
    score = 0
    threshold = 1000  # msec
    maxReward = 1.5
    j = 0
    k = 0

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
        except IndexError:
            break

    # Calculate Accuray
    NormalizedScore = (score+(len(subs1)-1))/(2*(len(subs1)-1))

    # Accuray may become greater than 100% --> max{Accuracy}=99%
    if NormalizedScore>1:
        NormalizedScore = 1.00

    acc = NormalizedScore*100

    return acc


if __name__ == '__main__':
    test()
