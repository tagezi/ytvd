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
The Script downloads subtitles by URL.
"""

import xml.etree.ElementTree as ET
from datetime import timedelta
from pytube import YouTube

from files import save_subtitles


def get_subtitles(sDir, sFile, oYouTube, sLang='en'):
    """ The function downloads and converts YouTube subtitles.

    :param sDir: The directory where video was downloaded.
    :type sDir: str
    :param sFile: A name of the video.
    :type sFile: str
    :param oYouTube: An object of pytube where stored information about video.
    :type oYouTube: YouTube
    :param sLang: A code of language in lower case.
    :return: None
    """
    oCaptions = oYouTube.captions[sLang]
    # In pytube there is bug with converting
    # See: https://github.com/pytube/pytube/issues/1085
    sSub = convert_xml_to_srt(oCaptions.xml_captions)
    save_subtitles(sDir, sFile, sSub)


def convert_xml_to_srt(sXMLSub):
    dXMLTree = ET.fromstring(sXMLSub)
    iNumSub = 1
    sSub = ''
    for dTagP in dXMLTree.iter('p'):
        sStartTime = covert_time(int(dTagP.attrib["t"]))
        sEndTime = covert_time(int(dTagP.attrib["t"]) + int(dTagP.attrib["d"]))
        sSub = f'{sSub}{iNumSub}\n{sStartTime}' \
               f' --> {sEndTime}\n{dTagP.text}\n\n'
        iNumSub += 1
    return sSub


def covert_time(iMsTime):
    oTime = timedelta(milliseconds=iMsTime)
    sTime = oTime.__str__()

    if sTime.find('.') == -1:
        sTime = f'{sTime}.000'

    if len(sTime.split('.')[1]) > 4:
        sTime = sTime[:-3]

    if len(sTime.split(':')[1]) < 2:
        sTime = f'0{sTime}'

    return sTime

