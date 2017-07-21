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


import json
import os
import genson
import python_jsonschema_objects as pjs

class FoamDictJSONGenerator(object):
    """
    A JSON object generator for a JSON Schema representing an OpenFoam dict.

    Generates a python class with bindings for the OpenFoam dict attributes in
    JSON format.
    """
    def __init__(self, schema_filename):
        """
        Creates a JSON object generator for a given JSON Schema.

        :param schema_filename The JSON Schema file representing an OpenFoam i
        dict.

        """
        json_dir = os.path.dirname(os.path.realpath(__file__))
        json_file = os.path.join(json_dir, "schemas", schema_filename)

        schema = genson.Schema()

        with open(json_file) as f:
            data = json.load(f)
            schema.add_schema(data)

        schema_dict = schema.to_dict()

        # ----------------------------------------------
        # mako cribs about key whose name is 'class' :-(
        # ----------------------------------------------
        schema_dict['classKeyName'] = 'class'
        schema_dict.pop('required', None)

        builder = pjs.ObjectBuilder(schema_dict)
        ns = builder.build_classes()

        # if schema title ==> Blockmeshdict Sample, then:
        # namespace key for the title is: BlockmeshdictSample
        # the space chars in the title are stripped

        schema_title = schema_dict['title']
        self.json_obj = ns[schema_title.replace(' ', '')]()

