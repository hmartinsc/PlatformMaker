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

		self.window = sg.Window(self.title, self.layout(), size=(1200,800)) # Window Defintion

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
		self.title = "Login"
		super().__init__(params)
		params['login_time'] = datetime.now()
		print("Initializing Login")

	# Login
	def layout(self):
		# Nao sei o que fazer com os mapas ainda
		return [[sg.Text("Username"), sg.Input(), sg.Text()], \
			[sg.Text("Password"), sg.Input()], \
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

		bla = user_exists(user, psswd)
		if bla:
			self.params['jogador'] = bla
			self.params['logged'] = True
			return event#{'next': event}
		else:
			return 'login'#{'next': 'login', 'params': {'bla': 1}}

class Main(Screen):
	
	def __init__(self, params):
		self.title = "Main"
		super().__init__(params)
		print("Initializing Login")

	# Main
	def layout(self):
		# Nao sei o que fazer com os mapas ainda
		return [[sg.Button('Personagens', key="personagem", tooltip="clickme")], \
			[sg.Button('Amigos', key='friends')], \
			[sg.Button('Mapas', key='maps')], \
			[sg.Button('Configuracoes', key='config')], \
			[sg.Button('LogOut', key="login")]]
		
	def window_behaviour(self, window):
		event, values = window.read() 
		
		print('event: ', event)
		print('values: ', values)
		
		
		if event == 'login':
			self.params['logged'] = False

		return event
		
class Musicas(Screen):
    	
	def __init__(self, params):
		self.title = "Musicas"
		super().__init__(params)

	# Main
	def layout(self):
		self.songs = list_songs()		
		l = [[sg.Button(song[0]) for song in self.songs]]
	
		# Nao sei o que fazer com os mapas ainda
		return l#[[sg.Button('Jogar', key="choose_level", tooltip="clickme")]]
		
	    	
		print(self.params)
		id_jogador = self.params['jogador'][0][0]
		items = list_items(id_jogador)
		print(items)
		l = [[sg.Text(item[0], tooltip="Poder: " + str(item[1]))] for item in items]

		return l + [[sg.Button("Back", key="main")]]
		#return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]

	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)
		
		get_song(event)
		
		
		if event == 'login':
			self.params['logged'] = False

		return 'config'

class Habilidades(Screen):
    	
	def __init__(self, params):
		self.title = "Habilidades"
		super().__init__(params)

	# Main
	def layout(self):
	    	
		print(self.params)
		id_jogador = self.params['jogador'][0][0]
		items = list_habilidades(id_jogador)
		print(items)
		l = [[sg.Text(item[0], tooltip="Poder: " + str(item[1]))] for item in items]

		return l + [[sg.Button("Back", key="main")]]
		#return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]

	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)		
		
		if event == 'login':
			self.params['logged'] = False

		return 'config'

class Friend(Screen):
	
	def __init__(self, params):
		self.title = "Friends"
		super().__init__(params)
		print("Initializing firends")

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
		

class Maps(Screen):
	
	def __init__(self, params):
		self.title = "Maps"
		super().__init__(params)
		print("Initializing maps")

	# Friend
	def layout(self):
		friends = list_friends(self.params['user'])
		print('\nFRIENDS: ', friends)
		maps = list_maps()
		l = [[sg.Text(m[0], tooltip=m[1])] for m in maps]

		return l + [[sg.Button("Back", key="main")]]
		#return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]


	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)
		
		return event
		

class Items(Screen):
	
	def __init__(self, params):
		self.title = "Items"
		super().__init__(params)
		print("Initializing items")

	# Friend
	def layout(self):
    	
		print(self.params)
		id_jogador = self.params['jogador'][0][0]
		items = list_items(id_jogador)
		print(items)
		l = [[sg.Text(item[0], tooltip="Poder: " + str(item[1]))] for item in items]

		return l + [[sg.Button("Back", key="config")]]
		#return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]


	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)
		
		return event


class Skin(Screen):
	
	def __init__(self, params):
		self.title = "Skins"
		super().__init__(params)
		print("Initializing skins")

	# Friend
	def layout(self):
    	
		print("\n"*10)
		#print(self.params)
		id_jogador = self.params['jogador'][0][0]
		skins = list_skins_jogador(id_jogador)
		print(skins)


		l = [[sg.Text(item[1], tooltip="Cor: " + item[0]), sg.Image(item[2])] for item in skins]
		 

		return [[sg.Button("Back", key="config")]] + l
		#return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]


	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)
		
		return event


class Config(Screen):
	
	def __init__(self, params):
		self.title = "Configs"
		super().__init__(params)
		print("Initializing Login")

	def layout(self):
		return [[sg.Button('Efeitos sonoros', key="musicas")], \
		[sg.Button('Skins', key="skins")], \
		[sg.Button('Items', key="items")], \
		[sg.Button('Habilidades', key="habilidades")],\
		[sg.Button('Back', key='main')]]
		
	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)

		return event


class Personagem(Screen):
	
	def __init__(self, params):
		self.title = "Personagens"
		super().__init__(params)
		print("Initializing personagem")

	def layout(self):
    	
		items = list_characters()
		print(items)
		l = [[sg.Text(item[0], tooltip=item[1])] for item in items]

		return l + [[sg.Button("Back", key="main")]]
		#return [[sg.Button('Obrigado, amigo, vc e um amigo', key="main")]]
		
	def window_behaviour(self, window):
		event, values = window.read()
		
		print('event: ', event)
		print('values: ', values)
		
		return event


class Level(Screen):
	
	def __init__(self, params):
		self.title = "Levels"
		super().__init__(params)
		print("Initializing level")

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
	"personagem": Personagem,
	"level": Level,
	"musicas": Musicas,
	"maps": Maps,
	"items": Items,
	"skins": Skin,
	"habilidades": Habilidades
}
