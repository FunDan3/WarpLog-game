from aiofiles import os, open
import json

assets_path = "../client/assets/"
assets = None
async def load_assets():
	global assets
	if assets:
		return assets
	assets = []
	json_data = {"asset_sizes": {}}
	filelist = await os.listdir(assets_path)
	total_size = 0
	for file in filelist:
		file_path = assets_path+file
		async with open(file_path, "rb") as f:
			data = await f.read()
			size = len(data)
			total_size += size
		assets.append(data)
		json_data["asset_sizes"][file] = size
	json_data["total_files_size"] = total_size
	json_data = json.dumps(json_data).encode("utf-8")
	json_size = len(json_data)
	assets = json_size.to_bytes(16, "big", signed = False) + json_data + b"".join(assets)
	return assets

async def main(connection):
	await connection.write(await load_assets())
