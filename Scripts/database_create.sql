--create DATABASE jogo;

create table if not exists public.Jogador(
	ID_jogador BIGSERIAL PRIMARY KEY,
	nick VARCHAR(30) not NULL,
	email VARCHAR(40) not NULL,
	senha VARCHAR(30) not NULL
);

--ALTER table public.Jogador ADD COLUMN ID_jogador BIGSERIAL PRIMARY KEY;

INSERT INTO public.jogador  (ID_jogador, nick, senha, email)
VALUES
(1, 'noobmaster', 'noobmaster', 'haroldo.mansur@outlook.com'),
(2, 'doutorabobrinha', 'doutorabobrinha', 'nino@gmail.com'),
(3, 'numero4', 'numero4', 'numero4@knd.com'),
(4, 'mamaefalei', 'mamaefalei', 'mamaefalei@gmail.com'),
(5, 'horacio', 'horacio', 'horacio@panini.com.br'),
(6, 'bolas', 'bolas', 'bolas@mtst.com.br'),
(7, 'couvos', 'couvos', 'couvos.flor@psdb.gov.br'),
(8, 'bananas', 'bananas', 'bananas@gmail.com'),
(9, 'nick', 'senha', 'email'),
(10, 'seumadruga', '12345', 'seu_madruga@gmail.com');

create table if not exists public.Amizade(
	id_jogador1 BIGSERIAL,
	id_jogador2 BIGSERIAL,
	CONSTRAINT fk_jogador1
      FOREIGN KEY(id_jogador1) 
	  REFERENCES public.Jogador(id_jogador),
	CONSTRAINT fk_jogador2
      FOREIGN KEY(id_jogador2) 
	  REFERENCES public.Jogador(id_jogador),
	UNIQUE(id_jogador1, id_jogador2)
);

INSERT INTO public.Amizade(id_jogador1, id_jogador2)
VALUES 
(1, 2),
(2, 4),
(2, 1),
(1, 2),
(2, 4),
(2, 1),
(1, 2),
(2, 4),
(2, 1),
(1, 2),
(2, 4),
(2, 1),
(1, 2),
(2, 4),
(2, 1),
(3, 4);

create table if not exists public.efeito_sonoro(
	id_efeito BIGINT PRIMARY KEY,
	local_arquivo VARCHAR(100) not null,
	descricao VARCHAR(100),
	nome VARCHAR(35) not null
);

INSERT INTO Public.efeito_sonoro (id_efeito, local_arquivo, descricao, nome)
VALUES (4, 'files/songs/smb_gameover.wav', 'Som de fim de jogo', 'Game Over'),
	   (3, 'files/songs/smb_mariodie.wav', 'Som de morte', 'Morte'),
	   (2, 'files/songs/smb_stage_clear.wav', 'Som de fase finalizada', 'Fim'),
	   (1, 'files/songs/smb_warning.wav', 'Som de aviso', 'Aviso');

create table if not exists public.item(
	id_item BIGINT PRIMARY KEY,
	material VARCHAR(35) not null,
	poder double precision
);

INSERT INTO Public.item (id_item, material, poder)
VALUES 
(1, 'Ferro', 100.0),
(2, 'Madeira', 50.0),
(3, 'Arma de fogo', 400.0),
(4, 'Torta', 20.0),
(5, 'Pedra', 70.0),
(6, 'Chicote', 90.0),
(7, 'Prego', 80.0),
(8, 'Mão', 10.0),
(9, 'Marreta biônica', 150.0),
(10, 'Pirula encolhedora', 20.0);

create table if not exists public.conquista(
	id_conquista BIGINT PRIMARY KEY,
	descricao VARCHAR(200) not null
);

INSERT INTO Public.item (id_conquista, descricao)
VALUES 
(1, 'Matou 10 tartarugas'),
(2, 'Completou o jogo na dificuldade difícil'),
(3, 'Conseguiu 10 records de cenários'),
(4, 'Jogu mais de 100 horas de jogo'),
(5, 'Tem mais de 20 amigos no multiplayer'),
(6, 'Possui 10 skins')
(7, 'Conseguiu todos os poderes'),
(8, 'Fez mais de 10 mapas'),
(9, 'Derrorou 100 inimigos'),
(10, 'Nao pegou nenhuma REC');

create table if not exists public.permissao(
	id_permissao bigint primary key,
	tipo varchar(30) not null,
	descricao varchar(100)
);

INSERT INTO Public.permissao (id_permissao, tipo, descricao)
VALUES 
(1, 'Poder', 'Super soco'),
(2, 'Poder', 'Invisibilidade'),
(3, 'Poder', 'Fogo pelos olhos'),
(4, 'Poder', 'Cospir fogo'),
(5, 'Poder', 'Super velocidade'),
(6, 'Poder', 'Magia'),
(7, 'Habilidade', 'Voar'),
(8, 'Habilidade', 'Nadar'),
(9, 'Habilidade', 'Andar sobre as aguas'),
(10, 'Habilidade', 'Pulo duplo');

