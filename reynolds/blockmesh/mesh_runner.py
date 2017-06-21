from subprocess import Popen


class MeshRunner(object):
    """
    Runs the blockMesh to generate the mesh for a given case.
    """
    def __init__(self, case_dir=None):
        """
        Creates a MeshRunner object for a given case directory.

        :param case_dir: The absolute path to the case directory on disk
        """
        self.case_dir = case_dir

    def run(self):
        """
        Runs the blockMesh to generate the mesh.

        :return: True, if success, False otherwise. You can inspect err when blockMesh fails.
        """
        blockmesh_proc = Popen(['blockMesh', '-case', self.case_dir])
        out, err = blockmesh_proc.communicate()
        if blockmesh_proc.poll() == 0:
            checkmesh_proc = Popen(['checkMesh', '-case', self.case_dir])
            out, err = checkmesh_proc.communicate()
            return (checkmesh_proc.poll() == 0, out, err)
        else:
            return (False, out, err)
