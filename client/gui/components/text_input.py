from .default_component import default_component
import time
import pygame

active_component = None #To let other instances know if they are active or not

shift_mod = 4097
special_keys_mods = (list("`1234567890-=[]\\;',.//"), list("~!@#$%^&*()_+{}|:\"<>?"))

enter_key = 13
backspace_key = 8

class text_input(default_component):
	interactive = True

	position = None
	size = None

	color = None
	secondary_color = None
	font = None
	rendered_surface = None

	border_color = None
	border = None

	filler_color = None

	active = False
	default_text = None
	input_text = None

	on_enter = None
	def __init__(self, position, size, default_text = None, color = None, border_size = 2, border_color = None, filler_color = None, font = None, on_enter = None):
		if not border_color:
			border_color = [255] * 3
		if not filler_color:
			filler_color = [0] * 3
		if not color:
			color = [255] * 3
		if not default_text:
			default_text = ""
		if not on_enter:
			on_enter = lambda: None
		if not font:
			if not pygame.font.get_init():
				pygame.font.init()
			font = pygame.font.Font(size = 64) #to keep resolution high. Only affects performance during initialization and text updates.
		self.position = position
		self.size = size

		self.color = color
		self.secondary_color = [color_value//2 for color_value in color] #to appear greyish or smth
		self.font = font

		self.filler_color = filler_color

		self.default_text = default_text
		self.input_text = ""

		self.on_enter = on_enter

		self.update_text()

		self.border_color = border_color
		self.border = [
                        position[0] - border_size,
                        position[1] - border_size,
                        size[0] + border_size*2,
                        size[1] + border_size*2]

	def event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			# this if statement is a mess but generaly it checks if mouse is within hitbox. It takes self.offset in consideration
			if (event.pos[0]>=self.position[0]+self.offset[0] and event.pos[0]<=self.position[0]+self.offset[0]+self.size[0]) and (event.pos[1]>=self.position[1]+self.offset[1] and event.pos[1]<=self.position[1]+self.offset[1]+self.size[1]):
				self.activate()
			else:
				self.deactivate()
		if event.type == pygame.KEYDOWN:
			if self.active and self == active_component:
				self.on_button(event)
			else:
				self.deactivate()
	def on_button(self, event):
		if event.key == backspace_key:
			if len(self.input_text):
				self.input_text = self.input_text[:len(self.input_text)-1]
				self.update_text()
			return
		if event.key == enter_key:
			self.on_enter()
			return
		try:
			key = chr(event.key)
		except ValueError:
			return
		if event.mod == shift_mod:
			if key in special_keys_mods[0]:
				key = special_keys_mods[1][special_keys_mods[0].index(key)]
			else:
				key = key.upper()
		self.input_text += key
		self.update_text()

	def activate(self):
		global active_component
		active_component = self
		self.active = True
		self.update_text()

	def deactivate(self):
		self.active = False
		self.update_text()

	def update_text(self):
		if self.active or self.input_text:
			text = self.input_text
			color = self.color
		else:
			text = self.default_text
			color = self.secondary_color

		rendered_text = self.font.render(text, True, color)
		if text:
			width, height = rendered_text.get_size()
			factors = (1/(width/(self.size[0])), 1/(height/self.size[1]))
			self.rendered_surface = pygame.transform.scale_by(rendered_text, min(factors))
		else:
			self.rendered_surface = pygame.Surface(self.size)

	def render_on(self, surface):
		pygame.draw.rect(surface, self.border_color, self.border)
		pygame.draw.rect(surface, self.filler_color, self.position + self.size)
		text_position = [self.position[0] + (self.size[0] - self.rendered_surface.get_width())//2,
			self.position[1] + (self.size[1] - self.rendered_surface.get_height())//2]
		surface.blit(self.rendered_surface, text_position)
