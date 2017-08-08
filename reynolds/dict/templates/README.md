This directory contains all the `mako` templates for various `OpenFoam` dicts.

The `ReynoldsFoamDict` class uses the `ParsedParameterFile` from `PyFoam` to
generate an emtpy foam dict given a template dict file and the empty foam dict
is just a regular python dict, which can then be updated and finally converted
to a string representing the actual foam dict.
