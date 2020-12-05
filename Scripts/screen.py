import PySimpleGUI as sg
import screen_behaviour

class Screen():
	
	def __init__(self, params):
		self.layout = params['layout']() # Execute function of layout
		self.title = params['title']
		
		self.window = sg.Window(self.title, self.layout, size=(800,600)) # Window Defintion

		self.window_behaviour = params['behaviour'] # Behaviour -> retorna status da tela
		
	def display(self):
		#print('Displaying screen')
		return self.window_behaviour( self.window )
		
	def close(self):
		self.window.close()
		
if __name__ == '__main__':
	next_screen = 'login'
	behavs = screen_behaviour.behaviours
	while next_screen:
		#window, event, values = sg.read_all_windows()
		#print("window " , window)
		#print("event ", event)
		#print("values ", values)

		print('Next screen: ', next_screen)
		s = Screen(behavs[next_screen])
		next_screen = s.display()
		s.close()