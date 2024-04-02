from .layer import layer

class group(layer):
	def __init__(self, *components):
		self.components = components

	def add_component(self, component):
		component.renderer = self.renderer
		component.parent = self
		component.offset = self.offset
		self.components.append(component)

	def on_added(self):
		for component in self.components:
			component.on_added()
