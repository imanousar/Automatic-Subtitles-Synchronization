## Instructions ##

# 1. Install python 3.6 .
# 2. Run: pip install susbsync 
#	 (Just to install the necessary libs)
# 3. Download subsync-master repo and place 
#	 it in the movie's directory.
#	 Link: https://github.com/tympanix/subsync
# 4. Place this script in the movie's directory 
#    and make sure that the .srt file has the 
#    same name as the movie file.
# 5. Place srt_evaluator.py and the optimum subtitle 
#	 in the movie's directory.
# 6. Run: python tympanix_subsync.py <filename.mp4> <optimum_sub.srt>

import sys, os

if(len(sys.argv) != 3):
    sys.exit("Excepted 2 arguments only and not NULL!")

os.system('python subsync-master\\subsync\\bin\\subsync '+sys.argv[1])
os.system('python srt_evaluator.py '+sys.argv[1][:-4]+'.srt '+sys.argv[2])
