import pg8000
import psswd

conn = pg8000.connect(user = 'postgres',
	host = 'localhost',
	password = psswd.psswd,
	database = 'jogo')
	
cursor = conn.cursor()

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

def exe_query(query=str()):
	cursor.execute(query)
	try:
		response = cursor.fetchall()
	except pg8000.exceptions.ProgrammingError:
		return cursor.rowcount
	
	return(response)
	
def user_exists(username, email):
	query = "SELECT * FROM public.jogador WHERE email = '%s' AND senha = '%s'"
	print(query % (username, email))
	#import pdb; pdb.set_trace()

	result = exe_query(query % (username, email))
	return result

	
def add_user(username, email):
	# Verify if is valid!!!!!
	
	# Add to database
	query = "INSERT INTO  public.jogador (nick, email) VALUES ('%s', '%s')" % (username, email)
	exe_query(query)


if __name__ == '__main__':
	username = "noobmaster"
	email = "haroldo.mansur@outlook.com"

	if user_exists(username, email):
		print("User exists")
	else:
		print("User not found")
