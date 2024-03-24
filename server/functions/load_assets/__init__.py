from aiofiles import os as aos
from aiofiles import open
import os
import json

client_path = "../client/"
data = None

banned_extensions = [".xcf"] #to save ram and user download time

async def load_folder(real_path, imaginary_path = None):
	if not imaginary_path:
		imaginary_path = "./"
	files = []
	filelist = await aos.listdir(real_path)
	for file in filelist:
		file_path = real_path+file
		imaginary_file_path = imaginary_path + file
		if await aos.path.isdir(file_path):
			files += await load_folder(file_path+"/", imaginary_file_path+"/")
		else:
			if os.path.splitext(file_path)[1] in banned_extensions:
				continue
			async with open(file_path, "rb") as f:
				data = await f.read()
			files.append((imaginary_file_path, data))
	return files
async def load_assets():
	global data
	if data:
		return data
	files = []
	json_data = {"file_sizes": {}}
	json_data["total_size"] = 0

	files = await load_folder(client_path)
	contents = []
	for path, content in files:
		json_data["file_sizes"][path] = len(content)
		json_data["total_size"] += len(content)
		contents.append(content)
	json_data = json.dumps(json_data).encode("utf-8")
	json_size = len(json_data)
	data = json_size.to_bytes(32, "big", signed = False) + json_data + b"".join(contents)
	return data

async def main(connection):
	await connection.write(await load_assets())
