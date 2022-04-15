# YTVD’s documentation

## User documentation

### YTVD is YouTube Video Downloader

It’s not new library for downloading videos from YouTube. YTVD is script which
uses *PyTube like API* for access to playlists and videos, and slightly expands
the functionality. For example, you can create a list with playlists and
download all videos from it. Also, you can download only new videos from this
list, if you already have downloaded videos from these playlists. Videos are
saved in a directory with the name of the playlist.

### Install and run YTDV

Download code with follow command in terminal:

```commandline
git clone https://github.com/tagezi/ytvd.git
```

Go to ytvd directory:

```commandline
cd ytvd
```

Install requirements:

```commandline
pip install -r requirements.txt
```

Run script:

```commandline
python3 ./src/main.py
```

### Setup configuration

Now, there is the file for setup of playlists. This file has name playlist.txt
and can be found in config directory. Add links on your playlists in this file
each on a new line. If you want to skip a few files, you can add link to that
videos in slipvideos.txt. It is located in the same directory.

When a video from a playlist is downloaded, a link to the video is added to
the file slipvideos.txt. So, next time when you run script, only new videos
in playlist will download.

There is lines in main.py file:

```python
#: The file name with a list of playlists.
PLAYLIST_FILE = '../config/playlists.ini'
#: The file name with a list of files which needs skip.
VIDEO_SKIP_FILE = '../config/skipvideos.ini'
#: A path to the directory where files are saves.
```

You can change, if you need.

## Code documentation

### Constants

#### config.config.CONF_DIR(_ = '../config_ )
The directory where config files locate except for this.

#### config.config.VODEO_DIR(_ = '../files_ )
A path to the directory where files are saves.

#### config.config.CHANNELS_FILE(_ = '../config/channels.txt_ )
The file name with a list of YouTube channels.

#### config.config.PLAYLIST_FILE(_ = '../config/playlists.txt_ )
The file name with a list of YouTube playlists.

#### config.config.VIDEOS_FILE(_ = '../config/videos.txt_ )
The file name with a list of YouTube playlists.

#### config.config.VIDEO_SKIP_FILE(_ = '../config/skipvideos.txt_ )
The file name with a list of videos which needs skip.

### Function

#### main.get_list(sFileName)
Function opens a file and creates lList from lines of the file.

* **Parameters**

    **sFileName** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – A file name with lines from which needs to make the list.

* **Returns**

    The lList with lines from the file.

* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)

#### main.get_video(sURLPlayList)
Function takes playlist of YuoTube and downloads all files from it.
Additionally, the function types messages about the progress of
the downloading of the files.

* **Parameters**

    **sURLPlayList** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – An URl to the playlist with files
    which needs downloading.

#### main.set_skip_video(sVideoURL)
Function writes video URL in file with a list of files
which needs skipping.

* **Parameters**

    **sVideoURL** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – An URL which need add to the file.
