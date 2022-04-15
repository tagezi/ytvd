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
The module reads config parameter.
"""
from configparser import ConfigParser
from os.path import join
from pathlib import Path
from sys import platform

from ytvd.files import get_dir

CONFIG_DIR = 'config'
YTVD_DIR = 'YTVD'
if platform.startswith('win32') or platform.startswith('cygwin'):
    CONFIG_PATH = join(str(Path.home()), YTVD_DIR, CONFIG_DIR)
    CONFIG_FILE = join(CONFIG_PATH, 'config.ini')
else:
    CONFIG_PATH = join(str(Path.home()), '.local', YTVD_DIR, CONFIG_DIR)
    CONFIG_FILE = join(CONFIG_PATH, 'config.ini')


def config_read():
    """ The function return values of configuration as dictionary.
      *path* - the path to directory where will bw saved video files.

      *channels* - the path to file where a list with URLs of YouTube channels
      stored.

      *playlists* - the path to file where a list with URLs of YouTube
      playlists stored.

      *videos* - the path to file where a list with URLs of YouTube videos
      stored.

      *skip* - the path to file where a list with URLs of YouTube videos
      that needs to skip.

    :return: The dictionary with keys.
    :rtype: dict
    """
    oConfig = ConfigParser()
    oConfig.read(CONFIG_FILE)

    return {'path': join(str(Path.home()), oConfig['PATH']['path']),
            'channels': join(CONFIG_PATH, oConfig['FILES']['channel']),
            'playlists': join(CONFIG_PATH, oConfig['FILES']['playlists']),
            'videos': join(CONFIG_PATH, oConfig['FILES']['videos']),
            'skip': join(CONFIG_PATH, oConfig['FILES']['skip'])}


CONFIG = config_read()

if __name__ == '__main__':
    pass
