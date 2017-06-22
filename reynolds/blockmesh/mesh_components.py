#------------------------------------------------------------------------------
# Reynolds | The Preprocessing and Solver python toolbox for OpenFoam
#------------------------------------------------------------------------------
# Copyright|
#------------------------------------------------------------------------------
#     Deepak Surti       (dmsurti@gmail.com)
#     Prabhu R           (IIT Bombay, prabhu@aero.iitb.ac.in)
#     Shivasubramanian G (IIT Bombay, sgopalak@iitb.ac.in) 
#------------------------------------------------------------------------------
# License
#
#     This file is part of reynolds.
#
#     reynolds is free software: you can redistribute it and/or modify it
#     under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     reynolds is distributed in the hope that it will be useful, but WITHOUT
#     ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#     FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#     for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with reynolds.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------


class Vertex3(object):
    """
    Represents an (x, y, z) coordinate in 3D space.
    """

    def __init__(self, x, y, z):
        """
        Creates an instance of a 3D coordinate.

        :param x: The x coordinate
        :param y: The y coordinate
        :param z: The z coordinate
        """

        self.x = x
        self.y = y
        self.z = z

    def dict_string(self):
        """
        Generates a string (x, y, z) as per the vertices spec of blockMeshDict.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: A string (x, y, z)
        """
        return "({} {} {})".format(self.x, self.y, self.z)


class Block(object):
    """
    Represents a 3D region or patch of the case geometry.
    """
    def __init__(self, vertex_labels, n_cells, grading):
        """

        :param vertex_labels: A list of vertex labels identifying the vertices of the geometry in the CCW order
        :param n_cells: The number of cells in each x, y, z direction
        :param grading: The cell expansion ratios for each direction in the block
        """
        self.vertex_labels = vertex_labels
        self.n_cells = n_cells
        self.grading = grading

    def dict_string(self):
        """
        Generates a string as per the blocks spec of blockMeshDict.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: A string as per the blocks spec of blockMeshDict
        """
        return "hex ({}) ({}) {}".format(' '.join(str(vl) for vl in self.vertex_labels),
                                         ' '.join(str(int(n)) for n in self.n_cells),
                                         self.grading.dict_string())


class SimpleGrading(object):
    """
    Represents the uniform expansions in the 3 directions in the block with only 3 expansion ratios.
    """

    def __init__(self, exp_ratios):
        """
        Creates a simple grading cell expansion ratio.

        :param exp_ratios: A list [k1, k2, k3] of uniform expansions in the 3 directions
        """
        self.exp_ratios = exp_ratios

    def dict_string(self):
        """
        Generates a string as per the simpleGrading spec of blockMeshDict.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: A string simpleGrading(k1 k2 k k3)
        """
        return "simpleGrading ({})".format(' '.join(str(int(r)) for r in self.exp_ratios))


class Face(object):
    """"
    Represents a quad face belonging to a block.
    """

    def __init__(self, vertex_labels):
        """
        Creates a quad face belonging to a block.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :param vertex_labels: The list of 4 vertex labels indentifying the vertices in the face.
        """
        self.vertex_labels = vertex_labels

    def dict_string(self):
        """
        Generates a string as per the block face spec of blockMeshDict.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: A string (v1 v2 v3 v4)
        """
        return "({})".format(' '.join(str(vl) for vl in self.vertex_labels))


class BoundaryRegion(object):
    """
    Represents a region belonging to a boundary of the case geometry.
    """

    def __init__(self, name, type, faces):
        """
        Creates a boundary region.

        :param name: The name of the boundary region
        :param type: The type of the boundary region, e.g., inlet, wall, empty
        :param faces: A list of Face objects which are part of the region
        """
        self.name = name
        self.type = type
        self.faces = faces

    def dict_string(self):
        """
        Generates a string as per the boundary spec of blockMeshDict.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: A string as per the boundary spec of blockMeshDict
        """
        face_strings = ['\t\t' + fs.dict_string() for fs in self.faces]
        ds_comps = [self.name, '{', '\ttype ' + self.type + ';', '\tfaces', '\t('] + face_strings + ['\t);', '}']
        return '\n'.join(s for s in ds_comps)