create table if not exists public.habilidade(
	id_habilidade bigint primary key,
	tipo varchar(30) not null,
	poder double precision
);

INSERT INTO Public.habilidade (id_habilidade, tipo, poder)
VALUES 
(1, 'Super soco', 200.0),
(2, 'Invisibilidade', 200.0),
(3, 'Fogo pelos olhos', 200.0),
(4, 'Cospir fogo', 200.0),
(5, 'Super velocidade', 200.0),
(6, 'Magia', 200.0),
(7, 'Gelo pela boca', 200.0),
(8, 'Soco duplo', 200.0),
(9, 'Punho de aço', 200.0),
(10, 'Socão', 200.0);

create table if not exists public.progresso(
	id_progresso bigint primary key,
	porcentagem_conclusao double precision default 0.0
		constraint porcentagem_menor_um check (porcentagem_conclusao < 1.0)
		constraint porcentagem_maior_zero check (porcentagem_conclusao > 0.0)
);

INSERT INTO public.progresso(id_progresso, porcentagem_conclusao)
VALUES 
(1, 90.0),
(2, 40.0),
(3, 10.0),
(4, 20.0),
(5, 40.0),
(6, 10.0),
(7, 20.0),
(8, 40.0),
(9, 10.0),
(10, 20.0);

create table if not exists public.musica(
	id_musica bigint primary key,
	nome varchar(70) not null,
	autor varchar(70) not null,
	artista varchar(70) not null,
	local_arquivo varchar(100) not null
);

INSERT INTO public.musica(id_musica, nome, autor, artista, local_arquivo)
VALUES 
(1, 'balada', 'mario', 'pedro', 'files/musics/balada.wav'),
(2, 'forro', 'mario', 'pedro', 'files/musics/forro.wav'),
(3, 'triste', 'mario', 'pedro', 'files/musics/triste.wav'),
(4, 'tururu', 'mario', 'pedro', 'files/musics/tururu.wav'),
(5, 'bla', '', 'mario', 'pedro', 'files/musics/bla.wav'),
(6, 'tutistutis', 'mario', 'pedro', 'files/musics/tutistutis.wav'),
(7, 'sofrencia', 'mario', 'pedro', 'files/musics/sofrencia.wav'),
(8, 'gospel', 'mario', 'pedro', 'files/musics/gospel.wav'),
(9, 'rock', 'mario', 'pedro', 'files/musics/rock.wav'),
(10, 'pop', 'mario', 'pedro', 'files/musics/pop.wav');

create table if not exists public.mapa(
	id_mapa bigint primary key,
	nome_mapa varchar(70) not null,
	descricao varchar(100) not null,
	preco double precision default 0.0
		constraint preco_positivo check (preco > 0)
);

INSERT INTO Public.mapa (id_mapa, nome_mapa, descricao, preco)
VALUES 
(1, 'Rio de Janeiro', 'Um mapa onde você pode jogar no Cristo Redentor e ser assaltado por dois caras de moto', 12.20),
(2, 'Vila do Chaves', 'Neste mapa você pode tomar uma xicara de café com a dona Florinda e entrar no barril do Chaves', 15.20),
(3, 'Biênio da POLI', 'Aqui você pode ficar de REC ma metade das disciplinas e pegar DP nas matérias do MAT', 13.20),
(4, 'FAU', 'Aqui você faz maquetes e se perde no prédio principal', 13.20),
(5, 'Metrô de São Paulo', 'Não entre neste mapa durante o horário de pico ou não conseguirá se mexer', 19.20),
(6, 'Floresta Amazonica', 'Corra de uma onça pintada enquanto pula em cipos na floresta', 18.20),
(7, 'Fogo no PCS', 'Corra do nabo enquanto tenta apagar um incendio no PCS', 16.20),
(8, 'Semana de Prova da POLI', 'Fique uma semana sem dormir, enquanto tenta acumular pontos nas provas', 20.20),
(9, 'Três homens em Conflito', 'São três jogadores e um conflito', 14.20),
(10, 'Espaço', 'Você está perdido em Marte e precisa plantar batatas para sobreviver', 12.20);

create table if not exists public.objeto_cenario(
	id_objeto_cenario bigint primary key,
	tipo varchar(70) not null,
	descricao varchar(100) not null,
	altura double precision constraint altura_positiva check (altura > 0),
	comprimento double precision constraint comprimento_positivo check (comprimento > 0),
	posicao_x double precision constraint pos_x_positiva check (posicao_x > 0),
	posicao_y double precision constraint pos_y_positiva check (posicao_y > 0)
);

