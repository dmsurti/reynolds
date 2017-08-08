import unittest

from reynolds.dict.parser import ReynoldsFoamDict

class TestReynoldsFoamDict(unittest.TestCase):
    def test_blockmesh_dict(self):
        block_mesh_dict = ReynoldsFoamDict('blockMeshDict.foam')
        self.assertIsNotNone(block_mesh_dict)

        # check vertices
        self.assertEqual(block_mesh_dict['vertices'], [])
        vertices = []
        vertices.append([0, 0, 0])
        vertices.append([1, 0, 0])
        vertices.append([1, 1, 0])
        vertices.append([0, 1, 0])
        vertices.append([0, 0, 0.1])
        vertices.append([1, 0, 0.1])
        vertices.append([1, 1, 0.1])
        vertices.append([0, 1, 0.1])

        # check blocks
        block_mesh_dict['vertices'] = vertices
        self.assertEqual(block_mesh_dict['vertices'],
                         ['(0 0 0)', '(1 0 0)', '(1 1 0)', '(0 1 0)',
                          '(0 0 0.1)', '(1 0 0.1)', '(1 1 0.1)', '(0 1 0.1)'])
        self.assertEqual(block_mesh_dict['blocks'], [])
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

        # check edges
        self.assertEqual(block_mesh_dict['edges'], [])
        edges = []
        edges.append('arc')
        edges.append(1)
        edges.append(5)
        edges.append([1.1, 0.0, 0.5])
        block_mesh_dict['edges'] = edges
        self.assertEqual(block_mesh_dict['edges'],
                         ['arc', 1, 5, '(1.1 0.0 0.5)'])

        # check boundary
        self.assertEqual(block_mesh_dict['boundary'], [])
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
        self.assertEqual(block_mesh_dict['boundary'], boundary)

        # check mergePatchPairs
        self.assertEqual(block_mesh_dict['mergePatchPairs'], [])
        mergePatchPairs = []
        mergePatchPairs.append(['inlet1', 'outlet1'])
        mergePatchPairs.append(['inlet2', 'outlet2'])
        block_mesh_dict['mergePatchPairs'] = mergePatchPairs
        self.assertEqual(block_mesh_dict['mergePatchPairs'], mergePatchPairs)

        print(block_mesh_dict)
