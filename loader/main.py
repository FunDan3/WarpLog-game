#! /usr/bin/python3
import pygame
import asyncio

from lib import server_api

async def start_game():
	api = server_api.api("localhost")
	await api.connect()
	await api.load_assets(path = "./game/")

asyncio.run(start_game())
