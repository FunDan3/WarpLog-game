from .default_component import default_component
import pygame

class image_button(default_component):
	interactive = True
	on_click = None

	position = None
	size = None
	image = None

	border_color = None
	border = None
	roundness = None


	filler_color = None
	filler = None
	def __init__(self, position, image, on_click, border_size = 2, border_color = None, filler_color = None, roundness = 32):
		if not border_color:
			border_color = [255] * 3
		if not filler_color:
			filler_color = [128] * 3
		self.roundness = roundness / 100
		self.size = image.get_size()

		self.on_click = on_click

		self.position = position
		self.image = image

		self.filler_color = filler_color
		self.filler = position + self.size

		self.border_color = border_color
		self.border = [
                        position[0] - border_size,
                        position[1] - border_size,
                        size[0] + border_size*2,
                        size[1] + border_size*2]

	def render_on(self, surface):
		pygame.draw.rect(surface, self.border_color, self.border, border_radius = round(max(self.border[2:])/2*self.roundness))
		pygame.draw.rect(surface, self.filler_color, self.filler, border_radius = round(max(self.filler[2:])/2*self.roundness))
		surface.blit(self.image, self.position)
	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			# this if statement is a mess but generaly it checks if mouse is within hitbox. It takes self.offset in consideration
			if (event.pos[0]>=self.filler[0]+self.offset[0] and event.pos[0]<=self.filler[0]+self.offset[0]+self.filler[2]) and (event.pos[1]>=self.filler[1]+self.offset[1] and event.pos[1]<=self.filler[1]+self.offset[1]+self.filler[3]):
				self.on_click()
