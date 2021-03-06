import pg8000
import psswd
from playsound import playsound

conn = pg8000.connect(user='postgres',
                      host='localhost',
                      password=psswd.psswd,
                      database='jogo')

conn.autocommit = True
cursor = conn.cursor()


class Screen():

    def __init__(self, params):
        self.layout = params['layout']()  # Execute function of layout
        self.title = params['title']

        self.window = sg.Window(self.title, self.layout,
                                size=(800, 600))  # Window Defintion

        # Behaviour -> retorna status da tela
        self.window_behaviour = params['behaviour']

    def display(self):
        #print('Displaying screen')
        return self.window_behaviour(self.window)

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


def add_user(username, email, password):
    # Verify if is valid!!!!!

    # Add to database
    query = "INSERT INTO  public.jogador (nick, email, senha) VALUES ('%s', '%s', '%s')" % (
        username, email, password)
    exe_query(query)


def list_friends(email):
    query = '''
		WITH l_amizades AS 
		(
			SELECT j1.nick n1, j1.email em1, j2.nick n2, j2.email em2
			FROM public.Amizade am
			INNER JOIN public.Jogador j1
			ON j1.id_jogador = am.id_jogador1
			INNER JOIN public.Jogador j2
			ON j2.id_jogador = am.id_jogador2
		)
		SELECT n1 FROM l_amizades WHERE em2 = '%s'
		UNION
		SELECT n2 FROM l_amizades WHERE em1 = '%s'
	'''
    print(query % (email, email))
    return exe_query(query % (email, email))
     
def list_items(id_jogador):
    query = '''
		SELECT i.material, i.poder
		FROM public.item i
		INNER JOIN public.item_jogador ij
		ON ij.id_item = i.id_item
		INNER JOIN public.jogador j
		ON ij.id_jogador = j.id_jogador
		WHERE j.id_jogador = '%s'
	'''
    print(query % (id_jogador))
    return exe_query(query % (id_jogador))
    
def list_habilidades(id_jogador):
    query = '''
        SELECT h.tipo, h.poder
        FROM public.habilidade h
        INNER JOIN public.habilidade_jogador hj
        ON hj.id_habilidade = h.id_habilidade
        INNER JOIN public.jogador j
        ON hj.id_jogador = j.id_jogador
        WHERE j.id_jogador = '%s' AND hj.habilitado = true
    '''
    print(query % (id_jogador))
    return exe_query(query % (id_jogador))

def list_skins_jogador(id_jogador):
    query = '''
		SELECT s.cor_principal, s.nome_textura, s.local_arquivo
		FROM public.skin s
		INNER JOIN public.skin_jogador sj
		ON sj.id_skin = s.id_skin
		INNER JOIN public.jogador j
		ON sj.id_jogador = j.id_jogador
		WHERE j.id_jogador = '%s'
	'''
    print(query % (id_jogador))
    return exe_query(query % (id_jogador))

def add_friend(email1, email2):
    query = '''
		INSERT INTO public.Amizade
		VALUES
		(
			(
				SELECT id_jogador 
				FROM public.Jogador
				WHERE email = '%s'
			),
			(
				SELECT id_jogador
				FROM public.Jogador
				WHERE email = '%s'
			)
		)
	'''
    print(query % (email1, email2))
    try:
        exe_query(query % (email1, email2))
    except pg8000.exceptions.IntegrityError:
        print("AMigo ja adicionado")
        pass  # Adicionou quem ja era amigo
        
def list_maps():
    query = '''
		SELECT nome_mapa, descricao, preco
		FROM public.mapa
	'''
    print(query)
    return exe_query(query)
    
def list_characters():
    query = '''
		SELECT nome, descricao, e_inimigo, preco
		FROM public.personagem
	'''
    print(query)
    return exe_query(query)
    
def list_skins():
    query = '''
		SELECT cor_principal, nome_textura, local_arquivo, preco
		FROM public.skin
	'''
    print(query)
    return exe_query(query)

def add_song(name, author, artist, file_path):
    # TODO: Add withou pass id

    # Add to database
    query = "INSERT INTO  public.musica (nome, autor, artista, local_arquivo) VALUES ('%s', '%s', '%s', '%s')" % (
        name, author, artist, file_path)
    exe_query(query)
    
def list_songs():

    query = "select nome from efeito_sonoro"
    
    return exe_query(query)
    
def get_song(name):
    query = "select local_arquivo from efeito_sonoro where nome = '%s'"
    
    song_path = exe_query(query % (name))
    
    if len(song_path) > 0:
        playsound(song_path[0][0])


if __name__ == '__main__':
    username = "noobmaster"
    email = "haroldo.mansur@outlook.com"

    if user_exists(username, email):
        print("User exists")
    else:
        print("User not found")

    emails = [('haroldo.mansur@outlook.com'),
              ('nino@gmail.com'),
              ('numero4@knd.com'),
              ('mamaefalei@gmail.com'),
              ('horacio@panini.com.br'),
              ('bolas@mtst.com.br'),
              ('couvos.flor@psdb.gov.br')]

    for el in emails:
        add_friend(el, 'email')
