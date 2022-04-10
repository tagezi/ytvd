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

"""
The Script downloads files from specified playlists.
"""

from pytube import Playlist
from src.ytvd_files import get_list
from src.ytvd_video import get_video
from config.config import VIDEO_DIR, VIDEO_SKIP_FILES


def get_playlist_videos(sURL):
    """ Function takes playlist's url of YuoTube and downloads all files
    from it. Additionally, the function types messages about the progress of
    the downloading of the files.

    :param sURL: An URl to the playlist with files which needs downloading.
    :type sURL: str
    """
    oPlayList = Playlist(sURL)
    sPlayListDir = f'{VIDEO_DIR}/{oPlayList.title}'
    print(f'\n{oPlayList.title}\n{oPlayList.playlist_url}')

    dValues = {'prefix': 1, 'repeat': True}
    for sURLVideo in oPlayList.video_urls:
        lSkipVideo = get_list(VIDEO_SKIP_FILES)
        if sURLVideo in lSkipVideo:
            dValues['prefix'] = dValues['prefix'] + 1

        dValues['repeat'] = True
        while dValues['repeat'] and sURLVideo not in lSkipVideo:
            dValues = get_video(sURLVideo, sPlayListDir, dValues['prefix'])


if __name__ == '__main__':
    pass
















