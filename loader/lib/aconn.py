import asyncio
import json
class aconn:
	reader = None
	writer = None
	def __init__(self):
		pass
	async def connect(self, ip, port):
		self.reader, self.writer = await asyncio.open_connection(ip, port)
	async def write(self, data):
		if type(data) in [list, dict]:
			data = json.dumps(data)
		elif type(data) not in [str, bytes]:
			data = str(data)
		if type(data) == str:
			data = data.encode("utf-8")
		self.writer.write(data)
		await self.writer.drain()
	async def read(self, size):
		return await self.reader.read(size)
	async def readline(self):
		return await self.reader.readline()
	async def close(self):
		self.writer.close()
		await self.writer.wait_closed()
