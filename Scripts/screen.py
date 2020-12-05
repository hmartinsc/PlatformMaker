import PySimpleGUI as sg
from screen_behaviour import *

		
if __name__ == '__main__':
	next_screen = 'login'
	params = {}
	behavs = behaviours#screen_behaviour.behaviours
	while next_screen:
		#window, event, values = sg.read_all_windows()
		#print("window " , window)
		#print("event ", event)
		#print("values ", values)

		print('Next screen: ', next_screen)

		s = behavs[next_screen](params)#Screen(behavs[next_screen])
		bla = s.display()
		next_screen = bla['next']
		s.close()