import os #sync is ok cause it is one-time and before server starts

components_folder = os.path.dirname(os.path.realpath(__file__))
for name in os.listdir(components_folder): #import all components
	path = f"{components_folder}/{name}"
	if os.path.isdir(path) and not name.startswith("_"):
		exec(f"from . import {name}", globals(), locals())

del os
del name
del path
del components_folder
