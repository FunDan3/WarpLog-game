from .default_component import default_component
import pygame

class progress_bar(default_component):
	position = None
	size = None
	progress = None #ranges from zero to 1

	border_color = None
	border = None

	filler_color = None

	void_color = None
	void = None

	def __init__(self, position, size, border_size = 2, border_color = None, filler_color = None, void_color = None):
		if not border_color:
			border_color = [255] * 3
		if not filler_color:
			filler_color = [128] * 3
		if not void_color:
			void_color = [0] * 3

		self.position = position
		self.size = size
		self.progress = 0

		self.filler_color = filler_color

		self.void_color = void_color
		self.void = self.position + self.size

		self.border_color = border_color
		self.border = [
                        position[0] - border_size,
                        position[1] - border_size,
                        size[0] + border_size*2,
                        size[1] + border_size*2]

	def render_on(self, surface):
		filler  = self.position + [self.size[0] * self.progress, self.size[1]]
		pygame.draw.rect(surface, self.border_color, self.border)
		pygame.draw.rect(surface, self.void_color, self.void)
		pygame.draw.rect(surface, self.filler_color, filler)

	def set_percentage(self, percentage):
		self.progress = percentage / 100

	def set_quantity(self, finished, total):
		self.progress = finished / total
