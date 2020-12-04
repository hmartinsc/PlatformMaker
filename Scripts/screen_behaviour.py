import PySimpleGUI as sg

# Main
def mainLayout():
	return [[sg.Button('Jogar', key="TestKey", tooltip="clickme")], [sg.Button('Amigos', key="friends")], [sg.Button('Mapas')], [sg.Button('Configuracoes')]]
	
def mainBehav(window):
	event, values = window.read() 
	
	print('event: ', event)
	print('values: ', values)
		
	return event

# Friend
def friendLayout():
	return [[sg.Button('Obrigado, amigo, vc e um amigo', key="friends")]]
	
def friendBehav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event

# Config
def configLayout():
	return [[sg.Button('Button', key="next")]]
	
def configBehav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event

# Choose level
def chooseLevelLayout():
	return [[sg.Button('Button', key="next")]]
	
def chooseLevelLayoutBehav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event

# Level
def levelLayout():
	return [[sg.Button('Button', key="next")]]
	
def levelLayoutBehav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event


def condMainToFriends(window):
	return True

behaviours = {

	"main": {
		"title": "Main screen",
		"layout": mainLayout(),#[[sg.Button('Jogar')], [sg.Button('Amigos')], [sg.Button('Mapas')], [sg.Button('Configuracoes')]]
		"behaviour": mainBehav,
		"nextScreen": [
			{ "destination": "Friends", "condition": condMainToFriends }
		]
	},
	"friends": {
		"title": "Friends",
		"layout": friendLayout(),
		"behaviour": friendBehav,
		"nextScreen": [
			{ "destination": "Friends", "condition": condMainToFriends }
		]
	}
}
