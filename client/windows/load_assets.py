import os
import pygame
import asyncio
import time
from gui import components
from lib import server_api

class folder:
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

async def load_assets(renderer, asset_map):
	start_time = time.time()
	total_filesize = sum([os.path.getsize(load_data[1]) for name, load_data in asset_map.items()])
	loaded_filesize = 0
	window = components.layer()
	progress_bar = components.progress_bar(position = [128, 1080 - 128], size = [1980 - 128*2, 32])
	text = components.text_oneline(position = [128, 1080 - 256], size = [1980 - 128*2, 32], text = "Loading...", boxed = False)
	window.add_component(progress_bar)
	window.add_component(text)
	renderer.add_component(window)

	assets = folder()
	for name, load_data in asset_map.items():
		loading_method, file = load_data
		text.update_text(f"Loading file '{file}'")
		await renderer.one_time_loop() #to let it render stuff
		loaded_asset = eval(loading_method % file)
		past_path = "assets"
		for name_chunk in name.split("."):
			if not hasattr(eval(past_path), name_chunk):
				if name_chunk == name.split(".")[-1]:
					setattr(eval(past_path), name_chunk, loaded_asset)
				else:
					setattr(eval(past_path), name_chunk, folder())
			past_path += f".{name_chunk}"
		file_size = os.path.getsize(file)
		loaded_filesize += file_size
		progress_bar.set_quantity(loaded_filesize, total_filesize)
	text.update_text("Setting up anticheat...")
	await renderer.one_time_loop()
	components.text_oneline.load_anticheat()
	text.update_text("Connecting to server...")
	await renderer.one_time_loop()
	try:
		connection = server_api.api("127.0.0.1" if os.path.exists("../development.mark") else "foxomet.ru", 21611) #Static because it is sent by server.
		await connection.connect()
	except Exception as e:
		text.color = [255, 64, 64]
		text.update_text(f"Could not connect to server: {str(e)}")
		progress_bar.border_color = [255, 0, 0]
		progress_bar.filler_color = [255, 64, 64]
		while True:
			await asyncio.sleep(2*32)
	await renderer.empty_components()
	print(f"Loaded assets in {time.time() - start_time} seconds")
	return assets, connection

