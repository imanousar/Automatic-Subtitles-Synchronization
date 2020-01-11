# Subsync by tympanix

## Installation - Windows (Checked for Python 3.6)
    
### 1. Optional - Create a new virtual environment
Install virtualenv if not installed

	pip install virtualenv 
	
Create new  Venv ie. named "venv"

	virtualenv --python C:\\Path\\To\\Python\\python.exe venv
	
Activate V. Environment

	source .\\venv\\Scripts\\activate

### 2. Install SubSync Repo
    
	pip install subsync

### 3. Install ffmpeg
	https://www.ffmpeg.org/download.html

## Execution - Windows (Checked for Python 3.6)

1. ( Activate the virtual environment )
2. Make sure that the .srt file has the same name as the movie file (ie. moviefile.mp4 -> moviefile.srt).
3. Open terminal and run:

		subsync moviefile.mp4 

## Ackowlegdements
Repo: https://github.com/tympanix/subsync
