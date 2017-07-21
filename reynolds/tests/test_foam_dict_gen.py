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


import filecmp
import os
import tempfile
from unittest import TestCase

from reynolds.json.schema_gen import FoamDictJSONGenerator
from reynolds.dict.foam_dict_gen import FoamDictGenerator


class TestBlockMeshDictGen(TestCase):
    def test_block_mesh_dict_gen(self):
        block_mesh_dict_gen = FoamDictJSONGenerator('blockMeshDict.schema')
        block_mesh_dict_json = block_mesh_dict_gen.json_obj
        self.assertIsNotNone(block_mesh_dict_json)

        # set header info
        block_mesh_dict_json['version'] = '2.0'
        block_mesh_dict_json['format'] = 'ascii'
        block_mesh_dict_json['class'] = 'dictionary'
        block_mesh_dict_json['object'] = 'blockMeshDict'

        # set convert to meters
        block_mesh_dict_json['convertToMeters'] = 0.1

        # set vertices
        block_mesh_dict_json['vertices'] = []
        block_mesh_dict_json['vertices'].append([0, 0, 0])
        block_mesh_dict_json['vertices'].append([1, 0, 0])
        block_mesh_dict_json['vertices'].append([1, 1, 0])
        block_mesh_dict_json['vertices'].append([0, 1, 0])
        block_mesh_dict_json['vertices'].append([0, 0, 0.1])
        block_mesh_dict_json['vertices'].append([1, 0, 0.1])
        block_mesh_dict_json['vertices'].append([1, 1, 0.1])
        block_mesh_dict_json['vertices'].append([0, 1, 0.1])

        # set blocks
        blocks_dict = {}
        blocks_dict['vertex_nums'] = [0, 1, 2, 3, 4, 5, 6, 7]
        blocks_dict['num_cells'] = [20, 20, 1]
        blocks_dict['grading'] = 'simpleGrading'
        blocks_dict['grading_x'] = [[1, 1, 1]]
        blocks_dict['grading_y'] = [[0.2, 0.3, 4], [0.6, 0.4, 1],
                                    [0.2, 0.3, 0.25]]
        blocks_dict['grading_z'] = [[1, 1, 1]]
        block_mesh_dict_json['blocks'] = blocks_dict

        # set boundary
        moving_wall = {}
        moving_wall['name'] = 'movingWall'
        moving_wall['type'] = 'wall'
        moving_wall['faces'] = [[3, 7, 6, 2]]

        fixed_walls = {}
        fixed_walls['name'] = 'fixedWalls'
        fixed_walls['type'] = 'wall'
        fixed_walls['faces'] = [[0, 4, 7, 3], [2, 6, 5, 1], [1, 5, 4, 0]]

        front_and_back = {}
        front_and_back['name'] = 'frontAndBack'
        front_and_back['type'] = 'empty'
        front_and_back['faces'] = [[0, 3, 2, 1], [4, 5, 6, 7]]

        patches = [moving_wall, fixed_walls, front_and_back]
        block_mesh_dict_json['boundary'] = patches

        # generate the blockMeshDict
        foam_dict_gen = FoamDictGenerator(block_mesh_dict_json,
                                          'blockMeshDict.foam')
        block_mesh_dict = foam_dict_gen.foam_dict
        print(block_mesh_dict)

        expected_dict_dir = os.path.dirname(os.path.realpath(__file__))
        expected_dict_file = os.path.join(expected_dict_dir, 'blockMeshDictSample')
        with open(expected_dict_file, 'r') as f:
            d = f.read()
            print('--------')
            print(d)
            self.maxDiff = 490
            self.assertEqual(block_mesh_dict, d)

        self.assertIsNotNone(block_mesh_dict)
