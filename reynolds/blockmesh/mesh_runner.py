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


from subprocess import Popen


class MeshRunner(object):
    """
    Runs the blockMesh to generate the mesh for a given case.
    """
    def __init__(self, case_dir=None):
        """
        Creates a MeshRunner object for a given case directory.

        :param case_dir: The absolute path to the case directory on disk
        """
        self.case_dir = case_dir

    def run(self):
        """
        Runs the blockMesh to generate the mesh.

        :return: True, if success, False otherwise. You can inspect err when blockMesh fails.
        """
        blockmesh_proc = Popen(['blockMesh', '-case', self.case_dir])
        out, err = blockmesh_proc.communicate()
        if blockmesh_proc.poll() == 0:
            checkmesh_proc = Popen(['checkMesh', '-case', self.case_dir])
            out, err = checkmesh_proc.communicate()
            return (checkmesh_proc.poll() == 0, out, err)
        else:
            return (False, out, err)
