import PySimpleGUI as sg
import database
import screen_behaviour

class Screen():
	
	def __init__(self, params):
		self.layout = params['layout']() # Execute function of layout
		self.title = params['title']
		
		self.window = sg.Window(self.title, self.layout) # Window Defintion

		self.window_behaviour = params['behaviour'] # Behaviour -> retorna status da tela
		
	def display(self):
		#print('Displaying screen')
		return self.window_behaviour( self.window )
		
	def close(self):
		self.window.close()
		
	
next_screen = 'main'
behavs = screen_behaviour.behaviours
while next_screen:
	print('Next screen: ', next_screen)
	s = Screen(behavs[next_screen])
	next_screen = s.display()
	s.close()