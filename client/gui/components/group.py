from .layer import layer

class group(layer):
	def __init__(self, *components):
		self.components = components

	def add_components(self, *args):
		for arg in args:
			self.add_component(arg)

	def add_component(self, component):
		component.parent = self
		component.offset = self.offset
		self.components.append(component)

	def on_added(self):
		for component in self.components:
			component.renderer = self.renderer
			component.on_added()
