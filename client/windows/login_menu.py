import pygame
import asyncio
from gui import components

async def login_menu(renderer, assets, connection):
	assets.music.menu.play(2**16) #If player isnt stuck in menu for eternity it should be enough
	window = components.window(position = (1980//2 - 256, 256), size = (512, 1080 - 256*2), closable = False)
	title = components.text_oneline(position = [0, 0], size=[512, 64], text = "WarpLog - authentication", boxed = False, font = assets.fonts.QuantumLemon)
	status_box = components.text_oneline(position = [0, 64], size = [512, 64], text = " ", color = [255, 64, 64], boxed = False, font = assets.fonts.QuantumLemon)
	login_button = components.text_button(position = [32, 384 + 96], size = [(512-64)//2-32, 64], text = "Sign in", font = assets.fonts.QuantumLemon)
	password_field = components.text_input(position = [32, 256+64], size = [512-64, 128], default_text = "Password", font = assets.fonts.AndroidInsomnia, on_enter = lambda: login_button.on_click())
	login_field = components.text_input(position = [32, 128+32], size = [512-64, 128], default_text = "Login", font = assets.fonts.AndroidInsomnia, on_enter = lambda: password_field.activate())
	register_button = components.text_button(position = [(512-64)//2+64, 384 + 96], size = [(512-64)//2-32, 64], text = "Sign up", font = assets.fonts.QuantumLemon)
	window.add_components(title, status_box, login_field, password_field, login_button, register_button)
	renderer.add_component(window)
