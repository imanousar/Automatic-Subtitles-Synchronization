import sys, os

if(len(sys.argv) != 3):
    sys.exit("Excepted 2 arguments only and not NULL!")

os.system('python subsync-master\\subsync\\bin\\subsync '+sys.argv[1])
os.system('python srt_evaluator.py '+sys.argv[1][:-4]+'.srt '+sys.argv[2])
