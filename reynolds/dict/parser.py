#------------------------------------------------------------------------------
# Reynolds | The Preprocessing and Solver python toolbox for OpenFoam
#------------------------------------------------------------------------------
# Copyright|
#------------------------------------------------------------------------------
#     Deepak Surti       (dmsurti@gmail.com)
#     Prabhu R           (IIT Bombay, prabhu@aero.iitb.ac.in)
#     Shivasubramanian G (IIT Bombay, sgopalak@iitb.ac.in) 
#------------------------------------------------------------------------------
# License
#
#     This file is part of reynolds.
#
#     reynolds is free software: you can redistribute it and/or modify it
#     under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     reynolds is distributed in the hope that it will be useful, but WITHOUT
#     ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#     FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#     for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with reynolds.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------


import os

from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile

class ReynoldsFoamDict(dict):
    """
    Read and write any foam dictionary, using python dictionary.
    """
    def __init__(self, dict_template_filename, solver_name=None):
        """
        Creates an inital empty python dictionary for a given foam dict.

        :param dict_template_filname: The foam dict template filename
        """
        templates_root_dir = os.path.dirname(os.path.realpath(__file__))
        if solver_name:
            template_file = os.path.join(templates_root_dir,
                                         'templates', solver_name,
                                         dict_template_filename)
        else:
            template_file = os.path.join(templates_root_dir,
                                         'templates', dict_template_filename)

        self.__foam_dict__ = ParsedParameterFile(template_file)

    def __convert(self, element, parent=None):
        """
        Converts the value for a foam dict key to the correct format.

        The rules of conversion are:
        1. Any nested list of size 3 is converted to : '(1 2 3)' string.
        2. Any nested list of size != 3 is retained as a list.
        3. A dict is retained as a dict.
        4. A single value element is retained as a single value.
        5. A list not nested is convered to: '[1 2 3]' string.
        """
        if isinstance(element, list):
            if parent:
                if len(element) == 3 and not(any(isinstance(e, list)
                                                 for e in element)):
                    return '(' + ' '.join(self.__convert(e, element)
                                          for e in element) + ')'
                else:
                    return [self.__convert(e, element) for e in element]
            else:
                if all(not hasattr(e, '__iter__') for e in element):
                    return '[' + ' '.join(str(e) for e in element) + ']'
                else:
                    return [self.__convert(e, element) for e in element]

        if isinstance(element, dict):
            return element

        if isinstance(parent, list) and len(parent) == 3:
            return str(element)
        else:
            return element

    # ------------
    # emulate dict
    # ------------
    def __getitem__(self, key):
        return self.__foam_dict__[key]

    def __setitem__(self, key, item):
        self.__foam_dict__[key] = self.__convert(item)

    def __str__(self):
        return str(self.__foam_dict__)
