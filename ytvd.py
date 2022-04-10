#     This code is a part of program Science Articles Orderliness
#     Copyright (C) 2021  Valerii Goncharuk (aka tagezi)
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from src.ytvd_playlist import get_playlist_videos
from src.ytvd_files import get_list
from src.ytvd_video import get_video
from config.config import CHANNELS_FILE, PLAYLIST_FILE, \
    VIDEOS_FILE, VIDEO_DIR

"""
It's not new library for downloading videos or video subtitles from YouTube. 
YTVD is script which uses *PyTube like API* and *youtube_transcript_api* for
access to playlists and videos, and slightly expands the functionality. For 
example, you can create a list with playlists and download all videos from it.
Also, you can download only new videos and video subtitles from this list, 
if you already have downloaded videos from these playlists. Videos are
saved in a directory with the name of the playlist.
"""

if __name__ == '__main__':
    lPlayListURLs = get_list(PLAYLIST_FILE)
    if lPlayListURLs:
        for sPlayListURL in lPlayListURLs:
            get_playlist_videos(sPlayListURL)
    lVideoURLs = get_list(VIDEOS_FILE)
    if lVideoURLs:
        for sVideoURL in lVideoURLs:
            get_video(sVideoURL, VIDEO_DIR())