create table if not exists public.skin(
	id_skin bigint primary key,
	cor_principal varchar(20) not null,
	nome_textura varchar(70) not null,
	local_arquivo varchar(100) not null,
	preco double precision default 0.0 
		constraint preco_positivo check (preco >= 0)
);

INSERT INTO Public.skin (id_skin, cor_principal, nome_textura, local_arquivo, preco)
VALUES 
(1, 'Branco', 'Bomba da paz', 'files/skins/pomba.png', 2.0),
(2, 'Verde', 'Arvore', 'files/skins/arvore.png', 1.0), 
(3, 'Preto', 'Grafite', 'files/skins/grafite.png', 5.0),
(4, 'Vermelho', 'Sangue', 'files/skins/sangue.png', 15.0),
(5, 'Roxo', 'Beringela', 'files/skins/roxo.png', 3.0),
(6, 'Azul', 'Baleia', 'files/skins/baleia.png', 1.0),
(7, 'Branco', 'Toalha', 'files/skins/toalha.png', 1.1),
(8, 'Azul', 'Tomate', 'files/skins/tomate.png', 1.5),
(9, 'Amarelo', 'Raio', 'files/skins/raio.png', 1.5),
(10, 'Vermelho', 'Melancia', 'files/skins/melancia.png', 4.0);

create table if not exists public.personagem(
	id_personagem bigint primary key,
	nome varchar(35) not null,
	descricao varchar(100) not null,
	e_inimigo boolean,
	preco double precision default 0.0 
		constraint preco_positivo check (preco > 0)
);

INSERT INTO Public.personagem (id_personagem, nome, descricao, e_inimigo, preco)
VALUES 
(1, 'Boulos', 'Cuidado Boulos pode invadir o seu cenário', false, 10.0),
(2, 'Seu Madruga', 'Para pagar os 14 meses de aluguel, Seu Madruga faz tudo, menos trabalhar', false, 1.0), 
(3, 'Pica Pau', 'Pica Pau é tão irritante que vai fazer você desistir do jogo', true, 5.0),
(4, 'Kratos', 'O Bom de Guerra, ,Kratos mata seus inimigos sem a menor misericódia', false, 15.0),
(5, 'MC Mirela', 'Com seu falsete desconcetra qualquer inimigo', true, 20.0),
(6, 'Pepe e Nenem', 'Por que voce nao vem ficar comigo, baby?', true, 1.0),
(7, 'Dona Benta', 'Faça bolos para a criançada', false, 1.1),
(8, 'Zeus', 'Joga raio e mata gente', true, 1.5),
(9, 'Dona Florinda', 'Com seu super tapa derrota qualquer inimigo', false, 1.5),
(10, 'Professor Girafales', 'TA TA TA TA TA', true, 3.0);

create table if not exists public.fala(
	id_fala bigint primary key,
	descricao varchar(100) not null,
	local_arquivo varchar(100) not null
);

create table if not exists public.habilidade_permissao(
	id_habilidade bigserial,
	id_permissao bigserial,
	constraint fk_habilidade
		foreign key(id_habilidade)
		references public.habilidade(id_habilidade),
	constraint fk_permissao
		foreign key(id_permissao)
		references public.permissao(id_permissao)
);

create table if not exists public.habilidade_jogador(
	id_habilidade bigserial,
	id_jogador bigserial,
	habilitado boolean,
	constraint fk_habilidade
		foreign key(id_habilidade)
		references public.habilidade(id_habilidade),
	constraint fk_jogador
		foreign key(id_jogador)
		references public.jogador(id_jogador)
);

INSERT INTO Public.habilidade_jogador (id_jogador, id_habilidade, habilitado)
VALUES 
(12, 1, true),
(12, 2, true),
(12, 3, true),
(12, 4, true),
(12, 7, true),
(12, 6, true),
(13, 8, true),
(13, 9, true),
(13, 10, true),
(14, 5, true),
(14, 7, true),
(14, 8, true),
(15, 3, true),
(15, 4, true),
(15, 5, true),
(16, 1, true),
(16, 2, true),
(16, 3, true),
(17, 4, true),
(17, 6, true),
(17, 7, true),
(18, 8, true),
(18, 9, true),
(18, 6, true),
(19, 4, true),
(19, 3, true),
(19, 2, true),
(19, 1, true),
(19, 4, true),
(19, 6, true);

create table if not exists public.item_jogador(
	id_item bigserial,
	id_jogador bigserial,
	constraint fk_item
		foreign key(id_item)
		references public.item(id_item),
	constraint fk_jogador
		foreign key(id_jogador)
		references public.jogador(id_jogador)
);

