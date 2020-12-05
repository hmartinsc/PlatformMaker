import PySimpleGUI as sg
from database import *
from datetime import datetime, timedelta

class Screen():
		
	def __init__(self, params):
    	
		print("\nInitializing screen")
		self.params = params#.copy()
		print("params: ", params)

		if('logged' not in params.keys()):
			print("Not logged (param does not exist)")
		else:
			if(params['logged'] == True):
				print("Logged")
				print('logintime: ', params['login_time'])

				if params['login_time'] \
					and datetime.now() > params['login_time'] + timedelta(seconds=500):
					
					#import pdb; pdb.set_trace()
					params["logged"] = False 
			else:
				print("Not logged")
				#return

		#self.layout = params['layout']() # Execute function of layout
		#self.title = params['title']
		
		#import pdb; pdb.set_trace()

		self.window = sg.Window(self.title, self.layout(), size=(800,600)) # Window Defintion

		#self.window_behaviour = params['behaviour'] # Behaviour -> retorna status da tela
		
	def display(self):
		#print('Displaying screen')
		#import pdb; pdb.set_trace()
		if 'logged' in self.params.keys() and not self.params['logged']:
    			self.params['logged'] = True # Infinit loop otherwise
    			return 'login'
		return self.window_behaviour( self.window )
		
	def close(self):
		self.window.close()

class Login(Screen):
	
	def __init__(self, params):
		self.title = "Login screen"
		super().__init__(params)
		params['login_time'] = datetime.now()
		print("Initializing Login")

	# Login
	def layout(self):
		# Nao sei o que fazer com os mapas ainda
		return [[sg.Text("Username"), sg.Input(size=(10, 10))], \
			[sg.Text("Password"), sg.Input(size=(10, 10))], \
			[sg.Button('LogIn', key="main")]]

	def window_behaviour(self, window):
		event, values = window.read() 
		
		user, psswd = values[0], values[1]
		self.params['user'] = user
		self.params['password'] = psswd

		print('event: ', event)
		print('values: ', values)
		print('user: ', user)
		print('passqord: ', psswd)

		if user_exists(user, psswd):
			self.params['logged'] = True
			return event#{'next': event}
		else:
			return 'login'#{'next': 'login', 'params': {'bla': 1}}

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
	def layout(self):
		friends = list_friends(self.params['user'])
		print('\nFRIENDS: ', friends)
		l = [[sg.Text(friend[0])] for friend in friends]

		return l + [[sg.Button("Back", key="main")]]
		#return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]


	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)
		
		return event


class Config(Screen):
	
	def __init__(self, params):
		self.title = "Login screen"
		super().__init__(params)
		print("Initializing Login")

	def layout(self):
		return [[sg.Button('Habilidades', key="main")], \
		[sg.Button('Skins', key="config")], \
		[sg.Button('Itens', key="friends")]]
		
	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)

		return event


class ChooseLevel(Screen):
	
	def __init__(self, params):
		self.title = "Login screen"
		super().__init__(params)
		print("Initializing Login")

	def layout(self):
		return [[sg.Button('Fase1', key="main"), sg.Image('Images/avatar1.png')], \
			[sg.Button('Fase2', key="config"), sg.Image('Images/avatar1.png')]]
		
	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)
		
		return event


class Level(Screen):
	
	def __init__(self, params):
		self.title = "Login screen"
		super().__init__(params)
		print("Initializing Login")

	def layout():
		return [[sg.Button('Este é um nivel', key="main")]]
		
	def window_behaviour(window):
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
	"friends": Friend,
	"config": Config,
	"choose_level": ChooseLevel,
	"level": Level
}