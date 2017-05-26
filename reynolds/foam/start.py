from subprocess import Popen, PIPE
import os
from os import path

class FoamRunner(object):
    def __init__(self):
        self.foam_path = path.join(path.expanduser('~'), 'OpenFOAM')
        self.source_path = path.join(self.foam_path, 'OpenFOAM-4.x', 'etc', 'bashrc')
        print(self.source_path)

    def start(self):
        foam_proc = Popen(['hdiutil', 'attach', '-mountpoint', self.foam_path,
                           'OpenFOAM.sparsebundle'], cwd=path.expanduser('~'))
        out, err = foam_proc.communicate()
        status = foam_proc.poll()
        if status == 0:
            self.shell_source(self.source_path)
            return True
        else:
            print("Could not start OpenFOAM")
            return False

    def shell_source(self, script):
        """Sometime you want to emulate the action of "source" in bash,
        settings some environment variables. Here is a way to do it."""
        pipe = Popen(". %s; env" % script, stdout=PIPE, shell=True)
        output = pipe.communicate()[0]
        env = dict((line.decode().split('=') for line in output.splitlines() if '=' in line.decode()))
        os.environ.update(env)
        print('tutorials: ', os.environ['FOAM_TUTORIALS'])
