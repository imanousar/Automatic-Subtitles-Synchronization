# Subsync by Smacke

The repo can be found [here](https://github.com/smacke/subsync)

## Installation

Windows 10 - Installlation (The same steps apply for Linux).

- Install ffmpeg
- Add ffmpeg to the path 

> Instructions can be found [here](https://www.youtube.com/watch?v=qjtmgCb8NcE&t=363s)

<br>
Install subsync
- pip install git+https://github.com/smacke/subsync@STABLE

<br>
If it fails with error:
> error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"
<br> 
Try the following
- Download Visual Studio 2019 Community from [here](https://visualstudio.microsoft.com/downloads/)
- Install C++ Desktopt tools

## Using the code

```
subsync video.mp4 -i unsynchronized.srt > synchronized.srt
```
or

```
subsync video.mp4 -i unsynchronized.srt -o synchronized.srt
``` 
or
```
subsync reference.srt -i unsynchronized.srt -o synchronized.srt

```

We don't own this work. Credits to this [repo](https://github.com/smacke/subsync).