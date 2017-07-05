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

from reynolds.blockmesh.mesh_runner import MeshRunner
from reynolds.solver.solver_runner import SolverRunner
from reynolds.tests.test_of import TestOFCase

class TestSolverRunner(TestOFCase):
    def test_cavity_tutorial(self):
        cavity_case_dir = os.path.join(self.temp_tutorials_dir, 'incompressible', 'icoFoam',
                                       'cavity', 'cavity')
        r = MeshRunner(case_dir=cavity_case_dir)
        status, out, err = r.run()
        self.assertTrue(status)
        i = SolverRunner(solver_name='icoFoam', case_dir=cavity_case_dir)
        for info in i.run():
            pass # client can stream this info live
        self.assertTrue(i.run_status)
