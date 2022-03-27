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

It's not new library for downloading videos from YouTube. YTVD is script which
uses *PyTube like API* for access to playlists and videos, and slightly expands
the functionality. For example, you can create a list with playlists and
download all videos from it. Also, you can download only new videos from this
list, if you already have downloaded videos from these playlists. Videos are
saved in a directory with the name of the playlist.

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

   python3 ./src/main.py

Setup configuration
===================

Now, there is the file for setup of playlists. This file has name `playlist.txt`
and can be found in `config` directory. Add links on your playlists in this file
each on a new line. If you want to skip a few files, you can add link to that
videos in `slipvideos.txt`. It is located in the same directory.

When a video from a playlist is downloaded, a link to the video is added to
the file `slipvideos.txt`. So, next time when you run script, only new videos
in playlist will download.

There is lines in main.py file:

.. code-block:: python

   #: The file name with a list of playlists.
   PLAYLIST_FILE = '../config/playlists.txt'
   #: The file name with a list of files which needs skip.
   VIDEO_SKIP_FILE = '../config/skipvideos.txt'
   #: A path to the directory where files are saves.

You can change, if you need.

------------------
Code documentation
------------------

Constants
=========

.. autodata:: config.config.CONF_DIR

.. autodata:: config.config.VODEO_DIR


.. autodata:: config.config.CHANNELS_FILE

.. autodata:: config.config.PLAYLIST_FILE

.. autodata:: config.config.VIDEOS_FILE

.. autodata:: config.config.VIDEO_SKIP_FILE

Function
========

.. automodule:: main
   :members:
   :exclude-members: PLAYLIST_FILE, VIDEO_SKIP_FILE, VODEO_DIR

------------------
Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
