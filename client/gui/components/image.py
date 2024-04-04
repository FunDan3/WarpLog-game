from .default_component import default_component
import pygame

class image(default_component):
	position = None
	image = None

	def __init__(self, position, image):
		self.position = position
		self.image = image

	def render_on(self, surface):
		surface.blit(self.image, self.position)
