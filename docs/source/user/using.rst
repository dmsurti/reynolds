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

2. Run setup.py::

    python setup.py install

Starting OpenFoam
=================

To use OpenFoam in your python environment, you can use the FoamRunner class which will source the openfoam environment variables. See the code listing below::

   from reynolds.foam.start import FoamRunner

   foam_runner = FoamRunner()
   foam_runner.start()

This loads your environment with various openFoam utilities such as blockMesh and various solvers so they can be executed with a python process using `POpen`.

Generating blockMeshDict
========================

To generate a blockMeshDict for the cavity tutorial, you could do::

   from reynolds.blockmesh.mesh_dict import MeshDict
   from reynolds.blockmesh.mesh_components import (Vertex3, Block,
     SimpleGrading, BoundaryRegion, Face)

   
   v0 = Vertex3(0, 0, 0)
   v1 = Vertex3(1, 0, 0)
   v2 = Vertex3(1, 1, 0)
   v3 = Vertex3(0, 1, 0)
   v4 = Vertex3(0, 0, 0.1)
   v5 = Vertex3(1, 0, 0.1)
   v6 = Vertex3(1, 1, 0.1)
   v7 = Vertex3(0, 1, 0.1)
   self.vertices = [v0, v1, v2, v3, v4, v5, v6, v7]

   sg = SimpleGrading([1, 1, 1])
   block = Block(range(8), [20, 20, 1], sg)

   # movingWall region
   mw1 = Face([3, 7, 6, 2])
   mw_br = BoundaryRegion("movingWall", "wall", [self.mw1])

   # fixedWalls region
   fw1 = Face([0, 4, 7, 3])
   fw2 = Face([2, 6, 5, 1])
   fw3 = Face([1, 5, 4, 0])
   fw_br = BoundaryRegion("fixedWalls", "wall", [fw1, fw2, fw3])

   # frontAndBack region
   self.fb1 = Face([0, 3, 2, 1])
   self.fb2 = Face([4, 5, 6, 7])
   self.fb_br = BoundaryRegion("frontAndBack", "empty", [fb1, fb2])

   self.regions = [mw_br, fw_br, fb_br]

   self.mesh_dict = MeshDict(0.1, vertices, block, regions)

The above generates an in memory blockMeshDict. To write this to a file on disk,
you can do::

   # case_dir is the absolute path to your case directory on disk
   file_path = os.path.join(case_dir, 'system', 'blockMeshDict')

   with open(file_path, 'w') as f:
       f.write(mesh_dict.dict_string)

Running a solver
================

You can run any openfoam solver available in the openfoam environment which has
been sourced, see :ref:`installation-label` instructions. For example, to run
the icoFoam solver used in the cavity tutorial, you can do::

   from reynolds.solver.solver_runner import SolverRunner

   # case_dir is the absolute path to your case directory on disk
   solver_runner = SolverRunner(solver_name='icoFoam', case_dir=case_dir)
   status, out, err = sovler_runner.run()
   # if all is well, status will be True
   if not status:
       print("Whoops, solving failed!")

Running with Blender using Docker
=================================

You can use `Blender with an add-on that`_ invokes this reynolds API to start openfoam, generate a blockMeshDict and run a solver. 

The simplest way to run Blender with this addon is to use `this Docker file`_, which
can be installed on Ubuntu, and runs the Blender GUI with this add-on.

You can refer to the `docker image repository`_ homepage for instructional videos.

.. _Installing on Mac: https://github.com/mrklein/openfoam-os-x/wiki
.. _Installing on Ubuntu: https://openfoam.org/download/4-1-ubuntu/
.. _Blender with an add-on that: https://github.com/dmsurti/reynolds-blender
.. _this Docker file: https://github.com/dmsurti/reynolds-docker/blob/master/Dockerfile
.. _docker image repository: https://github.com/dmsurti/reynolds-docker
 

   
