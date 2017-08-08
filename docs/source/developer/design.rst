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

This package also provides a class FoamCmdRunner which is used to execute any
OpenFoam command that is sourced after starting OpenFoam. The command runner
class requires the command name and the case directory in which to execute the
command.

Both the starter and the runner class emit the progress which can be `yield`ed
in the client code that uses these. For a sample, see the
`tests/test_foam_cmd_runner.py`.

dict
----

The dict package is responsible for reading/writing any OpenFoam dict file.

The class `ReynoldsFoamDict` uses `PyFoam` provided `ParsedParameterFile` to
read and write foam dicts. You need to initialize a `ReynoldsFoamDict` with a
template for the foam dict you want to read/write. The templates are availabel
in `dict/templates` directory.

The requirement of a template dict file is because ParsedParameterFile cannot be
intialized without a foam dict file and so we use the template to start with an
initial, empty foam dict.

See: `blockMeshDict.foam` template under `dict/templates`.

tests
-----

The above classes in various packages are tested and reading the test code and
`API docs`_ can be a good starting point to delve deeper into the code.

.. _API docs: ../api/reynolds.html
