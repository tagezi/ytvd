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

import os
import socket

from time import sleep
# it can have matter to use youtube_dl or ytpy
from pytube import Playlist, YouTube, exceptions
from urllib.error import HTTPError

from config.config import CHANNELS_FILE, PLAYLIST_FILE, \
    VIDEOS_FILE, VIODEO_DIR, VIDEO_SKIP_FILE
""""""  #
"""
The Script downloads files from specified playlists.
"""


def set_skip_video(sURL):
    """ Function writes video URL in file with a list of files
    which needs skipping.

    :param sURL: An URL which need add to the file.
    :type sURL: str
    """
    with open(VIDEO_SKIP_FILE, 'a') as fSkipVideo:
        fSkipVideo.write(sURL)


def get_list(sFileName):
    """ Function opens a file and creates lList from lines of the file.

    :param sFileName: A file name with lines from which needs to make the list.
    :type sFileName: str
    :return: The lList with lines from the file.
    :rtype: list
    """
    lList = []
    with open(sFileName, 'r') as fList:
        for line in fList:
            lList.append(line.strip('\n').strip())

    return lList


def get_video(sURL, sDir, Prefix=0, bRepeat=True):
    """ Function takes a video by URL and saves it in directory.

    :param sURL: An URL of the video on YouTube.
    :type sURL: str

    :param sDir: A directory where the video will save. For a video of the
                playlist it is a name of the playlist. Otherwise, it is
                a *Videos* directory.
    :type sDir: str

    :param Prefix: It is number as int for substitution at the beginning
                  of the line.
    :type Prefix: int or None

    :param bRepeat: It points that downloading should be repeated.
    :type bRepeat: bool

    :return: Returns two parameters as dict. The parameter *repeat* with value
            *True* points that downloading of the videos needs repeat.
            The parameter *prefix* points on index number of videos
            in the playlist.
    :rtype: dict[int, bool]
    """
    try:
        oYouTube = YouTube(sURL)
        print(f'{str(Prefix)}. {oYouTube.title}')
    except exceptions.VideoUnavailable:
        print(f'Видео по адресу {sURL} недоступно. Пропускаем.')
    else:
        print(f'Скачиваю видео по адресу: {sURL}')
        oYouTube.streams.filter(file_extension='mp4')
        oYouStream = oYouTube.streams.get_highest_resolution()
        try:
            if not os.path.exists(sDir):
                os.makedirs(sDir)

            sPrefix = ''
            if type(Prefix) == int:
                sPrefix = f'{str(Prefix)}. '

            oYouStream.download(
                filename=f'{sPrefix}{oYouStream.default_filename}',
                output_path=sDir
            )
        except socket.error:
            print(f'socket.error: Ошибка скачивания видео {sURL}')
        except HTTPError:
            print(f'HTTPError: Ошибка скачивания видео {sURL}')
        else:
            bRepeat = False
            set_skip_video(f'{sURL}\n')
            if type(Prefix) == int:
                Prefix = Prefix + 1
    finally:
        sleep(15)
    return {'prefix': Prefix, 'repeat': bRepeat}


def get_playlist_videos(sURL):
    """ Function takes playlist's url of YuoTube and downloads all files
    from it. Additionally, the function types messages about the progress of
    the downloading of the files.

    :param sURLPlayList: An URl to the playlist with files
                         which needs downloading.
    :type sURLPlayList: str
    """
    oPlayList = Playlist(sURL)
    sPlayListDir = f'{VIODEO_DIR}/{oPlayList.title}'
    print(f'\n{oPlayList.title}\n{oPlayList.playlist_url}')

    dValues = {'prefix': 1, 'repeat': True}
    for sURLVideo in oPlayList.video_urls:
        lSkipVideo = get_list(VIDEO_SKIP_FILE)
        if sURLVideo in lSkipVideo:
            dValues['prefix'] = dValues['prefix'] + 1
        dValues['repeat'] = True
        while dValues['repeat'] and sURLVideo not in lSkipVideo:
            dValues = get_video(sURLVideo, sPlayListDir, dValues['prefix'])


if __name__ == '__main__':
    lPlayListURLs = get_list(PLAYLIST_FILE)
    if lPlayListURLs:
        for sPlayListURL in lPlayListURLs:
            get_playlist_videos(sPlayListURL)
    lVideoURLs = get_list(VIDEOS_FILE)
    if lVideoURLs:
        for sVideoURL in lVideoURLs:
            get_video(sVideoURL, VIODEO_DIR)
