INSERT INTO Public.item_jogador (id_jogador, id_item)
VALUES 
(12, 1),
(12, 2),
(12, 3),
(12, 4),
(12, 7),
(12, 6),
(13, 8),
(13, 9),
(13, 10),
(14, 5),
(14, 7),
(14, 8),
(15, 3),
(15, 4),
(15, 5),
(16, 1),
(16, 2),
(16, 3),
(17, 4),
(17, 6),
(17, 7),
(18, 8),
(18, 9),
(18, 6),
(19, 4),
(19, 3),
(19, 2),
(19, 1),
(19, 4),
(19, 6);

create table if not exists public.efeito_sonoro_conquista(
	id_conquista bigserial,
	id_efeito bigserial,
	constraint fk_conquista
		foreign key(id_conquista)
		references public.conquista(id_conquista),
	constraint fk_efeito
		foreign key(id_efeito)
		references public.efeito_sonoro(id_efeito)
);

create table if not exists public.conquista_jogador(
	id_conquista bigserial,
	id_jogador bigserial,
	constraint fk_conquista
		foreign key(id_conquista)
		references public.conquista(id_conquista),
	constraint fk_jogador
		foreign key(id_jogador)
		references public.jogador(id_jogador)
);

create table if not exists public.progresso_jogador(
	id_progresso bigserial,
	id_jogador bigserial,
	pontuacao int not null,
	data_progresso date not null,
	constraint fk_progresso
		foreign key(id_progresso)
		references public.progresso(id_progresso),
	constraint fk_jogador
		foreign key(id_jogador)
		references public.jogador(id_jogador)
);

create table if not exists public.requisito_habilidade(
	id_habilidade bigserial,
	id_requisito bigserial,
	constraint fk_habilidade
		foreign key(id_habilidade)
		references public.habilidade(id_habilidade),
	constraint fk_requisito
		foreign key(id_requisito)
		references public.habilidade(id_habilidade)
);

create table if not exists public.requisito_habilidade(
	id_habilidade bigserial,
	id_requisito bigserial,
	constraint fk_habilidade
		foreign key(id_habilidade)
		references public.habilidade(id_habilidade),
	constraint fk_requisito
		foreign key(id_requisito)
		references public.habilidade(id_habilidade)
);

create table if not exists public.musica_mapa(
	id_musica bigserial,
	id_mapa bigserial,
	constraint fk_musica
		foreign key(id_musica)
		references public.musica(id_musica),
	constraint fk_mapa
		foreign key(id_mapa)
		references public.mapa(id_mapa)
);

create table if not exists public.objeto_mapa(
	id_objeto bigserial,
	id_mapa bigserial,
	constraint fk_objeto
		foreign key(id_objeto)
		references public.objeto_cenario(id_objeto_cenario),
	constraint fk_mapa
		foreign key(id_mapa)
		references public.mapa(id_mapa)
);

create table if not exists public.requisito_mapa(
	id_mapa bigserial,
	id_requisito bigserial,
	constraint fk_mapa
		foreign key(id_mapa)
		references public.mapa(id_mapa),
	constraint fk_requisito
		foreign key(id_requisito)
		references public.mapa(id_mapa)
);

create table if not exists public.personagem_mapa(
	id_mapa bigserial,
	id_personagem bigserial,
	constraint fk_mapa
		foreign key(id_mapa)
		references public.mapa(id_mapa),
	constraint fk_personagem
		foreign key(id_personagem)
		references public.personagem(id_personagem)
);

create table if not exists public.fala_personagem(
	id_fala bigserial,
	id_personagem bigserial,
	constraint fk_fala
		foreign key(id_fala)
		references public.fala(id_fala),
	constraint fk_personagem
		foreign key(id_personagem)
		references public.personagem(id_personagem)
);

create table if not exists public.skin_personagem(
	id_skin bigserial,
	id_personagem bigserial,
	constraint fk_skin
		foreign key(id_skin)
		references public.skin(id_skin),
	constraint fk_personagem
		foreign key(id_personagem)
		references public.personagem(id_personagem)
);

create table if not exists public.skin_jogador(
	id_skin bigserial,
	id_jogador bigserial,
	constraint fk_skin
		foreign key(id_skin)
		references public.skin(id_skin),
	constraint fk_jogador
		foreign key(id_jogador)
		references public.jogador(id_jogador)
);

create table if not exists public.skin_objeto(
	id_skin bigserial,
	id_objeto bigserial,
	constraint fk_skin
		foreign key(id_skin)
		references public.skin(id_skin),
	constraint fk_objeto
		foreign key(id_objeto)
		references public.objeto_cenario(id_objeto_cenario)
);

