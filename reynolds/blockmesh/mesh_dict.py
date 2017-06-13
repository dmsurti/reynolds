class MeshDict(object):
    def __init__(self, convert_to_meters, vertices, block, regions, edges=None, mergePairs=None):
        self.convert_to_meters = convert_to_meters
        self.vertices = vertices
        self.block = block
        self.regions = regions
        self.edges = edges
        self.mergePairs = mergePairs

    def header_string(self):
        header_comps = ['FoamFile',
                        '{',
                        '\tversion\t2.0;',
                        '\tformat\tascii;',
                        '\tclass\tdictionary;',
                        '\tobject\tblockMeshDict;',
                        '}']
        return '\n'.join(s for s in header_comps)

    def meters_string(self):
        return 'convertToMeters {};'.format(self.convert_to_meters)

    def vertices_string(self):
        vertices_comps = ['vertices', '('] + ['\t' + v.dict_string() for v in self.vertices] + [');']
        return '\n'.join(s for s in vertices_comps)

    def blocks_string(self):
        b_comps = ['blocks', '('] + ['\t' + self.block.dict_string()] + [');']
        return '\n'.join(s for s in b_comps)

    def boundary_string(self):
        r_comps = ['\t' + r1 for r in self.regions for r1 in r.dict_string().split('\n')]
        b_comps = ["boundary", '('] + r_comps + [');']
        return '\n'.join(br for br in b_comps)

    #TODO: Implement dict string for edges as a mesh component
    def edges_string(self):
        e_comps = ['edges', '('] + [');']
        return '\n'.join(s for s in e_comps)

    # TODO: Implement dict string for mergePatchPairs as a mesh component
    def merge_pairs_string(self):
        e_comps = ['mergePatchPairs', '('] + [');']
        return '\n'.join(s for s in e_comps)

    def dict_string(self):
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