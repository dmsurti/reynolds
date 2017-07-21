This directory contains sample json files for various dicts in `OpenFoam` to
generate JSON Schemas from these files using `genson` as such on the command
line:

```
cd <to-clone-repo-dir>/reynolds/json
genson -i 2 samples/sample.json > schemas/sample.schema
```

You can then modify the sample.schema to remove all the required properties, add
a title attribute and making any other changes.

This schema is used by `FoamDictJSONGenerator` class to auto generate a python
class with bindings for a JSON instance for this schema, using
`python_jsonschema_objects` library.