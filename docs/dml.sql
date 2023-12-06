-- Inserir dados na tabela LOCALIDADE
INSERT INTO LOCALIDADE (NOME, INFO, MAPA) VALUES
  ( 'Quarto do Treinador', 'Quarto onde o treinador cresceu.', 'Mapa001'),
  ( 'Sala do Treinador', 'Sala da casa do treinador.', 'Mapa002'),
  ( 'Leste de Pallet', 'Canto leste da cidade de pallet onde o Treinador inicia sua jornada.', 'Mapa003'),
  ( 'Laboratório do professor Oak', 'Laboratório onde o treinador recebe seu primeiro pokemon', 'Mapa004'),
  ('Floresta de Viridian', 'Uma floresta densa localizada perto da cidade de Viridian.', 'Mapa005'),
  ('PokeCenter', 'Centro Pokémon localizado na cidade de Pewter.', 'Mapa006'),
  ('PokeMart', 'Pokemart localizado na cidade de Pewter.', 'Mapa007'),
  ('Ginásio de Brock', 'Ginásio da cidade de Pewter, liderado por Brock, especialista em Pokémon do tipo Pedra.', 'Mapa008'),
  ('Rota 4', 'Uma área aberta cheia de árvores e pokémon.', 'Mapa009'),
  ('Monte Moon', 'Uma montanha misteriosa e cavernosa onde muitos treinadores encontram Pokémon noturnos.', 'Mapa010'),
  ('PokeCenter', 'Centro Pokémon localizado na cidade de Cerulean', 'Mapa011'),
  ('PokeMart', 'Pokemart localizado na cidade de Cerulean.', 'Mapa012'),
  ('Ginásio de Misty', 'Ginásio da cidade de Cerulean, liderada por Misty, especialista em Pokémon do tipo Água.', 'Mapa013');

-- Inserir dados na tabela CAMINHO
INSERT INTO CAMINHO (SALA_ATUAL, PROXIMA_SALA) VALUES
  (1, 2),
  (2, 3),
  (3, 4);


insert into tipo_item (nome_item,tipo_item) VALUES
  ('TM01', 'T'),
  ('Pokebola Comum', 'P'),
  ('Fruta Cítrica', 'F'),
  ('Chave da Cidade', 'K'),
  ('Poção', 'C');

-- Inserir dados na tabela TREINADOR
INSERT INTO TREINADOR (NOME_TREINADOR, SEXO, LOCALIZACAO, QUANT_INSIGNIAS, QUANT_PK_CAPTURADOS, DINHEIRO) VALUES
  ('Ash Ketchum', 'M', 1, 0, 0, 1000),
  ('Adivsnoisd', 'F', 1, 0, 0, 1000);

-- Inserir dados na tabela ITEM_COMUM
INSERT INTO ITEM_COMUM (NOME_ITEM, EFEITO) VALUES
  ('Poção', 'Cura 20 pontos de HP');

-- Inserir dados na tabela ITEM_CHAVE
INSERT INTO ITEM_CHAVE (NOME_ITEM, UTILIDADE) VALUES
  ('Chave da Cidade', 'Abre portas na cidade');

-- Inserir dados na tabela FRUTA
INSERT INTO FRUTA (NOME_ITEM, EFEITO) VALUES
  ('Fruta Cítrica', 'Cura paralisia');

-- Inserir dados na tabela TIPO
INSERT INTO TIPO (NOME_TIPO) VALUES
  ('Fogo'), ('Água'), ('Grama'), ('Elétrico'), ('Pedra'), ('Normal'),
  ('Fantasma'), ('Noturno'), ('Aço'), ('Dragão'), ('Veneno'), ('Lutador'), ('Psíquico'), ('Gelo'),
  ('Inseto'), ('Venenoso'), ('Voador'), ('Solo'), ('Rocha'), ('Metálico'), ('Fada'), ('Terra');

-- Inserir dados na tabela EFEITO
INSERT INTO EFEITO (NOME_EFEITO, ACURACIA, DANO, INFO) VALUES
  ('Queimar', 80, 10, 'Causa dano ao longo do tempo');

