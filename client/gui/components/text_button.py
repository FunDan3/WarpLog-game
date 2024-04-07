from .text_oneline import text_oneline
import pygame

class text_button(text_oneline):
	interactive = True
	on_click = None

	position = None
	size = None

	color = None
	font = None
	rendered_surface = None

	border_color = None
	border = None

	filler_color = None

	boxed = None

	def __init__(self, position, size, text, color = None, border_size = 2, border_color = None, filler_color = None, font = None, boxed = True, on_click = None):
		if not border_color:
			border_color = [255] * 3
		if not filler_color:
			filler_color = [128] * 3
		if not color:
			color = [255] * 3
		if not font:
			if not pygame.font.get_init():
				pygame.font.init()
			font = pygame.font.Font(size = 64) #to keep resolution high. Only affects performance during initialization and text updates.
		if not on_click:
			on_click = lambda: None
		self.on_click = on_click

		self.position = position
		self.size = size

		self.color = color
		self.font = font
		self.update_text(text)

		self.boxed = boxed

		self.filler_color = filler_color

		self.border_color = border_color
		self.border = [
                        position[0] - border_size,
                        position[1] - border_size,
                        size[0] + border_size*2,
                        size[1] + border_size*2]

	def update_text(self, text):
		rendered_text = self.font.render(text, True, self.color)
		width, height = rendered_text.get_size()
		factors = (1/(width/self.size[0]), 1/(height/self.size[1]))
		self.rendered_surface = pygame.transform.scale_by(rendered_text, min(factors))

	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			# this if statement is a mess but generaly it checks if mouse is within hitbox. It takes self.offset in consideration
			if (event.pos[0]>=self.position[0]+self.offset[0] and event.pos[0]<=self.position[0]+self.offset[0]+self.size[0]) and (event.pos[1]>=self.position[1]+self.offset[1] and event.pos[1]<=self.position[1]+self.offset[1]+self.size[1]):
				self.on_click()

	def render_on(self, surface):
		if self.boxed:
			pygame.draw.rect(surface, self.border_color, self.border)
			pygame.draw.rect(surface, self.filler_color, self.position + self.size)
		text_position = [self.position[0] + (self.size[0] - self.rendered_surface.get_width())//2,
			self.position[1] + (self.size[1] - self.rendered_surface.get_height())//2]
		surface.blit(self.rendered_surface, text_position)
