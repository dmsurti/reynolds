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


from subprocess import PIPE, Popen


class FoamCmdRunner(object):
    """
    Runs the foam command given the cmd name for a given case.

    """
    def __init__(self, cmd_name, case_dir=None, cmd_flags=[]):
        """
        Creates a foam command runner for a given command with a case directory.

        :param cmd_name: The command name, with correct case
        :param case_dir: The absolute path to the case directory on disk
        """
        self.cmd_name = cmd_name
        self.case_dir = case_dir
        self.cmd_flags = cmd_flags
        self.run_status = False

    def run_command(self):
        """
        Runs the command in the case directory.

        :return: True, if solving succeeds, False otherwise.
        """
        with Popen([self.cmd_name] + self.cmd_flags + ['-case', self.case_dir],
                   stdout=PIPE,
                   bufsize=1,
                   universal_newlines=True) as p:
            for info in p.stdout:
                lines = info.splitlines()
                for line in lines:
                    if len(line) > 0 and not line.isspace():
                        yield line.rstrip('\n')
        return p.returncode == 0

    def run(self):
        """
        Runs the solver and stores the status of the run.
        """
        self.run_status = False # Reset a previous run status
        self.run_status = yield from self.run_command()
