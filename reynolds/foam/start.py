from subprocess import Popen, PIPE
import os
from sys import platform
from os import path

class FoamRunner(object):
    def __init__(self):
        if platform == "linux" or platform == "linux2":
            self.foam_path = path.join("/", "opt", "openfoam4")
            self.source_path = path.join(self.foam_path, 'etc', 'bashrc')
        elif platform == "darwin":
            self.foam_path = path.join(path.expanduser('~'), 'OpenFOAM')
            self.source_path = path.join(self.foam_path, 'OpenFOAM-4.x', 'etc', 'bashrc')
        else:
            raise AssertionError("Unsupported platform: ", platform)
        print(self.source_path)


    def start(self):
        if platform == "linux" or platform == "linux2":
            self.shell_source(self.source_path)
            return True
        elif platform == "darwin":
            foam_proc = Popen(['hdiutil', 'attach', '-mountpoint', self.foam_path,
                               'OpenFOAM.sparsebundle'], cwd=path.expanduser('~'))
            out, err = foam_proc.communicate()
            status = foam_proc.poll()
            if status == 0:
                print("Source openfoam env vars...")
                self.shell_source(self.source_path)
                return True
            else:
                print("Could not start OpenFOAM")
                return False
        else:
            raise AssertionError("Unsupported platform: ", platform)


    def shell_source(self, script):
        """Sometime you want to emulate the action of "source" in bash,
        settings some environment variables. Here is a way to do it."""
        pipe = Popen(". %s; env" % script, stdout=PIPE, shell=True)
        output = pipe.communicate()[0]
        env = dict((line.decode().split('=', 1) for line in output.splitlines()
                    if '=' in line.decode()))
        os.environ.update(env)
        print('tutorials: ', os.environ['FOAM_TUTORIALS'])

if __name__ == '__main__':
    fr = FoamRunner()
    fr.start()
