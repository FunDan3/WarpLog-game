from .default_component import default_component
import pygame

class image_button(default_component):
	interactive = True
	on_click = None

	position = None
	image = None

	border_color = None
	border = None

	filler_color = None
	filler = None
	def __init__(self, position, image, on_click, border_size = 2, border_color = None, filler_color = None):
		if not border_color:
			border_color = [255] * 3
		if not filler_color:
			filler_color = [128] * 3

		size = image.get_size()

		self.on_click = on_click

		self.position = position
		self.image = image

		self.filler_color = filler_color
		self.filler = position + size

		self.border_color = border_color
		self.border = [
                        position[0] - border_size,
                        position[1] - border_size,
                        size[0] + border_size*2,
                        size[1] + border_size*2]

	def render_on(self, surface):
		pygame.draw.rect(surface, self.border_color, self.border)
		pygame.draw.rect(surface, self.filler_color, self.filler)
		surface.blit(self.image, self.position)
	def event(self, event):
		pass
