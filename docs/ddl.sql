BEGIN TRANSACTION;

CREATE TABLE Treinador (
    treinador_id serial PRIMARY KEY NOT NULL,
    nome_treinador varchar(50) NOT NULL,
    localizacao varchar(12),
    insignias int,
    pokemons_capturados int NOT NULL,
    registros_pokedex int NOT NULL,
    dinheiro int NOT NULL,
    sexo char(1) NOT NULL
);

CREATE TABLE Itens_Comuns(
    nome_item varchar(60) PRIMARY KEY,
    efeito varchar(150)
);

CREATE TABLE Itens_Chave(
    nome_item varchar(60) PRIMARY KEY,
    utilidade varchar(150)
);

CREATE TABLE Frutas(
    nome_item varchar(60) PRIMARY KEY,
    efeito varchar(150)
);

CREATE TABLE Tipo(
    tipo_id serial PRIMARY KEY,
    nome_tipo varchar(10) NOT NULL,
    CONSTRAINT sk_nome_tipo UNIQUE (nome_tipo)
);

CREATE TABLE Efeito(
    efeito_id SERIAL PRIMARY KEY,
    nome_efeito varchar(10) NOT NULL,
    acuracia SMALLINT NOT NULL,
    dano SMALLINT,
    info varchar(150) NOT NULL,
    CONSTRAINT sk_nome_efeito UNIQUE (nome_efeito)
);

CREATE TABLE Habilidade(
    habilidade_id serial PRIMARY KEY,
    nome_habilidade varchar(20) NOT NULL,
    alcance char(1),
    dano SMALLINT,
    tipo int NOT NULL,
    acuracia int NOT NULL,
    efeito SMALLINT,
    info varchar(150) NOT NULL,
    CONSTRAINT nome_habilidade_sk UNIQUE (nome_habilidade),
    CONSTRAINT fk_tipo FOREIGN KEY (tipo) REFERENCES Tipo (tipo_id) ON
DELETE
	RESTRICT ON
	UPDATE
		CASCADE,
		CONSTRAINT fk_efeito FOREIGN KEY (efeito) REFERENCES Efeito (efeito_id) ON
		DELETE
			RESTRICT ON
			UPDATE
				CASCADE
);

CREATE TABLE TMs(
    nome_item varchar(60) PRIMARY KEY,
    habilidade_id int NOT NULL,
    CONSTRAINT habilidade_fk FOREIGN KEY (habilidade_id) REFERENCES Habilidade (habilidade_id),
    CONSTRAINT sk_habilidade UNIQUE (habilidade_id)
);

CREATE TABLE Pokebolas(
    nome_item varchar(60) PRIMARY KEY,
    forca SMALLINT NOT NULL
);

CREATE TABLE Mochila(
    dono int NOT NULL,
    nome_item varchar(60) NOT NULL,
    quantidade SMALLINT,
    origem varchar(15) NOT NULL,
    CONSTRAINT pk_mochila PRIMARY KEY (nome_item),
    CONSTRAINT fk_item_chave FOREIGN KEY (nome_item) REFERENCES Itens_chave(nome_item),
    CONSTRAINT fk_item_comum FOREIGN KEY (nome_item) REFERENCES Itens_comuns(nome_item),
    CONSTRAINT fk_item_tms FOREIGN KEY (nome_item) REFERENCES TMs(nome_item),
    CONSTRAINT fk_item_pokebolas FOREIGN KEY (nome_item) REFERENCES Pokebolas(nome_item),
    CONSTRAINT fk_item_frutas FOREIGN KEY (nome_item) REFERENCES Frutas(nome_item),
    CONSTRAINT unq_dono_mochila UNIQUE (origem),
    CONSTRAINT fk_dono FOREIGN KEY (dono) REFERENCES Treinador (treinador_id)
);

