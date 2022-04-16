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
from files import get_list, get_dir
from video import get_video
from config import CONFIG


def get_list_playlists(sPlaylistFile, sDir, bSub=False, sLang=''):
    """ The function uses a list from a config file with a list of playlists.

    :param sPlaylistFile: A name of the file containing a list of playlists.
    :type sPlaylistFile: str
    :param sDir: A path to directory where will be downloaded playlists.
    :type sDir: str
    :param bSub: Does it need to download subtitles?
    :type bSub: bool
    :param sLang: A language of subtitles.
    :type sLang: str
    :return: None
    """
    lPlayListURLs = get_list(sPlaylistFile)
    if lPlayListURLs:
        for sPlayListURL in lPlayListURLs:
            get_playlist_videos(sPlayListURL, sDir, bSub, sLang)


def get_playlist_videos(sURL, sDir, bSub=False, sLang=''):
    """ Function takes playlist's url of YuoTube and downloads all files
    from it. Additionally, the function types messages about the progress of
    the downloading of the files.

    :param sURL: An URl to the playlist with files which needs downloading.
    :type sURL: str
    :param sDir: A directory where video files will save.
    :type sDir: str
    :param bSub: The flag which specify that subtitles should be downloaded.
    :type bSub: bool
    :param sLang: A language of subtitles that need to download.
    :type sLang: str
    :return: None
    """
    oPlayList = Playlist(sURL)
    sPlayListDir = get_dir(sDir, oPlayList.title)
    print(f'\n{oPlayList.title}\n{oPlayList.playlist_url}')

    dValues = {'prefix': 1, 'repeat': True}
    for sURLVideo in oPlayList.video_urls:
        lSkipVideo = get_list(CONFIG['skip'])
        if sURLVideo in lSkipVideo:
            dValues['prefix'] = dValues['prefix'] + 1

        dValues['repeat'] = True
        while dValues['repeat'] and sURLVideo not in lSkipVideo:
            dValues = get_video(sURLVideo, sPlayListDir, bSub, sLang,
                                dValues['prefix'])


if __name__ == '__main__':
    get_list_playlists(CONFIG['playlists'], CONFIG['path'])
