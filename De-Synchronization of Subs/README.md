## Description

This is an algorthim to unsynchronise a subtitle file in a srt format.
It was used to generate the subtitles dataset of the project.

<br>
Outputs 4 sub.srt files. The first one has -3 sec delay in total. The other 3 have 
random delays at random timestamps, different for each subtile in each .srt file


## Install library

- pip install pysubs2
- pip install chardet

### Run script and replace file with filename (1 arg only)

```
$ python srt_creator.py file.srt
```