CREATE TABLE Pokedex(
	numero_pokedex int PRIMARY KEY,
	nome_pokemon varchar(20),
	tipo1 int NOT NULL,
	tipo2 int,
	som_emitido int,
	regiao varchar(20),
	info varchar(100),
	pesquisa int,
    CONSTRAINT fk_tipo1_pokedex FOREIGN KEY (tipo1) REFERENCES Tipo (tipo_id) ON
DELETE
	RESTRICT ON
	UPDATE
		CASCADE,
		CONSTRAINT fk_tipo2_pokedex FOREIGN KEY (tipo2) REFERENCES Tipo (tipo_id) ON
		DELETE
			RESTRICT ON
			UPDATE
				CASCADE
);

CREATE TABLE Pokemons_Descobertos(
	numero_pokemon int PRIMARY KEY,
	treinador_id int,
	
	CONSTRAINT fk_numero_pokedex FOREIGN KEY(numero_pokemon) REFERENCES Pokedex(numero_pokedex),
	CONSTRAINT fk_treinador_id FOREIGN KEY (treinador_id) REFERENCES Treinador(treinador_id)

);

CREATE TABLE Pokemon(
    pokemon_id serial PRIMARY KEY,
    numero_pokedex int,
    nature varchar(10) NOT NULL,
    nivel SMALLINT NOT NULL,
    hp SMALLINT NOT NULL,
    defesa SMALLINT NOT NULL,
    habilidade1 varchar(20),
    habilidade2 varchar(20),
    habilidade3 varchar(20),
    habilidade4 varchar(20),
    treinador_id int,
    CONSTRAINT fk_treinador_id FOREIGN KEY (treinador_id) REFERENCES Treinador(treinador_id),
    CONSTRAINT fk_num_pokedex FOREIGN KEY (numero_pokedex) REFERENCES Pokedex(numero_pokedex),
    CONSTRAINT fk_habilidade1 FOREIGN KEY (habilidade1) REFERENCES Habilidade(nome_habilidade),
    CONSTRAINT fk_habilidade2 FOREIGN KEY (habilidade2) REFERENCES Habilidade(nome_habilidade),
    CONSTRAINT fk_habilidade3 FOREIGN KEY (habilidade3) REFERENCES Habilidade(nome_habilidade),
    CONSTRAINT fk_habilidade4 FOREIGN KEY (habilidade4) REFERENCES Habilidade(nome_habilidade)
);

CREATE TABLE Equipe(
    treinador_id int,
    pokemon int,
    CONSTRAINT pk_equipe PRIMARY KEY(treinador_id,
pokemon),
    CONSTRAINT fk_treinador_id FOREIGN KEY(treinador_id) REFERENCES Treinador(treinador_id),
    CONSTRAINT fk_pokemon FOREIGN KEY(pokemon) REFERENCES Pokemon(pokemon_id)
);

CREATE TABLE Batalha(
    batalha_id serial,
    pokemon1 int,
    pokemon2 int,
    CONSTRAINT pk_batalha PRIMARY KEY(batalha_id),
    CONSTRAINT fk_pokemon1 FOREIGN KEY(pokemon1) REFERENCES Pokemon(pokemon_id),
    CONSTRAINT fk_pokemon2 FOREIGN KEY(pokemon2) REFERENCES Pokemon(pokemon_id)
);

CREATE TABLE Lugar(
    localizacao varchar(12) PRIMARY KEY,
    nome varchar(50) NOT NULL,
    x int NOT NULL,
    y int NOT NULL,
    info varchar(255) NOT NULL
);

CREATE TABLE Npc(
    npc_id serial PRIMARY KEY NOT NULL,
    treinador int,
    localidade varchar(12) NOT NULL,
    sexo varchar(1) NOT NULL,
    ginasio varchar(50),
    info varchar(150) NOT NULL,
    CONSTRAINT fk_treinador FOREIGN KEY(treinador) REFERENCES Treinador(treinador_id),
    CONSTRAINT fk_localidade FOREIGN KEY(localidade) REFERENCES Lugar(localizacao)
);

