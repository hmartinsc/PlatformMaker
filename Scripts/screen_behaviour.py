import PySimpleGUI as sg
from database import *

# Login
def login_layout():
	# Nao sei o que fazer com os mapas ainda
	return [[sg.Text("Username"), sg.Input(size=(10, 10)), \
		sg.Text("Password"), sg.Input(size=(10, 10)), \
		sg.Button('LogIn', key="main")]]

def login_behav(window):
	event, values = window.read() 
	
	user, psswd = event[0], event[1]

	print('event: ', event)
	print('values: ', values)
	print('user: ', user)
	print('passqord: ', psswd)

	if user_exists(user, psswd):
		return event
	else:
		return 'login'

# Main
def main_layout():
	# Nao sei o que fazer com os mapas ainda
	return [[sg.Button('Jogar', key="choose_level", tooltip="clickme")], \
		[sg.Button('Amigos', key='friends')], \
		[sg.Button('Mapas', key='main')], \
		[sg.Button('Configuracoes', key='config')], [sg.Button('LogOut', key="login")]]
	
def main_behav(window):
	event, values = window.read() 
	
	print('event: ', event)
	print('values: ', values)
		
	return event

# Friend
def friend_layout():
	return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]
	
def friend_behav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event

# Config
def config_layout():
	return [[sg.Button('Habilidades', key="main")], \
	[sg.Button('Skins', key="config")], \
	[sg.Button('Itens', key="friends")]]
	
def config_behav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)

	return event

# Choose level
def choose_level_layout():
	return [[sg.Button('Fase1', key="main"), sg.Image('Images/avatar1.png')], \
		[sg.Button('Fase2', key="config"), sg.Image('Images/avatar1.png')]]
	
def choose_level_behav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event

# Level
def level_layout():
	return [[sg.Button('Este é um nivel', key="main")]]
	
def level_behav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event


# Transition between screens
def cond_main_to_friends(window):
	return True

behaviours = {

	"login": {
		"title": "Login screen",
		"layout": login_layout,
		"behaviour": login_behav,
		"next_screen": [
			{ "destination": "Friends", "condition": cond_main_to_friends }
		]
	},
	"main": {
		"title": "Main screen",
		"layout": main_layout,
		"behaviour": main_behav,
		"next_screen": [
			{ "destination": "Friends", "condition": cond_main_to_friends }
		]
	},
	"friends": {
		"title": "Friends",
		"layout": friend_layout,
		"behaviour": friend_behav,
		"next_screen": [
			{ "destination": "Friends", "condition": cond_main_to_friends }
		]
	},
	"config": {
		"title": "Configurations",
		"layout": config_layout,
		"behaviour": config_behav,
		"next_screen": [
			{ "destination": "Friends", "condition": cond_main_to_friends }
		]
	},
	"choose_level": {
		"title": "Choose Level",
		"layout": choose_level_layout,
		"behaviour": choose_level_behav,
		"next_screen": [
			{ "destination": "Friends", "condition": cond_main_to_friends }
		]
	},
	"level": {
		"title": "Level",
		"layout": level_layout,
		"behaviour": level_behav,
		"next_screen": [
			{ "destination": "Friends", "condition": cond_main_to_friends }
		]
	}
}
