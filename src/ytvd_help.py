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
The module provides functions for displaying help and processing arguments.
"""

from argparse import ArgumentParser
from config.config import CHANNELS_FILE, PLAYLIST_FILE, VIDEOS_FILE, VIDEO_DIR


def get_argparser():
    """ Creates a description of command line arguments for use and help.

        :return: Filling ArgumentParser object.
        :rtype: ArgumentParser
        """
    sVideoDir = VIDEO_DIR()
    sDis = 'The script allows you to download videos from youtube from ' \
           'channels, playlists and just videos. Yuo can use arguments of ' \
           'command line or just give YouTube URL.'
    sUsage = 'ytvd.py [URL] [--argument [--argument=value [...]]]'
    sEpilog = '(c) tagezi. Licensed under the GPL 3.0'
    oParser = ArgumentParser(description=sDis,
                             epilog=sEpilog,
                             usage=sUsage
                             )
    sHelp = 'Points to a file with video channels.'
    oParser.add_argument('--pchannels',
                         dest="pchannels",
                         metavar="FILE",
                         nargs='?',
                         const=CHANNELS_FILE,
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Points to a file with playlist.'
    oParser.add_argument('--pplaylists',
                         dest="pplaylists",
                         metavar="FILE",
                         nargs='?',
                         const=PLAYLIST_FILE,
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Point to a file with videos.'
    oParser.add_argument('--pvideos',
                         dest="pvideos",
                         metavar="FILE",
                         nargs='?',
                         const=VIDEOS_FILE,
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Points to a directory where downloaded videos with playlists ' \
            'and channels will save. '
    oParser.add_argument('--psave',
                         dest="psave",
                         metavar="PATH",
                         nargs='?',
                         const=sVideoDir,
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Points to a directory where separate downloaded videos will save.'
    oParser.add_argument('--psavevideos',
                         dest="psavevideos",
                         metavar="PATH",
                         nargs='?',
                         const='videos',
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Downloads everything playlists from config file.'
    oParser.add_argument('--dplaylists',
                         dest='dplaylists',
                         action='store_true',
                         help=sHelp
                         )
    sHelp = 'Downloads everything videos from config file.'
    oParser.add_argument('--dvideos',
                         dest='dvideos',
                         action='store_true',
                         help=sHelp
                         )
    sHelp = 'Downloads everything videos from channels by config file.'
    oParser.add_argument('--dchannel',
                         dest='dchannel',
                         action='store_true',
                         help=sHelp
                         )
    sHelp = 'Downloads specific playlist.'
    oParser.add_argument('--splaylist',
                         dest="splaylist",
                         metavar="URL",
                         nargs='?',
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Downloads the specific video.'
    oParser.add_argument('--svideo',
                         dest="svideo",
                         metavar="URL",
                         nargs='?',
                         type=str,
                         help=sHelp
                         )

    sHelp = 'Downloads videos from specific channel.'
    oParser.add_argument('--schannel',
                         dest="schannel",
                         metavar="URL",
                         nargs='?',
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Downloads videos from specific channel by playlists.'
    oParser.add_argument('--plchannel',
                         dest="plchannel",
                         metavar="URL",
                         nargs='?',
                         type=str,
                         help=sHelp
                         )

    sHelp = 'Redownloads video. It will download one video ignoring file for' \
            ' skipping videos. If you need redownload all videos, you need ' \
            'to clean file to skipping videos.'
    oParser.add_argument('--rvideo',
                         dest="rvideo",
                         metavar="URL",
                         nargs='?',
                         type=str,
                         help=sHelp
                         )
    sHelp = 'Clean file for skipping download video.'
    oParser.add_argument('--cskip',
                         dest="cskip",
                         action='store_true',
                         help=sHelp
                         )
    sHelp = 'Downloads subtitles for videos, if exist. Default will be' \
            'download created automatically EN subtitles.'
    oParser.add_argument('--dsub',
                         dest="dsub",
                         action='store_true',
                         help=sHelp
                         )
    sHelp = 'Sets the language of downloaded subtitles.'
    oParser.add_argument('--ssub',
                         dest="ssub",
                         metavar="LANG",
                         nargs='?',
                         type=str,
                         help=sHelp
                         )
    return oParser
