import pg8000
import psswd

conn = pg8000.connect(user = 'postgres',
	host = 'localhost',
	password = psswd.psswd,
	database = 'jogo')
	
cursor = conn.cursor()

def executar_query(query=str()):
	cursor.execute(query)
	response = cursor.fetchall()
	return(response)

def executar_query_semValor(query=str()):
	cursor.execute(query)
	return cursor.rowcount
	
	
	
query = '''
	SELECT * FROM public.jogador
	ORDER BY id_jogador ASC 
'''
bla = executar_query(query)	

print(bla)
