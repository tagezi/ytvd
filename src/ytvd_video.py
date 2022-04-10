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
The Script downloads videos by URL.
"""

import os
import socket

from time import sleep
# it can have matter to use youtube_dl or ytpy
from pytube import YouTube, exceptions
from urllib.error import HTTPError

from src.ytvd_files import set_skip_video
from src.ytvd_subtitles import get_subtitles


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

            fFileName = f'{sPrefix}{oYouStream.default_filename}'
            oYouStream.download(filename=fFileName, output_path=sDir)
            get_subtitles(sDir, fFileName, sURL)
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


if __name__ == '__main__':
    pass
