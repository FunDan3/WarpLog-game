#! /usr/bin/python3

import asyncio
import json
from lib.aconn import aconn
import client_processor

async def handle_client(reader, writer):
	connection = aconn()
	connection.on_connected(reader, writer)
	await client_processor.process(connection)
	await connection.close()

async def main():
	server = await asyncio.start_server(handle_client, "", 21611)
	try:
		async with server:
			await server.serve_forever()
	except KeyboardInterrupt:
		await server.close()

asyncio.run(main())
