#!/usr/bin/python
# coding: utf-8

r"""Importing single shape from IGES"""

from __future__ import print_function

import logging

import OCC.Display.SimpleGui

import aocutils.display.topology
import aocutils.display.defaults

import aocxchange.iges
import aocxchange.utils

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s :: %(levelname)6s :: %(module)20s :: %(lineno)3d :: %(message)s')

backend = aocutils.display.defaults.backend
display, start_display, add_menu, add_function_to_menu = OCC.Display.SimpleGui.init_display(backend)

# my_iges_importer = occaddons.dataexchange.iges.IgesImporter("../../data/IGES/splines.igs")
filename = aocxchange.utils.path_from_file(__file__, "./models_in/iges/aube_pleine.iges")
iges_importer = aocxchange.iges.IgesImporter(filename)

print(iges_importer.nb_shapes)  # 13
print(len(iges_importer.shapes))  # 13


the_compound = iges_importer.compound
# display.DisplayShape(the_compound)

# there are no shells or solids in the compound (IGES specific)
aocutils.display.topology.faces(display, iges_importer.compound)


display.FitAll()
display.View_Iso()
start_display()
