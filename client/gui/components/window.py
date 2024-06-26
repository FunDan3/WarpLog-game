from .layer import layer
from .. import exceptions
from .. import components
import pygame

class window(layer): #doesnt offset because it is part of UI
	position = None # [x_pos, y_pos]
	filler_color = None #[red, green, blue]
	size = None # [x_size, y_size]

	border = None #[x_pos, y_pos, x_size, y_size]
	border_color = None

	closable = None
	close_button = None
	def __init__(self, position, size, border_size = 2, border_color = None, filler_color = None, components = None, closable = True):
		if not components:
			components = []
		if not filler_color:
			filler_color = [64] * 3
		if not border_color:
			border_color = [255] * 3
		self.filler_color = filler_color
		self.border_color = border_color

		self.closable = closable
		self.components = components
		self.position = position
		self.size = size
		self.border = [
			position[0] - border_size,
			position[1] - border_size,
			size[0] + border_size*2,
			size[1] + border_size*2]

	def close(self):
		self.visible = False
		self.interactive = False
		if self.close_button:
			self.close_button.visible = False
			self.close_button.interactive = False

	def on_added(self):
		for component in self.components:
			component.renderer = self.renderer
		if self.closable:
			x_size = 24
			x_border_size = 4
			x_image = pygame.Surface((x_size, x_size))
			pygame.draw.rect(x_image, (255, 255, 255), ((x_size-x_size/4)//2, 0, x_size//4, x_size))
			pygame.draw.rect(x_image, (255, 255, 255), (0, (x_size-x_size/4)//2, x_size, x_size//4))
			x_image = pygame.transform.rotate(x_image, 45)
			if self.closable:
				self.close_button = components.image_button(image = x_image, on_click = self.close, position = [self.position[0] + self.size[0]-x_size//2-x_border_size, self.position[1]-x_size//2-x_border_size], border_size = x_border_size)

			self.parent.add_component(self.close_button, bypass_layer_check = True)

	def add_components(self, *args):
		for arg in args:
			self.add_component(arg)

	def add_component(self, component):
		if self.renderer:
			component.renderer = self.renderer
		component.parent = self
		component.offset = [self.position[0] + self.offset[0], self.position[1] + self.offset[1]]
		self.components.append(component)
		component.on_added()

	def render_on(self, surface):
		pygame.draw.rect(surface, self.border_color, self.border)
		window_surface = pygame.Surface(self.size)
		window_surface.fill(self.filler_color)
		for component in self.components:
			component.render_on(window_surface)
		surface.blit(window_surface, self.position)
