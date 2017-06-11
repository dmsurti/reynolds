from subprocess import  Popen

class SolverRunner(object):
    def __init__(self, solver_name, case_dir=None):
        self.solver_name = solver_name
        self.case_dir = case_dir

    def run(self):
        solver_proc = Popen([self.solver_name, '-case', self.case_dir])
        out, err = solver_proc.communicate()
        if solver_proc.poll() == 0:
            return (True, out, err)
        else:
            return (False, out, err)