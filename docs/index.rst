.. YouTube Video Downloader documentation master file, created by
   sphinx-quickstart on Sat Mar 26 16:16:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================
YTVD's documentation
=====================

.. image:: https://img.shields.io/pypi/pyversions/pytube.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/pytube/

YTVD is YouTube Video Downloader
================================

It's not new library for downloading videos or video subtitles from YouTube.
YTVD is script which uses *PyTube like API* for access to playlists and videos,
and slightly expands the functionality. For example, you can create a list with
playlists and download all videos from it.

Also, you can download only new videos and video subtitles from this list,
if you already have downloaded videos from these playlists. Videos are saved
in a directory with the name of the playlist.

.. note::
   Most people who post their videos on YouTube can only do so for some reward.
   When you download a video and watch it offline, the author has nothing.
   Don't forget to thank your author for his work so that he can continue to
   delight you further.

User documentation
==================

This application was developed as a console application in order to be used
along with the task scheduler. In addition, in fact, there is no functionality
here that really requires a GUI.

.. toctree::
   :maxdepth: 2

   user/install.rst
   user/firststart.rst
   user/setting.rst
   user/using.rst
   user/examples.rst
   user/troubleshooting.rst

Dev documentation
=================

If you decide to help improve this app in any way, I'll give you a quick
rundown of questions you might have. Any contribution is invaluable.

Thank you!

.. toctree::
   :maxdepth: 2

   dev/gratefulness.rst
   dev/agreement.rst
   dev/localization.rst
   dev/testing.rst
   dev/pulling.rst

------------------
Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