CREATE TABLE Loot(
    loot_id serial PRIMARY KEY,
    nome_item varchar(60) NOT NULL,
    quantidade int NOT NULL,
    localidade varchar(12) NOT NULL,
    CONSTRAINT fk_localidade FOREIGN KEY(localidade) REFERENCES Lugar(localizacao)
);

CREATE TABLE Ginasio(
    nome_ginasio varchar(50) PRIMARY KEY,
    lider_id int NOT NULL,
    tipo1 int NOT NULL,
    tipo2 int,
    cidade varchar(50) NOT NULL,
    loot int NOT NULL,
    CONSTRAINT fk_lider_id FOREIGN KEY(lider_id) REFERENCES Npc(npc_id),
    CONSTRAINT fk_tipo1_gin FOREIGN KEY(tipo1) REFERENCES Tipo(tipo_id),
    CONSTRAINT fk_tipo2_gin FOREIGN KEY(tipo2) REFERENCES Tipo(tipo_id),
    CONSTRAINT fk_cidade FOREIGN KEY(cidade) REFERENCES Lugar(localizacao),
    CONSTRAINT fk_loot FOREIGN KEY(loot) REFERENCES Loot(loot_id)
);

CREATE TABLE Batalhador(
	npc_treinador_id int PRIMARY KEY,
	tipo1 int NOT NULL,
	tipo2 int,
	localidade varchar(12) NOT NULL,
	loot int,
	
	
	CONSTRAINT fk_npc_batalhador FOREIGN KEY(npc_treinador_id) REFERENCES Npc(npc_id),
	CONSTRAINT fk_localidade FOREIGN KEY(localidade) REFERENCES Lugar(localizacao),
	CONSTRAINT fk_tipo1_batalhador FOREIGN KEY(tipo1) REFERENCES Tipo(tipo_id),
	CONSTRAINT fk_tipo2_batalhador FOREIGN KEY(tipo2) REFERENCES Tipo(tipo_id),
	CONSTRAINT fk_loot FOREIGN KEY(loot) REFERENCES Loot(loot_id) 
);

CREATE TABLE PokeCenter(
	pokecenter_id serial PRIMARY KEY,
	cura_disponivel int,
	localidade varchar(12) NOT NULL,
	info varchar(50),

	CONSTRAINT fk_localidade FOREIGN KEY(localidade) REFERENCES Lugar(localizacao)
);

CREATE TABLE EnfermeiraJoy(
	pokecenter_id int,
	npc_id int,

	CONSTRAINT pk_enfermeirajoy PRIMARY KEY(pokecenter_id,
npc_id),
	CONSTRAINT fk_pokecenter_id FOREIGN KEY(pokecenter_id) REFERENCES PokeCenter(pokecenter_id),
	CONSTRAINT fk_npc_id FOREIGN KEY(npc_id) REFERENCES Npc(npc_id)
);

CREATE TABLE PokeMart(
	pokemart_id int PRIMARY KEY,
	itens_disponiveis int,
	localidade varchar(12) NOT NULL,
	info varchar(50),

	CONSTRAINT fk_localidade FOREIGN KEY(localidade) REFERENCES Lugar(localizacao)
);

CREATE TABLE Lojista(
	pokemart_id int ,
	npc_id int,

	CONSTRAINT pk_lojista PRIMARY KEY(pokemart_id,
npc_id),
	CONSTRAINT fk_pokemart_id FOREIGN KEY(pokemart_id) REFERENCES PokeMart(pokemart_id),
	CONSTRAINT fk_npc_id FOREIGN KEY(npc_id) REFERENCES Npc(npc_id)
);

CREATE TABLE Itens_Vendidos(
	pokemart_id int ,
	item_id varchar(60),
	quantidade int,
	preco int,

	CONSTRAINT pk_itens_vendidos PRIMARY KEY(pokemart_id,
item_id),
	CONSTRAINT fk_pokemart_id FOREIGN KEY(pokemart_id) REFERENCES PokeMart(pokemart_id),
	CONSTRAINT fk_item_id FOREIGN KEY(item_id) REFERENCES Itens_Comuns(nome_item)
);

COMMIT;
