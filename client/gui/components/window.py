from .layer import layer
from .. import exceptions
from .. import components
import pygame

class window(layer): #doesnt offset because it is part of UI
	position = None # [x_pos, y_pos]
	color = None #[red, green, blue]
	size = None # [x_size, y_size]

	border = None #[x_pos, y_pos, x_size, y_size]
	border_color = None

	closable = True
	close_button = None
	def __init__(self, position, size, border_size = 2, border_color = None, color = None, components = None, closable = True):
		if not components:
			components = []
		if not color:
			color = [64] * 3
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

	def close(self):
		self.visible = False
		self.interactive = False
		if self.close_button:
			self.close_button.visible = False
			self.close_button.interactive = False

	def on_added(self):
		if self.closable:
			x_size = 32
			x_border_size = 6
			x_image = pygame.Surface((x_size, x_size))
			pygame.draw.rect(x_image, (255, 255, 255), ((x_size-x_size/4)//2, 0, x_size//4, x_size))
			pygame.draw.rect(x_image, (255, 255, 255), (0, (x_size-x_size/4)//2, x_size, x_size//4))
			x_image = pygame.transform.rotate(x_image, 45)
			self.close_button = components.image_button(image = x_image, on_click = self.close, position = [self.position[0] + self.size[0]-x_size//2-x_border_size, self.position[1]-x_size//2-x_border_size], border_size = x_border_size)

			self.parent.add_component(self.close_button, bypass_layer_check = True)


	def add_component(self, component):
		component.renderer = self.renderer
		component.parent = self
		component.offset = [self.position[0] + self.offset[0], self.position[1] + self.offset[1]]
		self.components.append(component)
		component.on_added()

	def render_on(self, surface):
		pygame.draw.rect(surface, self.border_color, self.border)
		window_surface = pygame.Surface(self.size)
		window_surface.fill(self.color)
		for component in self.components:
			component.render_on(window_surface)
		surface.blit(window_surface, self.position)
