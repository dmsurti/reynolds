class Vertex3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dict_string(self):
        return "({} {} {})".format(self.x, self.y, self.z)


class Block(object):
    def __init__(self, vertex_labels, n_cells, grading):
        self.vertex_labels = vertex_labels
        self.n_cells = n_cells
        self.grading = grading

    def dict_string(self):
        return "hex ({}) ({}) {}".format(' '.join(str(vl) for vl in self.vertex_labels),
                                         ' '.join(str(int(n)) for n in self.n_cells),
                                         self.grading.dict_string())


class SimpleGrading(object):
    def __init__(self, exp_ratios):
        self.exp_ratios = exp_ratios

    def dict_string(self):
        return "simpleGrading ({})".format(' '.join(str(int(r)) for r in self.exp_ratios))


class Face(object):
    def __init__(self, vertex_labels):
        self.vertex_labels = vertex_labels

    def dict_string(self):
        return "({})".format(' '.join(str(vl) for vl in self.vertex_labels))


class BoundaryRegion(object):
    def __init__(self, name, type, faces):
        self.name = name
        self.type = type
        self.faces = faces

    def dict_string(self):
        face_strings = ['\t\t' + fs.dict_string() for fs in self.faces]
        ds_comps = [self.name, '{', '\ttype ' + self.type + ';', '\tfaces', '\t('] + face_strings + ['\t);', '}']
        return '\n'.join(s for s in ds_comps)
