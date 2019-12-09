# PyAMC

*Python >= 3.5*


## Installation

    git clone https://github.com/Koenkk/PyAMC.git
    cd PyAMC
    python3 -m venv ./
    source bin/activate
    pip install -r requirements


-> Outside of the venv

    sudo apt install ffmpeg


## Execution

1. copy the movie and the subtitle to the same folder  
2. activate the venv
3. run: (substitute \<folder_path\> with the movie folder and \<language\> with the ISO 639-1 code of the language
    
        python pyamc.py auto_sync_subtitles --path <folder_path> --language <language>
