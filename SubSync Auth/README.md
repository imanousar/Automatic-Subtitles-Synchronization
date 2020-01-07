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
2. Copy subsync.pb file (found inside the chosen model directory) and paste it into:
    %USERPROFILE%\AppData\Local\Programs\Python\Python36\Lib\site-packages\subsync
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


## FOR LINUX

install ffmpeg
        
        sudo apt install ffmpeg
        

Using Python3.6.9


### subsync app for synchronizartion

Create the folder for the subsync app
        
        mkdir subsync_app
        cd subsync_app
Create and activate venv
        
        python3 -m venv ./
        source bin/activate
Install subsync
    
        pip install subsync

Using our models  
Our models are the `subsync.pb` file inside `/GRU/model` and `/BLSTM/model`.
Copy the model you want to use to `subsync_app/lib/python3.6/site-packages/subsync`
and replace the existing `subsync.pb`

In order to run the app to sync subtitles the movie must be in the same folder and have the same name
e.g.  my_movie.mp4 , my_movie.srt

    cd subsync_app
    source bin/activate
    subsync {path_to_the_movie}
subsync replaces the given subtitle with the synced one

### subsync neural net train

clone the repo https://github.com/tympanix/subsync.git and install the packages

    git clone https://github.com/tympanix/subsync.git
    cd subsync
    python3 -m venv ./
    pip install -r requirements.txt
   
Out training files are the `train_ann.py` in `GRU/train` and `BLSTM/train`
Copy the one you want in `subsync/subsync/model`
Create the folder `training` in `subsync/subsync/model` and copy the movies you want to use for training the nn in it.
The movies and the corresponding subtitles should have the same name e.g. movie1.mp4, movie1.srt etc

While still inside the venv run
    
        python train_ann.py 
The trained model `ann.hdf5` will be in the `subsync/subsync/model/out` folder
To convert it in `.pb` format so it can be used by the app run  `python convert.py` while the `ann.hdf5` is still inside the
`subsync/subsync/model/out` folder
The converted model `subsync.pb` will be in the `subsync/subsync/model/out` folder


## Ackowlegdements
Repo: https://github.com/tympanix/subsync
