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
