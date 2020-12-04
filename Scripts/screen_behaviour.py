import PySimpleGUI as sg

def mainLayout():
	return [[sg.Button('Jogar', key="TestKey", tooltip="clickme")], [sg.Button('Amigos', key="friends")], [sg.Button('Mapas')], [sg.Button('Configuracoes')]]
	
def mainBehav(window):
	event, values = window.read() 
	
	print('event: ', event)
	print('values: ', values)
	
	#if event == '1': # First button
	#	pass
	#if event == 'Amigos':
	#	print("Amigos")
	#if event == '3':
	#	pass
	#if event == '4': # Fourth button
	#	pass

	#print('Hello', values[0], "! Thanks for trying PySimpleGUI")
	#print("ANiversario em %s" % values[1])
		
	return event
	
def condMainToFriends(window):
	return True
	
def friendLayout():
	return [[sg.Button('Obrigado, amigo, vc e um amigo', key="friends")]]
	
def friendBehav(window):
	event, values = window.read()
	
	print('event: ', event)
	print('values: ', values)
	
	return event

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
