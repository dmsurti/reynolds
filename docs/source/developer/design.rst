==============
Package Design
==============

This project is divided into the following packages:

foam
----

The foam package is responsible to start openfoam with the environment sourced
into the target python's os.environ, so that openfoam utilities such as
blockMesh and solvers etc can be executed using a python subprocess with POpen.

This package contains a single FoamRunner class which does the above.

blockmesh
---------

The blockmesh package is responsible for generating an in-memory blockMeshDict
strucutre. It does this with a MeshDict class which delegates to various classes
such as Vertex3, Block, Face, SimpleGrading, BoundaryRegion that represent
different sections of the blockMeshDict.

You can study the `blockMeshDict specification here`_

.. _blockMeshDict specification here:
   https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

This package also handles executing the blockMesh generator. This is done with
the MeshRunner class which executes the blockMesh given a case directory. This
class runs the blockMesh in a python subprocess.


solver
------

The solver package is responsible for running any solver given the solver name.
The SolverRunner class runs a solver given it's name in a given case directory.
This class runs the solver in a python subprocess.

tests
-----

The above classes in various packages are tested and reading the test code and
`API docs`_ can be a good starting point to delve deeper into the code.

.. _API docs: ../api/reynolds.html
