.. YouTube Video Downloader documentation master file, created by
   sphinx-quickstart on Sat Mar 26 16:16:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================
YTVD's documentation
=====================


YTVD is YouTube Video Downloader
================================

It's not new library for downloading videos or video subtitles from YouTube.
YTVD is script which uses *PyTube like API* for access to channels, playlists
and videos of YouTube, and slightly expands its functionality. For example,
you can create a list with channels, playlists or/and download all videos and
video subtitles from it.

Also, in the next time you can download only new videos and video subtitles
from these lists without re-downloading already downloaded videos. Videos are
saved in a directory with the name of the channels/playlist/.

.. note::
   Most people who post their videos on YouTube can only do so for some reward.
   When you download a video and watch it offline, the author has nothing.
   Don't forget to thank author for authors work so that author can continue to
   delight you further.

User documentation
==================

YTVD was developed as a console application in order to be used along with the
task scheduler. In addition, in fact, there is no functionality here that
really requires a GUI.

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
