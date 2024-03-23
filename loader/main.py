#! /usr/bin/python3
import pygame
import asyncio

from lib import server_api

async def start_game():
	api = server_api.api("localhost")
	await api.connect()
	assets = await api.load_assets()
	for attr in dir(assets):
		if not attr.startswith("_"):
			print(getattr(assets, attr))

asyncio.run(start_game())
