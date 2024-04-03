import pygame
import asyncio
import sys
from . import components, exceptions
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
			focused_layer = self.get_focused_layer()
			if focused_layer:
				focused_layer.event(event)
		self.screen.fill((0, 0, 0))
		for layer in self.layers:
			if layer.visible:
				layer.render_on(self.screen)
		pygame.display.flip()

	def get_focused_layer(self):
		for layer in self.layers[::-1]:
			if layer.visible and layer.interactive:
				return layer

	def add_component(self, layer, bypass_layer_check = False):
		if not bypass_layer_check:
			if type(layer) not in [components.layer, components.window]:
				raise exceptions.NotLayerComponent("Renderer should only have layers.")
		layer.renderer = self
		layer.parent = self
		self.layers.append(layer)
		layer.on_added()

	async def empty_components(self):
		self.layers = []
		await self.one_time_loop()

	async def loop(self):
		while True:
			await asyncio.gather(self.one_time_loop(), asyncio.sleep(1/60))
