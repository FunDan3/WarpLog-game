#! /usr/bin/python3
import asyncio
import pygame

from gui import renderer
import gui.components as components

renderer = renderer.renderer()

def on_click():
	print("CLIK")

async def main():
	window = components.window(position = (128, 128), size = (512, 512), border_size = 2)
	window.add_component(
		components.image_button(position = (128, 128), on_click = on_click, image = pygame.image.load("./assets/images/credit.png"))
	)
	renderer.add_component(window)
	await renderer.loop()

asyncio.run(main())
