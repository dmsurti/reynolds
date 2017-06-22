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


class MeshDict(object):
    """
    An in-memory represenation of blockMeshDict.

    """
    def __init__(self, convert_to_meters, vertices, block, regions, edges=None, mergePairs=None):
        """

        :param convert_to_meters: The convert to meters value
        :param vertices: The list of Vertex objects
        :param block: The Block object
        :param regions: The list of BoundaryRegion objects
        :param edges: The list of edges (TBD)
        :param mergePairs: The list of mergePairs (TBD)
        """
        self.convert_to_meters = convert_to_meters
        self.vertices = vertices
        self.block = block
        self.regions = regions
        self.edges = edges
        self.mergePairs = mergePairs

    def header_string(self):
        """
        Generates a header string as per the blockMeshDict specs.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return:  A header string
        """
        header_comps = ['FoamFile',
                        '{',
                        '\tversion\t2.0;',
                        '\tformat\tascii;',
                        '\tclass\tdictionary;',
                        '\tobject\tblockMeshDict;',
                        '}']
        return '\n'.join(s for s in header_comps)

    def meters_string(self):
        """
        Generate the convertToMeters string as per the blockMeshDict specs.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: The string `convertToMeters     value`
        """
        return 'convertToMeters {};'.format(self.convert_to_meters)

    def vertices_string(self):
        """
        Generate the vertices string as per the blockMeshDict specs.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: The vertices string
        """
        vertices_comps = ['vertices', '('] + ['\t' + v.dict_string() for v in self.vertices] + [');']
        return '\n'.join(s for s in vertices_comps)

    def blocks_string(self):
        """
        Generate the blocks string as per the blockMeshDict specs.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: The blocks string
        """
        b_comps = ['blocks', '('] + ['\t' + self.block.dict_string()] + [');']
        return '\n'.join(s for s in b_comps)

    def boundary_string(self):
        """
        Generate the boundary string as per the blockMeshDict specs.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: The boundary string
        """
        r_comps = ['\t' + r1 for r in self.regions for r1 in r.dict_string().split('\n')]
        b_comps = ["boundary", '('] + r_comps + [');']
        return '\n'.join(br for br in b_comps)


    def edges_string(self):
        """
        #TODO: Implement dict string for edges as a mesh component

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: The edges string
        """
        e_comps = ['edges', '('] + [');']
        return '\n'.join(s for s in e_comps)

    def merge_pairs_string(self):
        """
        # TODO: Implement dict string for mergePatchPairs as a mesh component

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return: The mergePairs string
        """
        e_comps = ['mergePatchPairs', '('] + [');']
        return '\n'.join(s for s in e_comps)

    def dict_string(self):
        """
        Generates a complete blockMeshDict string as per the blockMeshDict specs.

        See: https://cfd.direct/openfoam/user-guide/blockMesh/#x25-1750005.3

        :return:  A blockMeshDict string, which can be written to a blockMeshDict file on disk
        """
        d_comps = [self.header_string(),
                   '\n',
                   self.meters_string(),
                   '\n',
                   self.vertices_string(),
                   '\n',
                   self.blocks_string(),
                   '\n',
                   self.edges_string(),
                   '\n',
                   self.boundary_string(),
                   '\n',
                   self.merge_pairs_string()]
        return '\n'.join(s for s in d_comps)
