#! /usr/bin/python3
import asyncio
import pygame

from gui import renderer
import gui.components as components

pygame.font.init()

renderer = renderer.renderer()
window = components.window(position = [128, 128], size = (512, 512), border_size = 2)
multilined_text = components.text_multiline(position = [0, 0], size = [512, 128], text = "TestSmall\nTest string that is quite big", font = pygame.font.Font("./assets/fonts/QuantumLemon.ttf", 64))
text = components.text_oneline(position = [0, 256], size = [256, 32], text = "Test", font = pygame.font.Font("./assets/fonts/QuantumLemon.ttf", 64))
progress_bar1 = components.progress_bar(position = [128, 128], size = [256, 32])
progress_bar2 = components.progress_bar(position = [128, 192], size = [256, 32])

async def loop1():
	for i in range(1000-6):
		await asyncio.sleep(0.01)
		progress_bar1.set_quantity(i, 1000-7) #💀

async def loop2():
	for i in range(1000-6):
		await asyncio.sleep(0.05)
		progress_bar2.set_quantity(i, 1000-7) #💀

async def main():
	progress_bars = components.group(progress_bar1, progress_bar2)
	window.add_component(multilined_text)
	window.add_component(text)
	window.add_component(progress_bars)
	renderer.add_component(window)
	await asyncio.gather(renderer.loop(), loop1(), loop2())

asyncio.run(main())
