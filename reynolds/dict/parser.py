import os

from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile

class ReynoldsFoamDict(dict):
    def __init__(self, dict_template_filename):
        templates_root_dir = os.path.dirname(os.path.realpath(__file__))
        template_file = os.path.join(templates_root_dir,
                                     'templates', dict_template_filename)
        self.__foam_dict__ = ParsedParameterFile(template_file)

    def __convert(self, element, parent=None):
        if isinstance(element, list):
            if parent:
                if len(element) == 3 and not(any(isinstance(e, list)
                                                 for e in element)):
                    return '(' + ' '.join(self.__convert(e, element)
                                          for e in element) + ')'
                else:
                    return [self.__convert(e, element) for e in element]
            else:
                if all(not hasattr(e, '__iter__') for e in element):
                    return '[' + ' '.join(str(e) for e in element) + ']'
                else:
                    return [self.__convert(e, element) for e in element]

        if isinstance(element, dict):
            return element

        if isinstance(parent, list) and len(parent) == 3:
            return str(element)
        else:
            return element

    def __getitem__(self, key):
        return self.__foam_dict__[key]

    def __setitem__(self, key, item):
        self.__foam_dict__[key] = self.__convert(item)

    def __str__(self):
        return str(self.__foam_dict__)
