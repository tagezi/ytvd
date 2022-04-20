.. setting:

Setup configuration
===================

Now, there are files for setup automatic download. These files have names:

* `channels.ini` - file for channel list
* `playlists.ini` - file for playlist list
* `videos.ini`  - file for playlist list
* `skipvideos.ini` - a file to remember downloaded videos and prevent them from
being downloaded again.

If you need, add links on your playlists in these files each on a new line. If
you want to skip a few videos, you can add link to that videos in
`slipvideos.ini`. It is located in the same directory.

When a video is downloaded, a link to the video is added authomaticaly to the
file `slipvideos.txt`. So, next time when you run script, only new videos will
download.

Program setup
=============

There are lines in `./config/YTVD/config.ini` file for OS Unix-like, and in
`C:/User/YTVD/config/config.ini:

.. code-block::

    [PATH]
    root = /home/daniel
    video = YTVD
    config =

    [FILES]
    channels = channels.ini
    playlists = playlists.ini
    videos = videos.ini
    skip = skipvideos.ini

You can change, if you need.