-- Inserir dados na tabela HABILIDADE
INSERT INTO HABILIDADE (NOME_HABILIDADE, TIPO_DANO, DANO, TIPO, ACURACIA, EFEITO, INFO) VALUES
  ('Investida', 'F', 20, 'Normal', 95, NULL, 'Ataque básico de investida');

-- Inserir dados na tabela TM
INSERT INTO TM (NOME_ITEM, HABILIDADE_ID) VALUES
  ('TM01', 1);

-- Inserir dados na tabela POKEBOLA
INSERT INTO POKEBOLA (NOME_ITEM, FORCA) VALUES
  ('Pokebola Comum', 0);

-- Inserir dados na tabela MOCHILA
INSERT INTO MOCHILA (NOME_ITEM, DONO, QUANTIDADE) VALUES
  ('Poção', 1, 3),
  ('Pokebola Comum', 1, 1);

  -- Inserir dados na tabela POKEDEX
INSERT INTO POKEDEX (NUMERO_POKEDEX, NOME_POKEMON, TIPO1, TIPO2, NIVEL_EVOLUCAO, TAXA_CAPTURA, SOM_EMITIDO, REGIAO, INFO) VALUES
    (1, 'Bulbasaur', 'Grama', 'Venenoso', 16, 45, 5, 'Kanto', 'Conhecido por sua planta nas costas.'),
    (2, 'Ivysaur', 'Grama', 'Venenoso', 32, 45, 5, 'Kanto', 'Quando cresce, sua planta floresce.'),
    (3, 'Venusaur', 'Grama', 'Venenoso', null, 45, 5, 'Kanto', 'Diz-se que floresce em resposta a um grande aumento de energia.'),
    (4, 'Charmander', 'Fogo', null, 16, 45, 4, 'Kanto', 'Chama na ponta da cauda arde brilhantemente.'),
    (5, 'Charmeleon', 'Fogo', null, 36, 45, 4, 'Kanto', 'Quando chama queima mais intensamente, indica que está prestes a evoluir.'),
    (6, 'Charizard', 'Fogo', 'Voador', null, 45, 4, 'Kanto', 'Solta chamas que podem derreter qualquer coisa.'),
    (7, 'Squirtle', 'Água', null, 16, 45, 3, 'Kanto', 'Pequeno e ágil, ele é o Pokémon inicial de água em Kanto.'),
    (8, 'Wartortle', 'Água', null, 36, 45, 3, 'Kanto', 'Cauda comprida e peluda é sinal de boa saúde.'),
    (9, 'Blastoise', 'Água', null, null, 45, 3, 'Kanto', 'Tem canhões de água poderosos nas costas.'),
    (10, 'Caterpie', 'Inseto', null, 7, 255, 1, 'Kanto', 'Evolui para Metapod.'),
    (11, 'Metapod', 'Inseto', null, 10, 120, 1, 'Kanto', 'Evolui para Butterfree.'),
    (12, 'Butterfree', 'Inseto', 'Voador', null, 45, 1, 'Kanto', 'Têm pó que causa sono.'),
    (13, 'Weedle', 'Inseto', 'Venenoso', 7, 255, 1, 'Kanto', 'Evolui para Kakuna.'),
    (14, 'Kakuna', 'Inseto', 'Venenoso', 10, 120, 1, 'Kanto', 'Evolui para Beedrill.'),
    (15, 'Beedrill', 'Inseto', 'Venenoso', null, 45, 1, 'Kanto', 'Muito agressivo, ataca com agulhas envenenadas.'),
    (16, 'Pidgey', 'Normal', 'Voador', 18, 255, 1, 'Kanto', 'Um Pokémon comum encontrado em muitas áreas.'),
    (17, 'Pidgeotto', 'Normal', 'Voador', 36, 120, 1, 'Kanto', 'Gosta de subir até grandes alturas.'),
    (18, 'Pidgeot', 'Normal', 'Voador', null, 45, 1, 'Kanto', 'Suas asas batem com força, criando ventos poderosos.'),
    (19, 'Rattata', 'Normal', null, 20, 255, 4, 'Kanto', 'Rápido e ágil, ele é comum em muitas áreas urbanas.'),
    (20, 'Raticate', 'Normal', null, null, 127, 4, 'Kanto', 'Altamente territorial, pode ser muito agressivo.');

