--CREATE DATABASE jogo;

CREATE TABLE IF NOT EXISTS public.Jogador(
	ID_jogador BIGSERIAL PRIMARY KEY,
	nick VARCHAR(30) NOT NULL,
	email VARCHAR(40) NOT NULL,
	senha VARCHAR(30) NOT NULL
);

--ALTER TABLE public.Jogador ADD COLUMN ID_jogador BIGSERIAL PRIMARY KEY;

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

CREATE TABLE IF NOT EXISTS public.Amizade(
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

CREATE TABLE IF NOT EXISTS item(
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

create table if not exists public.item(
	id_item BIGINT PRIMARY KEY,
	material VARCHAR(35) not null,
	poder double precision
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

