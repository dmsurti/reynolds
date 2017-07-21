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

json
----

The json package is responsible for generating an in-memory JSON object with
keys that are the attributes of the OpenFoam dict file it represents. This is
done by generating a schema using a sample JSON file for the dict file. This
schema is then updated with title and required attributes are deleted.

The class FoamDictJSONGenerator reads such a schema file and generates a JSON
object with dict attributes as it's keys.

See: `samples/blockMeshDict.json` and `schemas/blockMeshDict.schema`.

You can study the `blockMeshDict specification here`_

.. _blockMeshDict specification here:
   https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

dict
----

The dict package is responsible for generating any OpenFoam dict file, given a
JSON object which contains the data to be written in that dict file. This JSON
object is
based on a schema which represents the OpenFoam dict file to be generated.

The class FoamDictGenerator generates the OpenFoam dict file given the JSON
object and the mako template for the dict file.

See: `blockMeshDict.foam` makeo template under `dict/templates` directory to
understand how it generates a `blockMeshDict` file.

tests
-----

The above classes in various packages are tested and reading the test code and
`API docs`_ can be a good starting point to delve deeper into the code.

.. _API docs: ../api/reynolds.html
