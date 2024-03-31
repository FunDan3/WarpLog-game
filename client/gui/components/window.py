from .layer import layer
from .. import exceptions
import pygame

class window(layer): #doesnt offset because it is part of UI
	position = None # [x_pos, y_pos]
	color = None #[red, green, blue]
	size = None # [x_size, y_size]

	border = None #[x_pos, y_pos, x_size, y_size]
	border_color = None

	def __init__(self, position, size, border_size = 2, border_color = None, color = None, components = None):
		if not components:
			components = []
		if not color:
			color = [128] * 3
		if not border_color:
			border_color = [255] * 3
		self.color = color
		self.border_color = border_color

		self.components = components
		self.position = position
		self.size = size
		self.border = [
			position[0] - border_size,
			position[1] - border_size,
			size[0] + border_size*2,
			size[1] + border_size*2]

	def add_component(self, component):
		component.renderer = self.renderer
		component.parent = self
		component.offset = [self.position[0] + self.offset[0], self.position[1] + self.offset[1]]
		self.components.append(component)

	def render_on(self, surface):
		pygame.draw.rect(surface, self.border_color, self.border)
		window_surface = pygame.Surface(self.size)
		window_surface.fill(self.color)
		for component in self.components:
			component.render_on(window_surface)
		surface.blit(window_surface, self.position)
