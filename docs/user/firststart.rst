.. run:

First start
===========
At the first start, a search for the program configuration will be execute,
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
