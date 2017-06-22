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


from unittest import  TestCase
from reynolds.blockmesh.mesh_dict import MeshDict
from reynolds.blockmesh.mesh_components import Vertex3, Block, SimpleGrading, BoundaryRegion, Face
import os


class TestMeshDict(TestCase):
    def setUp(self):
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
        self.block = Block(range(8), [20, 20, 1], sg)

        # movingWall region
        self.mw1 = Face([3, 7, 6, 2])
        self.mw_br = BoundaryRegion("movingWall", "wall", [self.mw1])
        # fixedWalls region
        self.fw1 = Face([0, 4, 7, 3])
        self.fw2 = Face([2, 6, 5, 1])
        self.fw3 = Face([1, 5, 4, 0])
        self.fw_br = BoundaryRegion("fixedWalls", "wall", [self.fw1, self.fw2, self.fw3])
        # frontAndBack region
        self.fb1 = Face([0, 3, 2, 1])
        self.fb2 = Face([4, 5, 6, 7])
        self.fb_br = BoundaryRegion("frontAndBack", "empty", [self.fb1, self.fb2])

        self.regions = [self.mw_br, self.fw_br, self.fb_br]

        self.mesh_dict = MeshDict(0.1, self.vertices, self.block, self.regions)

    def test_header_string(self):
        header_comps = ['FoamFile',
                        '{',
                        '\tversion\t2.0;',
                        '\tformat\tascii;',
                        '\tclass\tdictionary;',
                        '\tobject\tblockMeshDict;',
                        '}']
        header_string = '\n'.join(s for s in header_comps)
        self.assertEqual(header_string, self.mesh_dict.header_string())

    def test_vertices(self):
        vertices_comps = ['vertices', '('] + ['\t' + v.dict_string() for v in self.vertices] + [');']
        v_string = '\n'.join(s for s in vertices_comps)
        self.assertEqual(v_string, self.mesh_dict.vertices_string())

    def test_blocks(self):
        b_comps = ['blocks', '('] + ['\t' + self.block.dict_string()] + [');']
        b_string = '\n'.join(s for s in b_comps)
        self.assertEqual(b_string, self.mesh_dict.blocks_string())

    def test_boundary(self):
        mw_face_comps = ['\t\t' + f.dict_string() for f in [self.mw1]]
        mw_string_comps = ["movingWall", '{', '\ttype wall;', '\tfaces', '\t('] + mw_face_comps + ['\t);', '}']
        mw_string = '\n'.join('\t' + s for s in mw_string_comps)

        fw_face_comps = ['\t\t' + f.dict_string() for f in [self.fw1, self.fw2, self.fw3]]
        fw_string_comps = ["fixedWalls", '{', '\ttype wall;', '\tfaces', '\t('] + fw_face_comps + ['\t);', '}']
        fw_string = '\n'.join('\t' + s for s in fw_string_comps)

        fb_face_comps = ['\t\t' + f.dict_string() for f in [self.fb1, self.fb2]]
        fb_string_comps = ["frontAndBack", '{', '\ttype empty;', '\tfaces', '\t('] + fb_face_comps + ['\t);', '}']
        fb_string = '\n'.join('\t' + s for s in fb_string_comps)

        b_string_comps = ["boundary", '(', mw_string, fw_string, fb_string, ');']
        b_string = '\n'.join(s for s in b_string_comps)
        print('Expected output:\n\n' + b_string)
        self.assertEqual(b_string, self.mesh_dict.boundary_string())

    def test_edges(self):
        e_string = 'edges\n' + '(\n' + ');'
        self.assertEqual(e_string, self.mesh_dict.edges_string())

    def test_merge_pairs(self):
        m_string = 'mergePatchPairs\n' + '(\n' + ');'
        self.assertEqual(m_string, self.mesh_dict.merge_pairs_string())
