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
The module creates and reads config parameter.
"""

import os
import re
from configparser import ConfigParser
from os.path import join
from pathlib import Path
from sys import platform

from ytvd.files import create_dir, create_file


def check_dirname(sDefaultName, sCheckingName):
    """ The function check name of directory for compliance with OS rules.

    :param sDefaultName: The name by default.
    :type sDefaultName: str
    :param sCheckingName: The name which needs to check.
    :type sCheckingName: str
    :return: The name that is according to OS rules or sDefaultName name.
    :rtype: str
    """
    if sCheckingName and not re.search(r'\W', sCheckingName):
        sDefaultName = sCheckingName

    return sDefaultName


def check_filename(sDefaultName, sCheckName):
    """ The function check name of filename for compliance with OS rules.

    :param sDefaultName: The name by default.
    :type sDefaultName: str
    :param sCheckName: The name which needs to check.
    :type sCheckName: str
    :return: The name that is according to OS rules or sDefaultName name.
    :rtype: str
    """
    if sCheckName and not re.search(r'[^A-Za-z\d_.]', sCheckName) \
            and (sCheckName.endswith('.ini') or sCheckName.endswith('.txt')):
        sDefaultName = sCheckName

    return sDefaultName


def config_read(sHome):
    """ The function return values of configuration as dictionary.

      *rootpath* - the path to directory where will bw saved video files.

      *confpath* - the path to directory where will bw saved list files.

      *channels* - the path to file where a list with URLs of YouTube channels
      stored.

      *playlists* - the path to file where a list with URLs of YouTube
      playlists stored.

      *videos* - the path to file where a list with URLs of YouTube videos
      stored.

      *skip* - the path to file where a list with URLs of YouTube videos
      that needs to skip.

    :param sHome: User's Home directory.
    :type sHome: str
    :return: The dictionaries with keys.
             dict[rootpath, confpath, channels, playlists, videos, skip]
    :rtype: dict
    """
    oConfig = ConfigParser()
    tMainConfig = config_path(sHome)
    oConfig.read(tMainConfig[1])

    sRoot = oConfig['PATH']['root']
    sVideoDir = oConfig['PATH']['video']
    sConfigDir = oConfig['PATH']['config']
    sChannelsFile = oConfig['FILES']['channels']
    sPlaylistsFile = oConfig['FILES']['playlists']
    sVideoFile = oConfig['FILES']['videos']
    sSkippingFile = oConfig['FILES']['skip']

    return {'rootpath': join(sRoot, sVideoDir),
            'confpath': join(sRoot, sVideoDir, sConfigDir),
            'channels': join(sRoot, sVideoDir, sConfigDir, sChannelsFile),
            'playlists': join(sRoot, sVideoDir, sConfigDir, sPlaylistsFile),
            'videos': join(sRoot, sVideoDir, sConfigDir, sVideoFile),
            'skip': join(sRoot, sVideoDir, sConfigDir, sSkippingFile)
            }


def config_path(sHome):
    """ Return a path to config file in OS rules.

    :param sHome: User's Home directory
    :type sHome: str
    :return: The path to config file and config file with path.
    :rtype: tuple[str, str]
    """
    if platform.startswith('win32') or platform.startswith('cygwin'):
        # For Windows
        CONFIG_PATH = join(sHome, PROG_NAME, CONFIG_DIR)
        CONFIG_FILE = join(CONFIG_PATH, 'config.ini')
    else:
        CONFIG_PATH = join(sHome, '.config', PROG_NAME)
        CONFIG_FILE = join(CONFIG_PATH, 'config.ini')

    return CONFIG_PATH, CONFIG_FILE


def prepare_space(sRootDir):
    """ Allows a user to specify the paths and file names that will be used
    when the program is running.

    :param sRootDir:
    :type sRootDir: str
    :return: None
    """
    tMainConfig = config_path(sRootDir)
    oConfigFile = Path(tMainConfig[1])
    if oConfigFile.is_file():
        return

    sConfDir = CONFIG_DIR
    sVideoDir = PROG_NAME
    sChannelFile = 'channels.ini'
    sPlaylistFile = 'playlists.ini'
    sVideoFile = 'videos.ini'
    sSkipVideoFile = 'skipvideos.ini'

    sAnswer = input('Do you want to customize the configuration? '
                    '(N/Y, default: N): ')

    if sAnswer == 'Y':
        print('You can specify HOME directory, where will be start '
              'directory tree \nof the program.\n'
              r'For example, in Windows: D:\ '
              '\nOr, for example, in Linux: /media/user/external_drive')
        sHInput = input(f'Enter path to home directory. '
                        f'(hit Enter to default: {sRootDir}): ')
        if sHInput and os.path.exists(sHInput):
            sRootDir = sHInput

        print('Use only uppercase and lowercase letters, underscores, and'
              'numbers in file \nand directory names. Give the filename an '
              'extension .ini, please. If the \nname is incorrect, the default'
              ' value will be used.')
        sVDir = input('Specify a directory name where you want to upload video'
                      ' files? (hit Enter to default:\n'
                      f' {join(sRootDir, sVideoDir)}: ')
        sVideoDir = check_dirname(sVideoDir, sVDir)

        if platform.startswith('win32') or platform.startswith('cygwin'):
            sPath = f'{join(str(Path.home()), PROG_NAME, "config")}'
            print(f'The config files will stored in {sPath}): ')
        else:
            sPath = f'{join(sRootDir, sVideoDir, CONFIG_DIR)}'
            print(f'The main configuration file will be stored in the'
                  f' directory {join(sRootDir, ".config", sVideoDir)}')
            sCDir = input(f'Specify a directory name where you want to story'
                          f' others config \nfiles of lists? (hit Enter to'
                          f' default: {sPath}): ')
            sConfDir = check_dirname(sConfDir, sCDir)

        sPath = f'{join(sRootDir, sVideoDir, "config")}'
        print(f'A list file of channel urls is storage in {sPath}')
        sCFile = input(f'Specify the filename (hit Enter to default: '
                       f'{sChannelFile}): ')
        sChannelFile = check_filename(sChannelFile, sCFile)

        sPFile = input(f'Specify a file name of a playlist list.\n'
                       f'(hit Enter to default: {sPlaylistFile}): ')
        sPlaylistFile = check_filename(sPlaylistFile, sPFile)

        sVFile = input(f'Specify a file name of a video list.\n'
                       f'(hit Enter to default: {sVideoFile}): ')
        sVideoFile = check_filename(sVideoFile, sVFile)

        print('You probably don\'t need to directly tamper with the file to '
              'skip the video.')
        sSFile = input('But you can specify its name'
                       f'(hit Enter to default: {sSkipVideoFile}):\n')
        sSkipVideoFile = check_filename(sSkipVideoFile, sSFile)

    tMainConfig = config_path(sRootDir)

    create_dir(tMainConfig[0])
    create_dir(join(sRootDir, sVideoDir))
    create_dir(join(sRootDir, sVideoDir, sConfDir))

    oConfig = ConfigParser()
    oConfig['PATH'] = {'root': sRootDir,
                       'video': sVideoDir,
                       'config': sConfDir}
    oConfig['FILES'] = {'channels': sChannelFile,
                        'playlists': sPlaylistFile,
                        'videos': sVideoFile,
                        'skip': sSkipVideoFile}

    with open(tMainConfig[1], 'w') as fConfig:
        oConfig.write(fConfig)

    create_file(join(sRootDir, sVideoDir, sConfDir, sChannelFile))
    create_file(join(sRootDir, sVideoDir, sConfDir, sPlaylistFile))
    create_file(join(sRootDir, sVideoDir, sConfDir, sVideoFile))
    create_file(join(sRootDir, sVideoDir, sConfDir, sSkipVideoFile))


PROG_NAME = 'YTVD'
CONFIG_DIR = ''
HOME_PATH = str(Path.home())
# Constant with config data.
try:
    CONFIG = config_read(HOME_PATH)
except KeyError:
    prepare_space(HOME_PATH)
    CONFIG = config_read(HOME_PATH)
