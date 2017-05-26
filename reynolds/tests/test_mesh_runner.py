from unittest import TestCase
from reynolds.blockmesh.mesh_runner import MeshRunner
from reynolds.foam.start import FoamRunner
from distutils.dir_util import  copy_tree, remove_tree
from tempfile import mkdtemp
import os

class TestMeshRunner(TestCase):
    def setUp(self):
        self.foam_runner = FoamRunner()
        self.foam_runner.start()
        self.tutorials_dir = os.environ['FOAM_TUTORIALS']
        self.temp_tutorials_dir = mkdtemp()
        print(self.temp_tutorials_dir)
        copy_tree(self.tutorials_dir, self.temp_tutorials_dir)
        self.ignore = ['Allclean', 'Allrun', 'Alltest', 'resources']
        print(os.listdir(self.temp_tutorials_dir))

    def test_cavity_tutorial(self):
        cavity_case_dir = os.path.join(self.temp_tutorials_dir, 'incompressible', 'icofoam',
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


    def tearDown(self):
        remove_tree(self.temp_tutorials_dir)
