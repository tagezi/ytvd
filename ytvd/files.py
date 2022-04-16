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
The module provides functions for working with files and directories.
"""
import os


def create_dir(sDir):
    """ The function creates directory, if it does not exist.

    :param sDir: A name of the directory.
    :type sDir: str
    :return: None
    """
    if not os.path.exists(sDir):
        os.makedirs(sDir)


def create_file(sPath, sString=''):
    """ The Function create empty file. It can be used to cleaning skip file
    of videos."""
    with open(sPath, 'w') as fFile:
        fFile.write(sString)


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


def get_dir(sDirStart, sDirEnd):
    """ The function gives human-readable name for concatenate parts of path
    for directories to one string.

    :param sDirStart: The start of path. It comes from a constant in
                       config file or an argument in command line.
    :type sDirStart: str
    :param sDirEnd: The end of path. It is hard-coded parameter,
                      but sVideoDir can be specified in an argument of
                      command line.
    :type sDirEnd: str
    :return: The path in system rules.
    :rtype: str
    """
    return os.path.join(sDirStart, sDirEnd)


def save_subtitles(sDir, sFile, sSub):
    """ Function saves subtitles into a file as JOSN format.

    :param sDir: A path where the file will save.
    :type sDir: str
    :param sFile: A name of the file with subtitles.
    :type sFile: str
    :param sSub: A list as JOSN.
    :type sSub: josn
    """
    sFilePath = os.path.join(sDir, sFile + ".srt")
    with open(sFilePath, 'w', encoding='utf-8') as fSTR:
        fSTR.write(sSub)


def set_skip_video(sFile, sURL):
    """ Function writes video URL in file with a list of files
    which needs skipping.

    :param sFile: The config fFile where stored URLs for skipping video.
    :type sFile: str
    :param sURL: An URL which need add to the file.
    :type sURL: str
    :return: None
    """
    with open(sFile, 'a') as fSkipVideo:
        fSkipVideo.write(sURL)


if __name__ == '__main__':
    pass
