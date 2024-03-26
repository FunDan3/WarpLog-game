from .aconn import aconn
from aiofiles import os as aos
import aiofiles
import asyncio
import pygame
import json
import os

pygame.font.init()
pygame.mixer.init()
code_map = {
"close": 0,
"load_assets": 1,
}

code_bytes = 2

for key, value in code_map.items():
	code_map[key] = value.to_bytes(code_bytes, "big", signed = False)

async def ensure_path(file):
	past_dir = ""
	for dir in file.split("/")[:len(file.split("/"))-1]:
		try:
			await aos.mkdir(past_dir+dir)
		except FileExistsError:
			pass
		past_dir += dir + "/"
async def write_file(path, content):
	await ensure_path(path)
	async with aiofiles.open(path, "wb") as f:
		await f.write(content)

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
	async def close(self):
		await self.connection.write(code_map["close"])
		await self.connection.close()
