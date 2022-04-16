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

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
from files import save_subtitles


def get_subtitles(sDir, sFile, sURL, sLang):
    lKey = sURL.split('=')
    transcript = YouTubeTranscriptApi.get_transcript(lKey[1])

    oFormatter = JSONFormatter()
    formatted = oFormatter.format_transcript(transcript)
    print('Скачиваю субтитры.')

    save_subtitles(sDir, sFile, formatted)
