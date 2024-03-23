import json
import functions

def serialize_codes(code_map):
	new_code_map = {}
	for key, value in code_map.items():
		new_code_map[key.to_bytes(2, "big", signed = False)] = value
	return new_code_map

code_map = serialize_codes({
0: "close",
1: "load_assets"})

async def process(connection):
	while True:
		command = await connection.read(2)
		if not command or code_map[command] == "close":
			print("Closed")
			return
		else:
			command = code_map[command]
			print(f"Executing {command}")
			function = getattr(functions, command).main #Its only a matter of time before eval is exploited so I figured it is safer
			await function(connection)
