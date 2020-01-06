## Description

This is a script to evaluate the accuracy of a subtitle in srt format. It 
requires a correct-synchronised subtitle (Ground Truth) for the evaluation.

## Install libraries

- `pip install pysubs2`
- `pip install chardet`

## Run script and replace file1 and file2 by the subs's filenames (2 args)

```bash
python srt_evaluator.py file1.srt file2.srt
```

## Output

- Report of un-synchronized subs.
- Accuracy of synchronization between the two input subtitles.
- Overall descriptive conclusion of synchronization results.

## Notes

Sub-Dialogs, that are not in common between both files, are
skipped without affecting accuracy.
