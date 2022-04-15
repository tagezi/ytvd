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
import socket

from time import sleep
# it can have matter to use youtube_dl or ytpy
from pytube import YouTube, exceptions
from urllib.error import HTTPError

from ytvd.config import CONFIG
from ytvd.files import create_dir, get_list, get_dir, set_skip_video
from ytvd.subtitles import get_subtitles


def get_list_video(sVideoPath, sVideoDir, sFile, bSub=False, sLang=''):
    """ The function uses a list from a config file with a list videos.

    :param sVideoPath: The start of path. It comes from a constant in
                      config file or an argument in command line.
    :type sVideoPath: str
    :param sVideoDir: The end of path. It is hard-coded parameter,
                      but sVideoDir can be specified in an argument of
                      command line.
    :type sVideoDir: str
    :param sFile: A name of the config file with a list videos.
    :type sFile: str
    :param bSub: Point to necessity of downloads subtitles.
    :type bSub: bool
    :param sLang: A code of language for subtitles.
    :type sLang: str
    :return: None
    """
    lVideoURLs = get_list(sFile)
    if lVideoURLs:
        sDir = get_dir(sVideoPath, sVideoDir)
        for sVideoURL in lVideoURLs:
            lSkipVideo = get_list(CONFIG['skip'])
            dValues = {'prefix': 1, 'repeat': True}
            while dValues['repeat'] and sVideoURL not in lSkipVideo:
                dValues = get_video(sVideoURL, sDir, bSub, sLang)


def get_video(sURL, sDir, bSub=False, sLang='', iPrefix=0, bRepeat=True):
    """ The function takes a video by URL and saves it in specified directory.

    :param sURL: An URL of the video on YouTube.
    :type sURL: str
    :param sDir: A directory where the video will save. For a video of the
                playlist it is a name of the playlist. Otherwise, it is
                a *Videos* directory.
    :type sDir: str
    :param bSub: Point to necessity of downloads subtitles.
    :type bSub: bool
    :param sLang: A code of language for subtitles.
    :type sLang: str
    :param iPrefix: It is number as int for substitution at the beginning
                  of the line. If Prefix = 0, no prefix will be added.
    :type iPrefix: int or None
    :param bRepeat: It points that downloading should be repeated.
    :type bRepeat: bool

    :return: Returns two parameters as dict. The parameter *repeat* with value
            *True* points to that downloading of the videos needs repeat.
            The parameter *prefix* points on index number of videos
            in the playlist.
    :rtype: dict[int, bool]
    """
    if not sURL:
        return {'prefix': iPrefix, 'repeat': False}

    try:
        oYouTube = YouTube(sURL)
    except exceptions.VideoUnavailable:
        print(f'The video at {sURL} is not available. Skip.')
    else:
        oYouTube.streams.filter(file_extension='mp4')
        oYouStream = oYouTube.streams.get_highest_resolution()
        create_dir(sDir)

        sPrefix = ''
        if iPrefix > 0:
            sPrefix = f'{str(iPrefix)}. '

        fFileName = f'{sPrefix}{oYouStream.default_filename}'
        print(f'Downloading video at: {sURL}')
        print(fFileName)
        try:
            oYouStream.download(filename=fFileName, output_path=sDir)
            if bSub:
                get_subtitles(sDir, fFileName, sURL, sLang)
        except socket.error:
            print(f'socket.error: Error of downloading video {sURL}')
        except HTTPError:
            print(f'HTTPError: Error of downloading video {sURL}')
        else:
            bRepeat = False
            set_skip_video(f'{sURL}\n')
            if iPrefix > 0:
                iPrefix = iPrefix + 1
    finally:
        sleep(15)
    return {'prefix': iPrefix, 'repeat': bRepeat}


if __name__ == '__main__':
    get_list_video(CONFIG['path'], 'videos', CONFIG['videos'], False, '')
