==============
Using reynolds
==============

Requirements
============
* Python 3.6 or later
* OpenFoam version 4.x
* macOS 10.10 or later
* Ubuntu 14.x or later

.. _prerequisites-label:

Pre-requisites
==============

You need to install OpenFoam version 4.x on macOS or Ubuntu.

Please note that reynolds depends on an OpenFoam sparsbundle on macOS.

The following are recommended guides for installing openfoam:

* `Installing on Mac`_
* `Installing on Ubuntu`_

.. _installation-label:

Installation
============

1. Clone the repository from Github::

    git clone git@github.com:dmsurti/reynolds.git

2. Install the requirements::

    pip install -r requirements.txt

3. Run setup.py::

    python setup.py install

Starting OpenFoam
=================

To use OpenFoam in your python environment, you can use the FoamRunner class
which will source the openfoam environment variables. See the code listing
below::

   from reynolds.foam.start import FoamRunner

   foam_runner = FoamRunner()
   foam_runner.start()

This loads your environment with various openFoam utilities such as blockMesh
and various solvers so they can be executed with a python process using `POpen`.

Generating blockMeshDict
========================

To generate a blockMeshDict for the cavity tutorial, you could do::

   from reynolds.dict.parser import ReynoldsFoamDict

   block_mesh_dict = ReynoldsFoamDict('blockMeshDict.foam')
   self.assertIsNotNone(block_mesh_dict)

   # add vertices
   vertices = []
   vertices.append([0, 0, 0])
   vertices.append([1, 0, 0])
   vertices.append([1, 1, 0])
   vertices.append([0, 1, 0])
   vertices.append([0, 0, 0.1])
   vertices.append([1, 0, 0.1])
   vertices.append([1, 1, 0.1])
   vertices.append([0, 1, 0.1])
   block_mesh_dict['vertices'] = vertices

   # add blocks
   blocks = []
   blocks.append('hex')
   blocks.append([0, 1, 2, 3, 4, 5, 6, 7])
   blocks.append([20, 20, 1])
   blocks.append('simpleGrading')
   blocks.append([1, 1, 1])
   block_mesh_dict['blocks'] = blocks
   self.assertEqual(block_mesh_dict['blocks'],
                     ['hex', [0, 1, 2, 3, 4, 5, 6, 7], '(20 20 1)',
                     'simpleGrading', '(1 1 1)'])

   # add edges
   self.assertEqual(block_mesh_dict['edges'], [])
   edges = []
   edges.append('arc')
   edges.append(1)
   edges.append(5)
   edges.append([1.1, 0.0, 0.5])
   block_mesh_dict['edges'] = edges

   boundary = []
   # add moving wall
   boundary.append('movingWall')
   moving_wall = {}
   moving_wall['faces'] = [[3, 7, 6, 2]]
   moving_wall['type'] = 'wall'
   boundary.append(moving_wall)
   # add fixed walls
   boundary.append('fixedWalls')
   fixed_walls = {}
   fixed_walls['faces'] = [[0, 4, 7, 3], [2, 6, 5, 1], [1, 5, 4, 0]]
   fixed_walls['type'] = 'wall'
   boundary.append(fixed_walls)
   # add front and back
   boundary.append('frontAndBack')
   front_and_back = {}
   front_and_back['faces'] = [[0, 3, 2, 1], [4, 5, 6, 7]]
   front_and_back['type'] = 'empty'
   boundary.append(front_and_back)
   block_mesh_dict['boundary'] = boundary

   # add mergePatchPairs
   mergePatchPairs = []
   mergePatchPairs.append(['inlet1', 'outlet1'])
   mergePatchPairs.append(['inlet2', 'outlet2'])
   block_mesh_dict['mergePatchPairs'] = mergePatchPairs

   print(block_mesh_dict)

The above generates an in memory blockMeshDict. To write this to a file on disk,
you can do::

   # case_dir is the absolute path to your case directory on disk
   file_path = os.path.join(case_dir, 'system', 'blockMeshDict')

   with open(file_path, 'w') as f:
       f.write(str(block_mesh_dict))

Running a solver
================

You can run any openfoam solver available in the openfoam environment which has
been sourced, see :ref:`installation-label` instructions. For example, to run
the icoFoam solver used in the cavity tutorial, you can do::

   from reynolds.foam.cmd_runner import FoamCmdRunner

   # case_dir is the absolute path to your case directory on disk
   solver_runner = FoamCmdRunner(cmd_name='icoFoam', case_dir=cavity_case_dir)
   for info in solver_runner.run():
       pass # client can stream this info live
   if solver_runner.run_status: # All is well
       print("Success")
   else:
       print("Failure")

On exactly the same lines, you can run any other OpenFoam command such as
`blockMesh` using the `FoamCmdRunner`.

Running with Blender using Docker
=================================

You can use `Blender with an add-on that`_ invokes this reynolds API to start
openfoam, generate a blockMeshDict and run a solver.

The simplest way to run Blender with this addon is to use `this Docker file`_,
which can be installed on Ubuntu, and runs the Blender GUI with this add-on.

You can refer to the `docker image repository`_ homepage for instructional videos.

.. _Installing on Mac: https://github.com/mrklein/openfoam-os-x/wiki
.. _Installing on Ubuntu: https://openfoam.org/download/4-1-ubuntu/
.. _Blender with an add-on that: https://github.com/dmsurti/reynolds-blender
.. _this Docker file: https://github.com/dmsurti/reynolds-docker/blob/master/Dockerfile
.. _docker image repository: https://github.com/dmsurti/reynolds-docker
 

   
