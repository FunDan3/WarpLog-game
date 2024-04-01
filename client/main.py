#! /usr/bin/python3
import asyncio
import pygame

from gui import renderer
import gui.components as components

renderer = renderer.renderer()
window = components.window(position = (128, 128), size = (512, 512), border_size = 2)
progress_bar = components.progress_bar(position = [128, 128], size = [256, 32])

async def loop():
	for i in range(1000-6):
		await asyncio.sleep(0.01)
		progress_bar.set_quantity(i, 1000-7) #💀

async def main():
	window.add_component(progress_bar)
	renderer.add_component(window)
	await asyncio.gather(renderer.loop(), loop())
asyncio.run(main())
