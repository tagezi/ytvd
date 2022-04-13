.. YouTube Video Downloader documentation master file, created by
   sphinx-quickstart on Sat Mar 26 16:16:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================
YTVD's documentation
=====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

------------------
User documentation
------------------

YTVD is YouTube Video Downloader
================================

It's not new library for downloading videos or video subtitles from YouTube.
YTVD is script which uses *PyTube like API* and *youtube_transcript_api* for
access to playlists and videos, and slightly expands the functionality. For
example, you can create a list with playlists and download all videos from it.
Also, you can download only new videos and video subtitles from this list,
if you already have downloaded videos from these playlists. Videos are saved
in a directory with the name of the playlist.

Install and run YTDV
====================

Download code with follow command in terminal:

.. prompt:: bash

   git clone https://github.com/tagezi/ytvd.git

Go to `ytvd` directory:

.. prompt:: bash

   cd ytvd

Install requirements:

.. prompt:: bash

   pip install -r requirements.txt

Run script:

.. prompt:: bash

   python3 ./ytvd.py

Setup configuration
===================

Now, there is the file for setup of playlists. This file has name `playlist.txt`
and can be found in `config` directory. Add links on your playlists in this file
each on a new line. If you want to skip a few files, you can add link to that
videos in `slipvideos.txt`. It is located in the same directory.

If you want to download only separated videos, you can add links to video to
`videos.txt` file.

When a video from a playlist is downloaded, a link to the video is added to
the file `slipvideos.txt`. So, next time when you run script, only new videos
in playlist will download.

There is lines in `./config/config.py` file:

.. autodata:: config.config.CONFIG_PATH

.. autodata:: config.config.VIDEO_PATH

.. autodata:: config.config.CHANNELS_FILE

.. autodata:: config.config.PLAYLIST_FILE

.. autodata:: config.config.VIDEOS_FILE

.. autodata:: config.config.VIDEO_SKIP_FILES

You can change, if you need.

Usage command line argument
===========================

.. argparse::
   :module: src.ytvd_help
   :func: get_argparser
   :prog: ytvd.py
   :noepilog:

------------------
Code documentation
------------------

Constants
=========

These

.. autodata:: config.config.CONFIG_PATH

.. autodata:: config.config.VIDEO_PATH

.. autodata:: config.config.CHANNELS_FILE

.. autodata:: config.config.PLAYLIST_FILE

.. autodata:: config.config.VIDEOS_FILE

.. autodata:: config.config.VIDEO_SKIP_FILES

Function
========

.. automodule:: ytvd_files
   :members:
   :exclude-members: get_list

.. automodule:: ytvd_video
   :members:
   :exclude-members: set_skip_video, write_subtitles, get_video

------------------
Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
