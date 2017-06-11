import os
from distutils.dir_util import copy_tree, remove_tree
from tempfile import mkdtemp
from unittest import TestCase

from reynolds.foam.start import FoamRunner


class TestOFCase(TestCase):
    def setUp(self):
        self.foam_runner = FoamRunner()
        self.foam_runner.start()
        self.tutorials_dir = os.environ['FOAM_TUTORIALS']
        self.temp_tutorials_dir = mkdtemp()
        print(self.temp_tutorials_dir)
        copy_tree(self.tutorials_dir, self.temp_tutorials_dir)
        self.ignore = ['Allclean', 'Allrun', 'Alltest', 'resources']
        print(os.listdir(self.temp_tutorials_dir))

    def tearDown(self):
        remove_tree(self.temp_tutorials_dir)