import json
import string

allowed_login_characters = string.ascii_letters + string.digits + "_"

def check_login_validity(login):
	for character in login:
		if character not in allowed_login_characters:
			return False
	return True

async def send_message(connection, message):
	await connection.write(b"".join([len(message.encode("utf-8")).to_bytes(4, "big", signed = False), message.encode("utf-8")]))

async def main(connection):
	registration = bool(int.from_bytes(await connection.read(1), "big", signed = False))
	password_hash = await connection.read(64) #sha-512
	login_size = int.from_bytes(await connection.read(1), "big", signed = False)
	login = await connection.read(login_size)
	login = login.decode("utf-8")

	if not check_login_validity(login):
		await send_message(connection, "Login can only contain alphanumerical and underscore characters")
		return

	if len(login) < 4 or len(login) > 32:
		await send_message(connection, "Login size must be in range from 4 to 32 characters")
		return

	await send_message(connection, "")
