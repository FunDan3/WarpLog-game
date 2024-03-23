#! /usr/bin/python3
target_globals = __import__("copy").copy(globals())
import pygame
import asyncio
import os
import sys
from lib import server_api


async def start_game():
	api = server_api.api("localhost")
	await api.connect()
	await api.load_assets(path = "./game/")
	os.chdir("./game/")
	sys.path.pop(0)
	sys.path.insert(0, os.path.abspath("./"))
	target_globals["file"] = os.path.abspath("./main.py")

	with open("./main.py", "r") as f:
		exec(f.read(), target_globals, {})

asyncio.run(start_game())
