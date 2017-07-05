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
from os import path
from subprocess import PIPE, Popen
from sys import platform


class FoamRunner(object):
    """
    A class to start the OpenFoam runtime environment.

    This works by loading the openfoam env variables into the python os.environ thereby
    allowing openfoam tools such as blockMesh and various solvers to be executed using a python process.

    This is a platform dependent class that supports linux and macOS only as the process of loading openfoam env
    variables is different on the two supported platforms.

    """
    def __init__(self):
        """
        Initializes the runner with:

        1. Foam path: which is path to the openfoam installation
        2. Source path: which is the path to the openfoam bash script to source openfoam env variables.

        The foam path and source path are setup as per the os platform.
        """
        if platform == "linux" or platform == "linux2":
            self.foam_path = path.join("/", "opt", "openfoam4")
            self.source_path = path.join(self.foam_path, 'etc', 'bashrc')
        elif platform == "darwin":
            self.foam_path = path.join(path.expanduser('~'), 'OpenFOAM')
            self.source_path = path.join(self.foam_path, 'OpenFOAM-4.x', 'etc', 'bashrc')
        else:
            raise AssertionError("Unsupported platform: ", platform)
        print(self.source_path)

    def start(self):
        """
        Starts the openfoam environment as such on the following os platforms:

        1. macOS: Loads the openfoam sparsebundle and sources the openfoam env variables.
        2. linux: Sources the openfoam env variables.

        :return: True if the process was successful, else False on macOs and linux
                 AssertionError for any other non supported os platform.
        """
        if platform == "linux" or platform == "linux2":
            self.shell_source(self.source_path)
            return True
        elif platform == "darwin":
            foam_proc = Popen(['hdiutil', 'attach', '-mountpoint', self.foam_path,
                               'OpenFOAM.sparsebundle'], cwd=path.expanduser('~'))
            out, err = foam_proc.communicate()
            status = foam_proc.poll()
            if status == 0 and self.shell_source(self.source_path):
                print("Started Openfoam and Sourced openfoam env vars...")
                return True
            else:
                print("Could not start OpenFOAM")
                return False
        else:
            raise AssertionError("Unsupported platform: ", platform)

    def shell_source(self, script):
        """
        Updates the environment with variables sourced from openfoam bash script.

        :param script: The path to the openform etc/bashrc script to be sourced

        :return: True if env sourced succesfully. False otherwise.
        """
        pipe = Popen(". %s; env" % script, stdout=PIPE, shell=True)
        output = pipe.communicate()[0]
        env = dict((line.decode().split('=', 1) for line in output.splitlines() if '=' in line.decode()))
        os.environ.update(env)
        print('tutorials: ', os.environ['FOAM_TUTORIALS'])
        return bool(env)


if __name__ == '__main__':
    fr = FoamRunner()
    fr.start()
