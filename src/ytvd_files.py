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
The Script provides functions for working with files .
"""
import os
from config.config import VIDEO_SKIP_FILES


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


def set_skip_video(sURL):
    """ Function writes video URL in file with a list of files
    which needs skipping.

    :param sURL: An URL which need add to the file.
    :type sURL: str
    """
    with open(VIDEO_SKIP_FILES, 'a') as fSkipVideo:
        fSkipVideo.write(sURL)


def save_subtitles(sDir, sFile, oJOSNSubtitles):
    """ Function saves subtitles into a file as JOSN format.

    :param sDir: A path where the file will save.
    :type sDir: str
    :param sFile: A name of the file with subtitles.
    :type sFile: str
    :param oJOSNSubtitles: A list as JOSN.
    :type oJOSNSubtitles: josn
    """
    completeName = os.path.join(sDir, sFile + ".json")
    with open(completeName, 'w', encoding='utf-8') as json_file:
        json_file.write(oJOSNSubtitles)


if __name__ == '__main__':
    pass
