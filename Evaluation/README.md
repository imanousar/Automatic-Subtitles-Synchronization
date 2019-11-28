## Install libraries

pip install pysubs2
<br>
pip install chardet

### Run script and replace file1 and file2 by the sub's filenames (2 args)

python srt_evaluator.py file1.srt file2.srt

<br>
Report of un-synchronized subs.
Accuracy of synchronization between the two input subtitles.
Overall descriptive conclusion of synchronization results.

## Notes

Sub-Dialogs, that are not in common between both files, are
skipped without affecting accuracy.
