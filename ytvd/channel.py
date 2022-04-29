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
The module represents the main functionality for obtaining information about
the YouTube channel.
"""
from bs4 import BeautifulSoup
from pytube import Channel

from ytvd.config import CONFIG
from ytvd.files import get_list, get_dir
from ytvd.playlist import get_playlist_videos
from ytvd.video import get_video


def download_videos(sChannelURL, sDir, sDirVideos, bSub=False, sLang=''):
    """ The function uses a list from a config file with a list of playlists.

    :param sChannelURL: A name of the file containing a list of channels.
    :type sChannelURL: str
    :param sDir: A path to directory where will be downloaded channels.
    :type sDir: str
    :param sDirVideos: A path to directory where will be downloaded videos.
    :type sDirVideos: str
    :param bSub: Does it need to download subtitles?
    :type bSub: bool
    :param sLang: A language of subtitles.
    :type sLang: str
    :return: None
    """
    lPlaylists = get_chanel_playlists(sChannelURL)
    sDir = get_dir(sDir, Channel(sChannelURL).channel_name)
    for sPlaylistURL in lPlaylists:
        get_playlist_videos(sPlaylistURL, sDir, bSub, sLang)
    get_channel_videos(sChannelURL, sDir, sDirVideos, bSub, sLang)


def get_channel_file(sChannelFile, sDir, sDirVideos, bSub=False, sLang=''):
    """ The function uses a list from a config file with a list of playlists.

    :param sChannelFile: A name of the file containing a list of channels.
    :type sChannelFile: str
    :param sDir: A path to directory where will be downloaded channels.
    :type sDir: str
    :param sDirVideos: A path to directory where will be downloaded videos.
    :type sDirVideos: str
    :param bSub: Does it need to download subtitles?
    :type bSub: bool
    :param sLang: A language of subtitles.
    :type sLang: str
    :return: None
    """
    lChannelURLs = get_list(sChannelFile)
    if lChannelURLs:
        for sChannelURL in lChannelURLs:
            download_videos(sChannelURL, sDir, sDirVideos, bSub, sLang)


def get_chanel_playlists(sChannelURL):
    """ Here is used Tarot cards, magic ball and ancient voodoo to get a
    list of playlists from the garbage that YouTube returns instead of the
    normal conscious code.

    :param sChannelURL: An URL of YouTube channel.
    :type sChannelURL: str
    :return: A list of playlists.
    :rtype: list
    """
    #: Get HTML code from pytube and select all <script>s by BeautifulSoup
    sPlaylists = Channel(sChannelURL).playlists_html
    sHTML = BeautifulSoup(sPlaylists, 'html5lib')
    oScripts = sHTML.findAll('script')
    #: Let's find the trash where YouTube put the playlist codes
    #: ytInitialData is var in the script we need
    sScript = ''
    for oScript in oScripts:
        if str(oScript).find('ytInitialData') != -1:
            sScript = str(oScript)
            break

    #: In this case, working with giant multi-level JSON as a string is faster
    #: and more efficient. Then to look for all occurrences of a playlistId and
    #: take the playlist code after it.
    lPlaylists = []
    while sScript.find('playlistId') != -1:
        sCode = sScript.partition('playlistId":"')[2].partition('","')[0]
        lPlaylists.append(f'https://www.youtube.com/playlist?list={sCode}')
        sScript = sScript.partition('","')[2]

    #: So, we have list where code of playlists repeat many times.
    #: Remove Duplicates.
    return list(set(lPlaylists))


def get_channel_videos(sChannelURL, sDir, sDirVideos, bSub=False, sLang=''):
    """ The function downloads all videos what is not in skipping file.

    :param sChannelURL: An URL of YouTube channel.
    :type sChannelURL: str
    :param sDir: A directory where will save videos.
    :type sDir: str
    :param bSub: Does it need to download subtitles?
    :type bSub: bool
    :param sLang: A language of subtitles.
    :type sLang: str
    :return: None
    """
    lVideos = Channel(sChannelURL)
    for sVideoURL in lVideos.video_urls:
        sDir = get_dir(sDir, lVideos.channel_name)
        sDir = get_dir(sDir, sDirVideos)
        lSkipVideo = get_list(CONFIG['skip'])
        dValues = {'prefix': 0, 'repeat': True}
        while dValues['repeat'] and sVideoURL not in lSkipVideo:
            dValues = get_video(sVideoURL, sDir, bSub, sLang)
