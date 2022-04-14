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
It's not new library for downloading videos or video subtitles from YouTube.
YTVD is script which uses *PyTube like API* and *youtube_transcript_api* for
access to playlists and videos, and slightly expands the functionality. For
example, you can create a list with playlists and download all videos from it.
Also, you can download only new videos and video subtitles from this list,
if you already have downloaded videos from these playlists. Videos are
saved in a directory with the name of the playlist.
"""
from config.config import *
from src.ytvd_channel import *
from src.ytvd_files import clean_skip_file, get_list
from src.ytvd_help import get_argparser
from src.ytvd_playlist import get_list_playlists, get_playlist_videos
from src.ytvd_video import get_list_video, get_video, get_video_dir


def get_specific_video(oArgs, bSub, sLang):
    """ The function processes the url from the command line passed using the
    command line argument.

    :param oArgs: Arguments of command line.
    :type oArgs: ArgumentParser
    :param bSub: Does it need to download subtitles?
    :type bSub: bool
    :param sLang: A language of subtitles.
    :type sLang: str
    :return: None
    """
    sVideoPath = VIDEO_DIR()
    sVideoDir = 'videos'
    if oArgs.psave:
        sVideoPath = oArgs.psave
    if oArgs.psavevideos:
        sVideoDir = oArgs.psavevideos

    if oArgs.schannel:
        get_channel_videos(oArgs.schannel, sVideoPath, sVideoDir, bSub, sLang)
    if oArgs.plchannel:
        download_videos(oArgs.plchannel, sVideoPath, sVideoDir, bSub, sLang)
    if oArgs.splaylist:
        get_playlist_videos(oArgs.splaylist, sVideoPath, bSub, sLang)
    if oArgs.svideo:
        sDir = get_video_dir(sVideoPath, sVideoDir)
        get_video(oArgs.svideo, sDir, bSub, sLang)


def get_action(oPrsr):
    """ Creates a description of command line arguments for use and help.

    :param oPrsr: Argparse object.
    :type oPrsr: ArgumentParser
    """
    sVideoPath = VIDEO_DIR()
    sVideoDir = 'videos'
    sChannelFile = CHANNELS_FILE
    sPlaylistFile = PLAYLIST_FILE
    sVideosFile = VIDEOS_FILE
    bSubtitles = False
    # Get all string arguments.
    oArgs, oUnknown = oPrsr.parse_known_args()

    # Parsing unknown arguments.
    if oUnknown:
        if oUnknown[0].find('https://www.youtube.com/') == -1:
            return

        # Just to avoid clutter in the if operator.
        bChannel = (oUnknown[0].find('channel/') != -1)
        bPlaylist = (oUnknown[0].find('playlist') != -1)
        bPlaylistVar = (oUnknown[0].find('watch') != -1
                        and oUnknown[0].find('&list=') != -1)
        bVideosFile = (oUnknown[0].find('watch') != -1)

        if bChannel:
            download_videos(oUnknown[0], sVideoPath, sVideoDir)
        elif bPlaylist or bPlaylistVar:
            get_playlist_videos(oUnknown[0], sVideoPath)
        elif bVideosFile:
            lSkipVideo = get_list(VIDEO_SKIP_FILES)
            dValues = {'prefix': 0, 'repeat': True}
            while dValues['repeat'] and oUnknown[0] not in lSkipVideo:
                dValues = get_video(oUnknown[0], sVideoPath)
        else:
            # if the unknown arg isn't a YouTube link, it displays help
            oPrsr.print_help()
        return

    # Parsing known arguments.
    if oArgs.cskip:
        clean_skip_file()
    if oArgs.dsub or oArgs.ssub:
        bSubtitles = True
    if oArgs.schannel or oArgs.plchannel or oArgs.splaylist or oArgs.svideo:
        get_specific_video(oArgs, bSubtitles, oArgs.ssub)
    if oArgs.pchannels:
        sChannelFile = oArgs.pchannels
    if oArgs.pplaylists:
        sPlaylistFile = oArgs.pplaylists
    if oArgs.pvideos:
        sVideosFile = oArgs.pvideos
    if oArgs.dplaylists:
        get_channel_file(sChannelFile, sVideoPath, bSubtitles, oArgs.ssub)
    if oArgs.dplaylists:
        get_list_playlists(sPlaylistFile, sVideoPath, bSubtitles, oArgs.ssub)
    if oArgs.dvideos:
        get_list_video(sVideoPath, sVideoDir, sVideosFile,
                       bSubtitles, oArgs.ssub)


if __name__ == '__main__':
    oParser = get_argparser()
    get_action(oParser)
