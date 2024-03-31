from .default_component import default_component

class layer(default_component):
	components = None
	interactive = True

	def __init__(self, components = None):
		if not components:
			components = []
		self.components = components

	def render_on(self, surface):
		for component in self.components:
			component.render(surface)

	def event(self, event):
		for component in self.components:
			if component.interactive:
				component.event(event)

	def add_component(self, component):
		component.renderer = self.renderer
		component.parent = self
		component.offset = self.offset
		self.components.append(component)
