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
        status, out, err = i.run()
        self.assertTrue(status)
