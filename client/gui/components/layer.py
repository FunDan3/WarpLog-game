from .default_component import default_component

class layer(default_component):
	components = None
	interactive = True

	def __init__(self, components = None):
		if not components:
			components = []
		self.components = components
		#In hopes of avoiding unexpected behavior
		self.position = [0, 0]
		self.size = [1980, 1080]
	def render_on(self, surface):
		for component in self.components:
			component.render_on(surface)

	def event(self, event):
		for component in self.components:
			if component.interactive:
				component.event(event)

	def on_add(self):
		for component in self.components:
			component.renderer = self.renderer

	def add_component(self, component):
		if self.renderer:
			component.renderer = self.renderer
		component.parent = self
		component.offset = self.offset
		self.components.append(component)
		component.on_added()
