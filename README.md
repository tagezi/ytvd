YTVD is YouTube Video Downloader
================================

It's not new library for downloading videos or video subtitles from YouTube.
YTVD is script which uses *PyTube like API* for access to playlists and videos,
and slightly expands the functionality. For example, you can create a list with
playlists and download all videos from it.

Also, you can download only new videos and video subtitles from this list,
if you already have downloaded videos from these playlists. Videos are saved
in a directory with the name of the playlist.

**_NOTE:_**
   Most people who post their videos on YouTube can only do so for some reward.
   When you download a video and watch it offline, the author has nothing.
   Don't forget to thank your author for his work so that he can continue to
   delight you further.

User documentation
==================

This application was developed as a console application in order to be used
along with the task scheduler. In addition, in fact, there is no functionality
here that really requires a GUI.

Install and run YTDV
====================

**_NOTE:_**
   First of all, you should remember that this program is written in Python 3.9.
   So, it is necessary to `install its interpreter <https://www.python.org/>`
   for work. After installing python
   `install pip <https://pip.pypa.io/en/stable/installation/>`.

You can download code from only github now. Download zip archive from github
or use `git applications <https://git-scm.com/>`_ to sync with storage.

If you downloaded zip-file, unzip it to a folder of your choice.
Below are the commands if you decide to use git.

```bash
git clone https://github.com/tagezi/ytvd.git
```

Go to `ytvd` directory:

```bash
cd ytvd
```
Install requirements:

```bash
pip install -r requirements.txt
```

Now you are ready to run the script:

```bash
python3 ytvd
```

First start
===========
At the first start, a search for the program configuration will be executed,
and if it is not found, it will be offered to configure it.

You can customize the program to your liking or choose the default settings.

The following questions will be asked.

*Do you want to customize the configuration? (N/Y, default: N):*

If you select H, the setting will be default. If you pressed Y, then you can
customize the program to your liking.

By default, the directory where downloaded files and automatic configuration
files are stored is located in the user directory. You can specify a different
path. (For example, Daniel's directory is shown.)

*Enter path to home directory. (hit Enter to default: /home/daniel/):*

For example:

In Windows D disk: ``D:\``

In Linux Video directory of user ``daniel``: ```/home/daniel/Video```

If you do not know the rules of the operating system, use only lowercase and
uppercase letters, underscores and numerics.

*Specify a directory name where you want to upload video files?
(hit Enter to default: /home/daniel/YVTD):*

Specify a directory name or press Enter.

For example: ``YouTubeVideos``

At the moment, files for setting up automatic downloads in operating systems
cannot be moved.

If you use OS Windows, you see the message like this: *The config files will
stored in C:\\User\\Daniel\\YTVD)*.

If you use OS Unix-like, you can specify path.

*Specify a directory name where you want to story others config files of lists.
(hit Enter to default: /home/daniel/YTVD:*

For example:

``config``

By default, the files for configuring automation are named:

* channels.ini - file for channel list
* playlists.ini - file for playlist list
* videos.ini  - file for playlist list
* skipvideos.ini - a file to remember downloaded videos.

You can press Enter for default, or specify wishful name.

For example for skipping videos:

``myskippingvideos.txt``

After all the above settings, the main configuration file, files for automation
and directories will be created.

Setting configuration
===================

Now, there are files for setup automatic download. These files have names:

* `channels.ini` - file for channel list
* `playlists.ini` - file for playlist list
* `videos.ini`  - file for playlist list
* `skipvideos.ini` - a file to remember downloaded videos.

If you need, add links on your playlists in these files each on a new line. If
you want to skip a few videos, you can add link to that videos in
`slipvideos.ini`. It is located in the same directory.

When a video is downloaded, a link to the video is added automatically to the
file `slipvideos.txt`. So, next time when you run script, only new videos will
download.

Setting program
=============

There are lines in `./config/YTVD/config.ini` file for OS Unix-like, and in
`C:/User/YTVD/config/config.ini`:

```
    [PATH]
    root = /home/daniel
    video = YTVD
    config =

    [FILES]
    channels = channels.ini
    playlists = playlists.ini
    videos = videos.ini
    skip = skipvideos.ini
```
You can change, if you need.

Troubleshooting
===============

1. There is [bug in PyTube](https://github.com/pytube/pytube/issues/1281) 
that shows message:
```
Pytube Error: get_throttling_function_name: could not find match for multiple
```
The solution is in the discussion.

2. PyTube cannot convert subtitles from xml format to srt format. This problem
is bypassed in the code of this script.

If you find any bugs while using script or come up with an idea for 
improvement, feel free to [report](https://github.com/tagezi/ytvd/issues) them.
