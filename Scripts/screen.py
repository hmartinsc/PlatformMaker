import PySimpleGUI as sg 

class Screen():
	
	def __init__(self, params):#, window_behaviour):
		self.layout = params['layout']
		self.title = params['title']
		
		self.window = sg.Window(self.title, self.layout) # Window Defintion

		#self.window_behaviour = window_behaviour # Behaviour -> retorna status da tela
		
	def display(self):
		print('Displaying screen')
		return self.window_behaviour( self.window )
		
	def close(self):
		self.window.close()
		
	def window_behaviour(self, window):
		# Default screen
		event, values = window.read() 

		# Do something with the information gathered
		print('Hello', values[0], "! Thanks for trying PySimpleGUI")
		print("ANiversario em %s" % values[1])
		
		return True
		
		
class ScreenStack():

	def __init__(self):
		self.stack = []
		

class MainScreen(Screen):

	# Overwriting method
	def window_behaviour(self, window):
		print("Nada a ser feito")
		return True
	

# Tela 1	
layout = [  [sg.Text("What's your name?")],
            [sg.Input()],
            [sg.Button('Ok')] ]
title = 'Titulo legal'

params = { 'layout': layout, 'title': title }
s1 = MainScreen(params)
#
#s1.display()
#s1.close()


# Tela 2
params = params.copy()

print("eae mano")
title = 'Outro titulo'
params['title'] = title
params['layout'] = [  [sg.Text("Qual o seu nome?")],
            [sg.Input()],
            [sg.Text("Data de nascimento?")],
            [sg.Input()],
            [sg.Button('Ok')] ]
s2 = Screen(params)

s2.display()
s2.close()