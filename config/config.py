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
""""""  #
"""
It is configuration file to control script behavior.
"""

#: The directory where config files locate except for this.
CONF_DIR = '../config'
#: A path to the directory where files are saves.
VIODEO_DIR = '../files'


#: The file name with a list of YouTube channels.
CHANNELS_FILE = f'{CONF_DIR}/channels.txt'
#: The file name with a list of YouTube playlists.
PLAYLIST_FILE = f'{CONF_DIR}/playlists.txt'
#: The file name with a list of YouTube playlists.
VIDEOS_FILE = f'{CONF_DIR}/videos.txt'
#: The file name with a list of videos which needs skip.
VIDEO_SKIP_FILE = f'{CONF_DIR}/skipvideos.txt'
