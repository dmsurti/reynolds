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

from reynolds.foam.cmd_runner import FoamCmdRunner
from reynolds.tests.test_of import TestOFCase

class TestFoamRunner(TestOFCase):
    def test_icofoam_solver(self):
        cavity_case_dir = os.path.join(self.temp_tutorials_dir,
                                       'incompressible', 'icoFoam',
                                       'cavity', 'cavity')
        b = FoamCmdRunner(cmd_name='blockMesh', case_dir=cavity_case_dir)
        for info in b.run():
            pass # client can stream this info live
        self.assertTrue(b.run_status)

        i = FoamCmdRunner(cmd_name='icoFoam', case_dir=cavity_case_dir)
        for info in i.run():
            pass # client can stream this info live
        self.assertTrue(i.run_status)

    def test_block_mesh(self):
        cavity_case_dir = os.path.join(self.temp_tutorials_dir,
                                       'incompressible', 'icoFoam',
                                       'cavity', 'cavity')
        b = FoamCmdRunner(cmd_name='blockMesh', case_dir=cavity_case_dir)
        for info in b.run():
            pass # client can stream this info live
        self.assertTrue(b.run_status)

    def test_all_tutorials(self):
        cases = 0
        solved = 0
        failed = 0
        failed_cases = []

        for subdir in os.walk(self.temp_tutorials_dir):
            print(subdir)
            possible_case_dir = subdir[0]
            subdirs = subdir[1]
            if subdirs == ['0', 'constant', 'system']:
                cases += 1
                b = FoamCmdRunner(cmd_name='blockMesh',
                                  case_dir=possible_case_dir)
                for info in b.run():
                    pass # client can stream this info live
                # -------------------------------------------------------------
                # TODO: This assertion should be true for each case eventually
                # -------------------------------------------------------------
                # self.assertTrue(b.run_status)
                print('     Solving case : ' + possible_case_dir)
                if b.run_status:
                    solved += 1
                    print("      SUCCESS")
                else:
                    failed += 1
                    failed_cases.append(possible_case_dir)
                    print("      FAILED: ", possible_case_dir)

        print(" CASES: {}, SOLVED: {}, FAILED: {}".format(cases, solved,
                                                          failed))

        if failed > 0:
            print(" FAILED CASE LIST: ")
            print(*failed_cases, sep='\n')

        # -----------------------------------------------------
        # TODO: This assertion should be failed == 0 eventually
        # -----------------------------------------------------
        self.assertTrue(failed <= 30)
