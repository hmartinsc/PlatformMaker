import pg8000
import psswd

conn = pg8000.connect(user = 'postgres',
	host = 'localhost',
	password = psswd.psswd,
	database = 'jogo')
	
cursor = conn.cursor()

def exe_query(query=str()):
	cursor.execute(query)
	try:
		response = cursor.fetchall()
	except pg8000.exceptions.ProgrammingError:
		return cursor.rowcount
	
	return(response)
	
def add_user(username, email):
	# Verify if exists and if valid
	
	# Add to database
	query = "INSERT INTO  public.jogador (nick, email) VALUES ('%s', '%s')" % (username, email)
	exe_query(query)	
	
query = '''
	SELECT * FROM public.jogador
	ORDER BY id_jogador ASC 
'''

add_user('teste1', 'teste@gmail.com')

bla = exe_query(query)	
print(bla)
