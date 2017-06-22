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


from subprocess import  Popen


class SolverRunner(object):
    """
    Runs the solver given a solver name for a given case.

    """
    def __init__(self, solver_name, case_dir=None):
        """
        Creates a solver runner for a given solver with a case directory.

        :param solver_name: The solver name, with correct case
        :param case_dir: The absolute path to the case directory on disk
        """
        self.solver_name = solver_name
        self.case_dir = case_dir

    def run(self):
        """
        Runs the solver in the case directory.

        :return: True, if solving succeeds, False otherwise. You can inspect err if solving fails.
        """
        solver_proc = Popen([self.solver_name, '-case', self.case_dir])
        out, err = solver_proc.communicate()
        if solver_proc.poll() == 0:
            return (True, out, err)
        else:
            return (False, out, err)
