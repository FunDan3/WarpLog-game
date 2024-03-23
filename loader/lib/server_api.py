from .aconn import aconn
import asyncio
import pygame
import json
import os

pygame.font.init()
pygame.mixer.init()

class folder:
	def __init__(self, **kwargs):
		for name, value in kwargs:
			setattr(self, name, value)

code_map = {
"close": 0,
"load_assets": 1,
}

code_bytes = 2

for key, value in code_map.items():
	code_map[key] = value.to_bytes(code_bytes, "big", signed = False)

def get_loading_method(filename):
	ext = os.path.splitext(filename)[1]
	for method, file_formats in loading_methods.items():
		if ext in file_formats:
			return method
	return "%s"

class api:
	ip = None
	port = None
	connection = None
	def __init__(self, ip = None, port = 21611):
		if not ip:
			ip = "foxomet.ru"
		self.ip = ip
		self.port = port
	async def connect(self):
		self.connection = aconn()
		await self.connection.connect(self.ip, self.port)
	async def load_assets(self):
		await self.connection.write(code_map["load_assets"])
		json_size = int.from_bytes(await self.connection.read(16), "big", signed = False)
		json_data = json.loads(await self.connection.read(json_size))
		total_files_size = json_data["total_files_size"]
		loaded_files_size = 0
		assets = folder()
		for file_path, file_size in json_data["asset_sizes"].items():
			loaded_files_size += file_size
			print(f"Loading asset {file_path} {round(loaded_files_size/total_files_size*100, 2)}%")
			asset_name = os.path.splitext(file_path)[0].split("/")[-1]
			asset_content = await self.connection.read(file_size)
			asset_content = eval("%s" % "asset_content")
			setattr(assets, asset_name, asset_content)
		return assets
