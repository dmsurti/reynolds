import os

from reynolds.blockmesh.mesh_runner import MeshRunner
from reynolds.tests.test_of import TestOFCase


class TestMeshRunner(TestOFCase):
    def test_cavity_tutorial(self):
        cavity_case_dir = os.path.join(self.temp_tutorials_dir, 'incompressible', 'icoFoam',
                                       'cavity', 'cavity')
        r = MeshRunner(case_dir=cavity_case_dir)
        status, out, err = r.run()
        self.assertTrue(status)

    def fix_test_all_tutorials(self):
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
                r = MeshRunner(case_dir=possible_case_dir)
                status, out, err = r.run()
                # self.assertTrue(status)
                print('     Solving case : ' + possible_case_dir)
                if status:
                    solved += 1
                    print("      SUCCESS")
                else:
                    failed += 1
                    failed_cases.append(possible_case_dir)
                    print("      FAIL", out, err)

        print(" CASES: {}, SOLVED: {}, FAILED: {}", cases, solved, failed)
        if failed > 0:
            print(" FAILED CASE LIST: {}", *failed_cases, sep='\n')
