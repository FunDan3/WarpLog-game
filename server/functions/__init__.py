import os #sync is ok cause it is one-time and before server starts

functions_folder = os.path.dirname(os.path.realpath(__file__))
for name in os.listdir(functions_folder): #import all functions
	path = f"{functions_folder}/{name}"
	if os.path.isdir(path) and not name.startswith("_"):
		exec(f"from . import {name}", globals(), locals())

del os
del name
del path
del functions_folder
