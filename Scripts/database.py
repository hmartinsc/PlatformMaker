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
	
def user_exists(username, email):
	query = "SELECT * FROM public.jogador WHERE nick = '%s' AND email = '%s'"
	print(query % (username, email))
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
