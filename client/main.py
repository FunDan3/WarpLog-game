#! /usr/bin/python3
import asyncio
import pygame

import windows
from gui import renderer

pygame.font.init()

renderer = renderer.renderer()

asset_map = {
	"fonts.QuantumLemon": ("pygame.font.Font('%s', 128)", "./assets/fonts/QuantumLemon.ttf"),
}

async def window_switcher():
	assets = await windows.load_assets(renderer, asset_map)
async def main():
	await asyncio.gather(renderer.loop(), window_switcher())

asyncio.run(main())
