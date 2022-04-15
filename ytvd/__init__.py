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
YTVD: a very unserious Python library for downloading YouTube Videos. ;)
"""
__title__ = "YTVD"
__author__ = "Valerii Goncharuk"
__license__ = "GPL 3.0"

from ytvd.config import *
from ytvd.version import __version__
from ytvd.channel import *
from ytvd.files import *
from ytvd.help import *
from ytvd.playlist import *
from ytvd.subtitles import *
from ytvd.video import *
from ytvd.__main__ import get_action

if __name__ == '__main__':
    get_action(get_argparser())