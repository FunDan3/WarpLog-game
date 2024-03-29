#! /usr/bin/python3
import asyncio
from gui import renderer
import gui.components as components

renderer = renderer.renderer()

async def main():
	renderer.add_component(components.window(position = (200, 300), size = (300, 200), border_size = 2))
	await renderer.loop()

asyncio.run(main())