-- Inserir dados na tabela EVOLUCAO
INSERT INTO EVOLUCAO (ANTERIOR, SUCESSOR) VALUES
  (1, 2);

-- Inserir dados na tabela REGISTRO_POKEDEX
INSERT INTO REGISTRO_POKEDEX (NUMERO_POKEMON, TREINADOR_ID) VALUES
  (1, 1);

-- Inserir dados na tabela POKEMON
INSERT INTO POKEMON (NUMERO_POKEDEX, TREINADOR_ID, HABILIDADE1, NATURE, NIVEL, HP, DEFESA, ATAQUE, SP_ATAQUE, SP_DEFESA, VELOCIDADE, SEXO, XP, STATUS, POKEBOLA, ALTURA, PESO, LOCALIZACAO) VALUES
  (1, 1, 1, 'Audaciosa', 5, 25, 15, 20, 18, 18, 20, 'M', 0, 'Saudável', 'Pokebola Comum', 70, 70, 1),
  (1, 1, 1, 'Audaciosa', 5, 25, 15, 20, 18, 18, 20, 'M', 0, 'Saudável', 'Pokebola Comum', 70, 70, 1);

-- Inserir dados na tabela EQUIPE
INSERT INTO EQUIPE (TREINADOR_ID, POKEMON) VALUES
  (1, 1);

-- Inserir dados na tabela BATALHA
INSERT INTO BATALHA (POKEMON1, POKEMON2) VALUES
  (1, 2);

-- Inserir dados na tabela NPC
INSERT INTO NPC (LOCALIDADE, SEXO, INFO) VALUES
  (2, 'F', 'Mãe'),
  (3, 'F', 'Guia da Cidade Inicial'),
  (4, 'M', 'Professor Oak'),
  (5,'M', 'Treinador de Campo'),
  (6, 'F', 'Enfermeira'),
  (7, 'M', 'Lojista'),
  (8, 'M', 'Brock'),
  (9, 'M', 'Treinador da Rota 4'),
  (10, 'M', 'Climber'),
  (11, 'F', 'Enfermeira'),
  (12, 'M', 'Lojista'),
  (13, 'F', 'Misty');
  

-- Inserir dados na tabela LOOT
INSERT INTO LOOT (NOME_ITEM, QUANTIDADE, LOCALIDADE) VALUES
  ('Potion', 1, 1);

-- Inserir dados na tabela GINASIO
INSERT INTO GINASIO (NOME_GINASIO, LIDER_ID, TIPO1, CIDADE, LOOT) VALUES
  ('Ginásio Inicial', 1, 'Água', 1, 1);

-- Inserir dados na tabela POKENPC
INSERT INTO POKENPC (NPC_TREINADOR_ID, TREINADOR, TIPO1, LOCALIDADE, GINASIO, LOOT) VALUES
  (1, 2, 'Água', 1, 'Ginásio Inicial', 1);

-- Inserir dados na tabela POKECENTER
INSERT INTO POKECENTER (CURA_DISPONIVEL, LOCALIDADE, INFO) VALUES
  (3, 1, 'Centro Pokémon da Cidade Inicial');

-- Inserir dados na tabela ENFERMEIRA
INSERT INTO ENFERMEIRA (POKECENTER_ID, NPC_ID) VALUES
  (1, 1);

-- Inserir dados na tabela POKEMART
INSERT INTO POKEMART (POKEMART_ID, LOCALIDADE, INFO) VALUES
  (1, 1, 'PokéMart da Cidade Inicial');

-- Inserir dados na tabela LOJISTA
INSERT INTO LOJISTA (POKEMART_ID, NPC_ID) VALUES
  (1, 2);

-- Inserir dados na tabela CATALOGO_POKEMART
INSERT INTO CATALOGO_POKEMART (POKEMART_ID, ITEM_NOME, QUANTIDADE, PRECO) VALUES
  (1, 'Pokebola Comum', 10, 200),
  (1, 'Poção', 5, 300);
  
