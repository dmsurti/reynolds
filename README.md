Reynolds
========

[![Build
Status](https://travis-ci.org/dmsurti/reynolds.svg?branch=master)](https://travis-ci.org/dmsurti/reynolds)
[![Documentation Status](https://readthedocs.org/projects/reynolds/badge/?version=latest)](http://reynolds.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/dmsurti/reynolds/branch/master/graph/badge.svg)](https://codecov.io/gh/dmsurti/reynolds)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

**Reynolds** is a full featured, scriptable python API of components for the
preprocessing and the solver environments of
[OpenFoam](http://www.openfoam.com). These components can be easily combined
to build a GUI using any 3D graphics package such as VTK, Blender etc.

Integration with Blender
---

For a reference integration of these components, check out the [Blender
integration](https://github.com/dmsurti/reynolds-blender).

Running with docker container on Ubuntu
---

Please refer to [reynolds-docker](https://github.com/dmsurti/reynolds-docker)
repository for instructions to build a docker image and run the container with
the Blender addon to solve the cavity case tutorial.

Documentation
---

* [User and Developer Docs](http://reynolds.readthedocs.io/en/latest/)
* [API Docs](http://reynolds.readthedocs.io/en/latest/#api-docs)

License
---

reynolds is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. See the file [LICENSE](LICENSE.md) in this directory or
[[http://www.gnu.org/licenses/]], for a description of the GNU General Public
License terms under which you can copy the files.

Author
---

[Deepak Surti](https://github.com/dmsurti)

Contributing
---

To contribute to reynolds:

* Please open an issue describing the bug, enhancement or any other improvement.
* If possible, please supply the case directory that can help demonstrate the issue.
* If the design involves a larger refactor, please open a issue to dicuss the refactor.
* After discussion on the issue, you can submit a Pull Request by forking this project.
* Please accompany your Pull Request with updates to test code.