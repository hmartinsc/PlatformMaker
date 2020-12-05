import PySimpleGUI as sg
from database import *


class Screen():
    	
	def __init__(self, params):
		print("Initializing screen")
		#self.layout = params['layout']() # Execute function of layout
		#self.title = params['title']
		
		#import pdb; pdb.set_trace()

		self.window = sg.Window(self.title, self.layout(), size=(800,600)) # Window Defintion

		#self.window_behaviour = params['behaviour'] # Behaviour -> retorna status da tela
		
	def display(self):
		#print('Displaying screen')
		return self.window_behaviour( self.window )
		
	def close(self):
		self.window.close()

class Login(Screen):
    
	def __init__(self, params):
		self.title = "Login screen"
		super().__init__(params)
		print("Initializing Login")

	# Login
	def layout(self):
		# Nao sei o que fazer com os mapas ainda
		return [[sg.Text("Username"), sg.Input(size=(10, 10)), \
			sg.Text("Password"), sg.Input(size=(10, 10)), \
			sg.Button('LogIn', key="main")]]

	def window_behaviour(self, window):
		event, values = window.read() 
		
		user, psswd = values[0], values[1]

		print('event: ', event)
		print('values: ', values)
		print('user: ', user)
		print('passqord: ', psswd)

		if user_exists(user, psswd):
			return {'next': event}
		else:
			return {'next': 'login', 'params': {'bla': 1}}

class Main(Screen):
    
	def __init__(self, params):
		self.title = "Login screen"
		super().__init__(params)
		print("Initializing Login")

	# Main
	def layout(self):
		# Nao sei o que fazer com os mapas ainda
		return [[sg.Button('Jogar', key="choose_level", tooltip="clickme")], \
			[sg.Button('Amigos', key='friends')], \
			[sg.Button('Mapas', key='main')], \
			[sg.Button('Configuracoes', key='config')], [sg.Button('LogOut', key="login")]]
		
	def window_behaviour(self, window):
		event, values = window.read() 
		
		print('event: ', event)
		print('values: ', values)
			
		return event

class Friend(Screen):
    
	def __init__(self, params):
		self.title = "Login screen"
		super().__init__(params)
		print("Initializing Login")
	# Friend
	def layout():
		#list_friends()
		return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]


	def window_behaviour(window):
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
	"login": Login,
	"main": Main,
	"friend": Friend
}