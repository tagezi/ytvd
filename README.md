# YTVD is YouTube Video Downloader

It's not new library for downloading videos from YouTube. YTVD is script which 
uses *PyTube like API* for access to playlists and videos, and slightly expands 
the functionality. For example, you can create a list with playlists and
download all videos from it. Also, you can download only new videos from this
list, if you already have downloaded videos from these playlists. Videos are 
saved in a directory with the name of the playlist. 

## Install YTDV

Download code with follow command in terminal:
```commandline
git clone https://github.com/tagezi/ytvd.git
```
Go to `ytvd` directory:
```commandline
cd ytvd
```
Install requirements:
```commandline
pip install -r requirements.txt
```

## Setup configuration

Now, there is the file for setup of playlists. This file has name `playlist.txt`
and can be found in `config` directory. Add links on your playlists in this file
each on a new line. If you want to skip a few files, you can add link to that
videos in `slipvideos.txt`. It is located in the same directory.

When a video from a playlist is downloaded, a link to the video is added to
the file `slipvideos.txt`. So, next time when you run script, only new videos 
in playlist will download.

There is lines in main.py file:
```python
#: The file name with a list of playlists.
PLAYLIST_FILE = '../config/playlists.txt'
#: The file name with a list of files which needs skip.
VIDEO_SKIP_FILE = '../config/skipvideos.txt'
#: A path to the directory where files are saves.
VODEO_DIR = '../files/'
```
You can change, if you need.


