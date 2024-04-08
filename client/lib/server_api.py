from .aconn import aconn
import hashlib
import asyncio
import json
import os

code_map = {
"close": 0,
"load_assets": 1, #not inplemented in client code
"authenticate": 2,
}

code_bytes = 2

for key, value in code_map.items():
	code_map[key] = value.to_bytes(code_bytes, "big", signed = False)

class api:
	ip = None
	port = None
	connection = None
	def __init__(self, ip = None, port = 21611):
		if not ip:
			ip = "foxomet.ru"
		self.ip = ip
		self.port = port
	async def authenticate(self, login, password, registration = False):
		password_hash = hashlib.new("sha512")
		password_hash.update(password.encode("utf-8"))
		password_hash.update(login.encode("utf-8"))
		password_hash = password_hash.digest() #64 bytes
		request = b"".join([code_map["authenticate"],
			int(registration).to_bytes(1, "big", signed = False),
			password_hash,
			len(login).to_bytes(1, "big", signed = False) + login.encode("utf-8")])
		await self.connection.write(request)

	async def connect(self):
		self.connection = aconn()
		await self.connection.connect(self.ip, self.port)
	async def close(self):
		await self.connection.write(code_map["close"])
		await self.connection.close()
