from subprocess import Popen

class MeshRunner(object):
    def __init__(self, case_dir=None):
        self.case_dir = case_dir

    def run(self):
        blockmesh_proc = Popen(['blockMesh', '-case', self.case_dir])
        out, err = blockmesh_proc.communicate()
        if blockmesh_proc.poll() == 0:
            checkmesh_proc = Popen(['checkMesh', '-case', self.case_dir])
            out, err = checkmesh_proc.communicate()
            return (checkmesh_proc.poll() == 0, out, err)
        else:
            return (False, out, err)
