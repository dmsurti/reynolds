from distutils.core import setup

setup(
        name='reynolds',
        version='0.0.1',
        packages=['reynolds', 'reynolds.foam', 'reynolds.tests', 'reynolds.solver', 'reynolds.blockmesh'],
        url='https://github.com/dmsurti/reynolds',
        license='GPL v3.0',
        author='Deepak Surti',
        author_email='dmsurti@gmail.com',
        description='Open source GUI for OpenFoam preprocessing'
)
