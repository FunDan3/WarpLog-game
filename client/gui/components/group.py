from .default_component import default_component

class group(default_component):
	components = None
	def __init__(self, *components):
		if not components:
			components = []
		self.components = components

	def add_component(self, component):
		self.components.append(component)

	def on_added(self):
		for component in self.components:
			self.parent.add_component(component)
