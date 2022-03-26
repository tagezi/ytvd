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

import os
import socket

from time import sleep
from pytube import Playlist, YouTube, exceptions
from urllib.error import HTTPError

#: The file name with a list of playlists.
PLAYLIST_FILE = '../config/playlists.txt'
#: The file name with a list of files which needs skip.
VIDEO_SKIP_FILE = '../config/skipvideos.txt'
#: A path to the directory where files are saves.
VODEO_DIR = '../files/'


def set_skip_video(sVideoURL):
    """ Function writes video URL in file with a list of files
    which needs skipping.

    :param sVideoURL: An URL which need add to the file.
    :type sVideoURL: str
    """
    with open(VIDEO_SKIP_FILE, 'a') as fSkipVideo:
        fSkipVideo.write(sVideoURL)


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


def get_video(sURLPlayList):
    """ Function takes playlist of YuoTube and downloads all files from it.
    Additionally, the function types messages about the progress of
    the downloading of the files.

    :param sURLPlayList: An URl to the playlist with files
                         which needs downloading.
    :type sURLPlayList: str
    """
    oPlayList = Playlist(sURLPlayList)
    print(f'\n{oPlayList.title}\n{oPlayList.playlist_url}')
    # sleep(2)

    sPlayListDir = f'{VODEO_DIR}{oPlayList.title}'
    if not os.path.exists(sPlayListDir):
        os.makedirs(sPlayListDir)

    num = 1
    for sVideoURL in oPlayList.video_urls:
        bRepeat = True
        lSkipVideo = get_list(VIDEO_SKIP_FILE)
        if sVideoURL in lSkipVideo:
            num = num + 1
        while bRepeat and sVideoURL not in lSkipVideo:
            try:
                oYouTube = YouTube(sVideoURL)
                print(f'{str(num)}. {oYouTube.title}')
            except exceptions.VideoUnavailable:
                print(f'Видео по адресу {sVideoURL} недоступно. Пропускаем.')
                sleep(15)
            else:
                print(f'Скачиваю виде по адресу: {sVideoURL}')
                oYouTube.streams.filter(file_extension='mp4')
                oYouStream = oYouTube.streams.get_highest_resolution()
                try:
                    oYouStream.download(
                        filename=f'{str(num)}. {oYouStream.default_filename}',
                        output_path=sPlayListDir
                    )
                except socket.error:
                    print(f'socket.error: Ошибка скачивания видео {sVideoURL}')
                except HTTPError:
                    print(f'HTTPError: Ошибка скачивания видео {sVideoURL}')
                else:
                    bRepeat = False
                    set_skip_video(f'{sVideoURL}\n')
                    num = num + 1
                finally:
                    sleep(15)


if __name__ == '__main__':
    for sPlayListURL in get_list(PLAYLIST_FILE):
        get_video(sPlayListURL)
