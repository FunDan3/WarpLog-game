import pygame
import asyncio
import sys

class layer:
	components = None

	visible = True
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
class renderer:
	screen = None
	layers = None
	def __init__(self):
		self.screen = pygame.display.set_mode((1980, 1080), pygame.FULLSCREEN)
		self.layers = []

	async def one_time_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit("Program finished.")
				self.get_focused_layer().event(event)
		for layer in self.layers:
			if layer.visible:
				layer.render(self.screen)

	def get_focused_layer(self):
		for layer in self.layers[::-1]:
			if layer.visible and layer.interactive:
				return layer

	async def loop(self):
		while True:
			await asyncio.gather(self.one_time_loop(), asyncio.sleep(1/60))
