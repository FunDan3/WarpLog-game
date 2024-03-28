from .default_component import default_component

class layer(default_component):
	components = None
	interactive = True
	def __init__(self, components = None):
		if not components:
			components = []
		self.components = components
	def render(self, screen):
		for component in components:
			component.render(screen)
	def event(self, event):
		for component in components:
			if component.interactable:
				component.event(event)
	def add_component(self, component):
		component.renderer = self.renderer
		component.parent = self
		self.components.append(component)
