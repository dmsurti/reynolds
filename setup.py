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


from distutils.core import setup

setup(
        name='reynolds',
        version='0.0.1',
        packages=['reynolds', 'reynolds.foam', 'reynolds.tests',
                  'reynolds.dict'],
        package_data={'':['**/*.json', '**/*.schema', '**/*.foam']},
        url='https://github.com/dmsurti/reynolds',
        license='GPL v3.0',
        author='Deepak Surti',
        author_email='dmsurti@gmail.com',
        description='Open source GUI for OpenFoam preprocessing'
)
