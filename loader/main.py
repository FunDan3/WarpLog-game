#! /usr/bin/python3
target_globals = __import__("copy").copy(globals())
import pygame
import asyncio
import os
import sys
from lib import server_api

def remove_recursive(path): #rm -rf is not an option because I want windows support.
	if os.path.isdir(path):
		for file_name in os.listdir(path):
			file_path = path+"/"+file_name
			remove_recursive(file_path)
		os.rmdir(path)
	else:
		os.remove(path)

async def download_game():
	api = server_api.api("localhost")
	await api.connect()
	await api.load_assets(path = "./game/")
	await api.close()

def start_game():
	os.chdir("./game/")
	original_script_path = sys.path[0]
	sys.path[0] = os.path.abspath("./")
	target_globals["file"] = os.path.abspath("./main.py")
	with open("./main.py", "r") as f:
		exec(f.read(), target_globals, target_globals)
	sys.path[0] = original_script_path
	os.chdir("../")


if os.path.exists("./game/"):
	remove_recursive("./game")
asyncio.run(download_game())
start_game()
remove_recursive("./game")
