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
""" Test Case for module config. """
import unittest
from pathlib import Path
from sys import platform

from ytvd.config import check_dirname, check_filename, config_path


class TestConfig(unittest.TestCase):

    def test_check_dirname(self):
        """ Cheack the function check_dirname. """
        sName = 'example'
        self.assertEqual(sName, check_dirname(sName, 'abc/dfg'))
        self.assertEqual(sName, check_dirname(sName, r'abc\dfg'))
        self.assertEqual(sName, check_dirname(sName, 'abc$dfg'))
        self.assertEqual(sName, check_dirname(sName, 'abc:dfg'))
        self.assertEqual(sName, check_dirname(sName, 'abc#dfg'))

        self.assertEqual('abcdfg11_', check_dirname(sName, 'abcdfg11_'))

    def test_check_filename(self):
        """ Check the function check_filename. """
        sName = 'canonical.ini'
        self.assertEqual(sName, check_filename(sName, ''))
        self.assertEqual(sName, check_filename(sName, 'abc'))
        self.assertEqual(sName, check_filename(sName, 'ab/c.ini'))
        self.assertEqual(sName, check_filename(sName, 'ab$c.ini'))
        self.assertEqual(sName, check_filename(sName, r'ab\c.ini'))

        self.assertEqual('ab_c.ini', check_filename(sName, 'ab_c.ini'))
        self.assertEqual('a_bc.txt', check_filename(sName, 'a_bc.txt'))

    def test_config_read(self):
        """ Check the function config_read."""
        pass

    def test_config_path(self):
        """ Check the function config_path. """
        sHome = str(Path.home())
        tValues = config_path(sHome)
        if platform.startswith('win32') or platform.startswith('cygwin'):
            # For Windows
            pass
        else:
            self.assertEqual(tValues, (f'{sHome}/.config/YTVD',
                                       f'{sHome}/.config/YTVD/config.ini'))

    def test_prepare_space(self):
        """ Check the function prepare_space. """
        pass


if __name__ == '__main__':
    unittest.main()
