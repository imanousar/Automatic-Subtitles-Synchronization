# SubSync Auth

## Installation
    
### Optional - Create a new virtual environment (Install Python 3.6 on Venv!)
    python3 -m venv ./
    source bin/activate
    
### Install SubSync Repo
    pip install subsync

### Install ffmpeg
    https://www.ffmpeg.org/download.html

## Execution

### If Python 3.6.xx is installed in your System (not Venv!)

1. Choose Model (GRU: Gated Recurrent Unit | BLSTM: Bidirectional Long Short-Term Memory)
2. 
4. Make sure that the .srt file has the same name as the movie file (ie. moviefile.mp4 -> moviefile.srt).
3. Open terminal and run: 
        subsync moviefile.mp4

### If Python 3.xx.xx is installed in your System (not Venv!) 

1. Choose Model (GRU: Gated Recurrent Unit | BLSTM: Bidirectional Long Short-Term Memory)
2. Copy the model directory (found inside the GRU or BLSTM directory) inside the movie's directory.
3. ( Activate the virtual environment )
4. Make sure that the .srt file has the same name as the movie file (ie. moviefile.mp4 -> moviefile.srt).
5. Open terminal and run: 
        python model\subsync moviefile.mp4

## Ackowlegdements
Repo: https://github.com/tympanix/subsync
