#! /usr/bin/python3
import asyncio
import pygame
import random

import windows
from gui import renderer

pygame.font.init()
pygame.mixer.init()

renderer = renderer.renderer()

asset_map = {
	"fonts.QuantumLemon": ("pygame.font.Font('%s', 128)", "./assets/fonts/QuantumLemon.ttf"),
	"image.credit": ("pygame.image.load('%s')", "./assets/images/credit.png"),
	"music.menu": random.choice([("pygame.mixer.Sound('%s')", "./assets/music/menu1.mp3"), ("pygame.mixer.Sound('%s')", "./assets/music/menu2.mp3")]),
	"sfx.cancel": ("pygame.mixer.Sound('%s')", "./assets/sfx/cancel.mp3"),
	"sfx.error": ("pygame.mixer.Sound('%s')", "./assets/sfx/error.mp3"),
	"sfx.success": ("pygame.mixer.Sound('%s')", "./assets/sfx/success.mp3")
}

async def window_switcher():
	assets = await windows.load_assets(renderer, asset_map)
async def main():
	await asyncio.gather(renderer.loop(), window_switcher())

asyncio.run(main())
