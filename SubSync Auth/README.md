# SubSync Auth

## Installation - Windows (Checked for Python 3.6)
    
1. Optional - Create a new virtual environment
    pip install virtualenv # if not installed
	virtualenv --python C:\\Path\\To\\Python\\python.exe venv # Create new  Venv ie. named "venv"
	source .\\venv\\Scripts\\activate # Activate V. Environment

2. Install SubSync Repo
    pip install subsync

3. Install ffmpeg
    https://www.ffmpeg.org/download.html

## Execution

1. Choose Model (BGRU: Bidirectional Gated Recurrent Unit | LSTM: Long Short-Term Memory)
2. Copy the BGRU/LSTM directory inside the movie's directory.
3. ( Activate the virtual environment )
4. Make sure that the .srt file has the same name as the movie file (ie. moviefile.mp4 -> moviefile.srt).
5. Open terminal and run: 
        python BGRU\subsync\bin\subsync moviefile.mp4 
	or 
		python LSTM\subsync\bin\subsync moviefile.mp4


## Training Process - Windows (Checked for Python 3.6)
   
Our training scripts are the `train_ann.py` files found in `BGRU/train` and `LSTM/train` directories.
Create a folder named `training` in `subsync/subsync/model` and copy the movies that you want to use for training the ann in it.
Make sure that the .srt files have the same name as the movie files (ie. moviefile.mp4 -> moviefile.srt)

While the venv is activated, run:
		python train_data.py
        python train_ann.py 
The trained model `ann.hdf5` will be created in the `subsync/subsync/model/out` folder. In order to use it you need to convert 
it to `.pb` format. To do this, so it can be used by the app, run  `python convert.py` while the `ann.hdf5` is still inside the
`subsync/subsync/model/out` folder.
The converted model `subsync.pb` will be created in the `subsync/subsync/model/out` folder.
Replace the existing `subsync.pb` file by the one you've just created.

## Installation - Linux

### Install ffmpeg
        
        sudo apt install ffmpeg
        

Using Python3.6.9


### SubSync App for Synchronization

Create the folder for the subsync app
        
        mkdir subsync_app
        cd subsync_app
Create and activate venv
        
        python3 -m venv ./
        source bin/activate
Install subsync
    
        pip install subsync

Using our models  
Our models are the `subsync.pb` files found inside `/BGRU/model` or `/LSTM/model`.
Copy the model that you want to use to `subsync_app/lib/python3.6/site-packages/subsync`
and replace the existing `subsync.pb` file.

Make sure that the .srt file has the same name as the movie file (ie. moviefile.mp4 -> moviefile.srt)

    cd subsync_app
    source bin/activate
    subsync {path_to_the_movie}
subsync replaces the given subtitle with the synced one

### Subsync - Artificial Neural Network Train

clone the repo https://github.com/tympanix/subsync.git and install the packages

    git clone https://github.com/tympanix/subsync.git
    cd subsync
    python3 -m venv ./
    pip install -r requirements.txt
   
Our training scripts are the `train_ann.py` in `BGRU/train` and `LSTM/train`
Copy the one you want in `subsync/subsync/model`
Create the folder `training` in `subsync/subsync/model` and copy the movies that you want to use for training the nn in it.
Make sure that the .srt files have the same name as the movie files (ie. moviefile.mp4 -> moviefile.srt)

While the venv is activated, run:
		python train_data.py 
        python train_ann.py 
The trained model `ann.hdf5` will be created in the `subsync/subsync/model/out` folder. In order to use it you need to convert 
it to `.pb` format. To do this, so it can be used by the app, run  `python convert.py` while the `ann.hdf5` is still inside the
`subsync/subsync/model/out` folder.
The converted model `subsync.pb` will be created in the `subsync/subsync/model/out` folder


## Ackowlegdements
Repo: https://github.com/tympanix/subsync
