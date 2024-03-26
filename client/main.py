#! /usr/bin/python3
import asyncio

from gui import renderer
window = renderer.renderer()

async def main():
	await window.loop()

asyncio.run(main())
