--create DATABASE jogo;

create table if not exists public.Jogador(
	ID_jogador BIGSERIAL PRIMARY KEY,
	nick VARCHAR(30) not NULL,
	email VARCHAR(40) not NULL,
	senha VARCHAR(30) not NULL
);

--ALTER table public.Jogador ADD COLUMN ID_jogador BIGSERIAL PRIMARY KEY;

INSERT INTO public.jogador  (nick, senha, email)
VALUES
('noobmaster', 'noobmaster', 'haroldo.mansur@outlook.com'),
('doutorabobrinha', 'doutorabobrinha', 'nino@gmail.com'),
('numero4', 'numero4', 'numero4@knd.com'),
('mamaefalei', 'mamaefalei', 'mamaefalei@gmail.com'),
('horacio', 'horacio', 'horacio@panini.com.br'),
('bolas', 'bolas', 'bolas@mtst.com.br'),
('couvos', 'couvos', 'couvos.flor@psdb.gov.br'),
('nick', 'senha', 'email');

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
VALUES (1, 2), (2, 4), (2, 1), (3, 4);

create table if not exists item(
	ID_item BIGSERIAL PRIMARY KEY,
	ID_jogador BIGSERIAL REFERENCES public.jogador(ID_Jogador)
);

INSERT INTO Public.item (id_jogador)
VALUES (4), (5), (3), (1), (2);

SELECT j.id_jogador, j.nick, j.email, i.id_item
FROM public.jogador j
inner join public.item i
on j.id_jogador = i.id_jogador;


create table if not exists public.efeito_sonoro(
	id_efeito BIGINT PRIMARY KEY,
	local_arquivo VARCHAR(100) not null,
	descricao VARCHAR(100),
	nome VARCHAR(35) not null
);

INSERT INTO Public.efeito_sonoro (id_efeito, local_arquivo, descricao, nome)
VALUES (4, 'files\songs\smb_gameover.wav', 'Som de fim de jogo', 'Game Over'),
	   (3, 'files\songs\smb_mariodie.wav', 'Som de morte', 'Morte'),
	   (2, 'files\songs\smb_stage_clear.wav', 'Som de fase finalizada', 'Fim'),
	   (1, 'files\songs\smb_warning.wav', 'Som de aviso', 'Aviso');

create table if not exists public.item(
	id_item BIGINT PRIMARY KEY,
	material VARCHAR(35) not null,
	poder double precision
);

create table if not exists public.conquista(
	id_conquista BIGINT PRIMARY KEY,
	descricao VARCHAR(200) not null
);

create table if not exists public.permissao(
	id_permissao bigint primary key,
	tipo varchar(30) not null,
	descricao varchar(100)
);

create table if not exists public.habilidade(
	id_habilidade bigint primary key,
	tipo varchar(30) not null,
	poder double precision
);

create table if not exists public.progresso(
	id_progresso bigint primary key,
	porcentagem_conclusao double precision default 0.0
		constraint porcentagem_menor_um check (porcentagem_conclusao < 1.0)
		constraint porcentagem_maior_zero check (porcentagem_conclusao > 0.0)
);

create table if not exists public.musica(
	id_musica bigint primary key,
	nome varchar(70) not null,
	autor varchar(70) not null,
	artista varchar(70) not null,
	local_arquivo varchar(100) not null
);

create table if not exists public.mapa(
	id_mapa bigint primary key,
	nome_mapa varchar(70) not null,
	descricao varchar(100) not null,
	preco double precision default 0.0
		constraint preco_positivo check (preco > 0)
);

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
		constraint preco_positivo check (preco > 0)
);


create table if not exists public.personagem(
	id_personagem bigint primary key,
	nome varchar(35) not null,
	descricao varchar(100) not null,
	e_inimigo boolean,
	preco double precision default 0.0 
		constraint preco_positivo check (preco > 0)
);

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

