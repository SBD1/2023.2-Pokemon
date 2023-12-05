-- Inserir dados na tabela LOCALIDADE
INSERT INTO LOCALIDADE ( NOME, INFO, MAPA) VALUES
  ( 'Quarto do Treinador', 'Quarto onde o treinador cresceu.', 'Mapa001'),
  ( 'Sala do Treinador', 'Sala da casa do treinador.', 'Mapa002'),
  ( 'Leste de Pallet', 'Canto leste da cidade de pallet onde Ash inicia sua jornada.', 'Mapa003'),
  ( 'Laboratório do professor Oak', 'Laboratório onde Ash recebe seu primeiro pokemon', 'Mapa004'),
  ('Centro Pokémon de Pewter', 'Centro Pokémon localizado na cidade de Pewter.', 'Mapa005'),
  ('PokeMart de Pewter localizado na cidade de Pewter.', 'Pokemart.', 'Mapa006'),
  ('Floresta de Viridian', 'Uma floresta densa localizada perto da cidade de Viridian.', 'Mapa007'),
  ('Ginásio de Brock', 'Ginásio da cidade de Pewter, liderado por Brock, especialista em Pokémon do tipo Pedra.', 'Mapa008'),
  ('Lago Cerulean', 'Um lago sereno próximo à cidade de Cerulean, conhecido por seus Pokémon aquáticos.', 'Mapa009'),
  ('Monte Moon', 'Uma montanha misteriosa e cavernosa onde muitos treinadores encontram Pokémon noturnos.', 'Mapa010'),
  ('Cidade de Saffron', 'Uma cidade movimentada conhecida pelo seu Ginásio de Psíquicos e pelo Silph Co.', 'Mapa011'),
  ('Torre Pokémon de Lavender', 'Uma torre assustadora em Lavender Town, lar de Pokémon Fantasma.', 'Mapa012'),
  ('Ilha Cinnabar', 'Uma ilha vulcânica com um laboratório de Pokémon, conhecida por experimentos.', 'Mapa013');

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
  ('Fogo'), ('Água'), ('Grama'), ('Elétrico'), ('Pedra'), ('Normal');

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
  (1, 'Bulbasaur', 'Grama', Null, 16, 30, 1, 'Kanto', 'Um pequeno Pokémon semente'),
  (2, 'Ivysaur', 'Grama', Null, 36, 30, 1, 'Kanto', 'Um Pokémon semente médio');

-- Inserir dados na tabela EVOLUCAO
INSERT INTO EVOLUCAO (ANTERIOR, SUCESSOR) VALUES
  (1, 2);

-- Inserir dados na tabela REGISTRO_POKEDEX
INSERT INTO REGISTRO_POKEDEX (NUMERO_POKEMON, TREINADOR_ID) VALUES
  (1, 1);

-- Inserir dados na tabela POKEMON
INSERT INTO POKEMON (NUMERO_POKEDEX, TREINADOR_ID, HABILIDADE1, NATURE, NIVEL, HP, DEFESA, ATAQUE, SP_ATAQUE, SP_DEFESA, VELOCIDADE, ACURACIA, SEXO, XP, STATUS, POKEBOLA, ALTURA, PESO, LOCALIZACAO) VALUES
  (1, 1, 1, 'Audaciosa', 5, 25, 15, 20, 18, 18, 20, 90, 'M', 0, 'Saudável', 'Pokebola Comum', 70, 70, 1),
  (1, 1, 1, 'Audaciosa', 5, 25, 15, 20, 18, 18, 20, 90, 'M', 0, 'Saudável', 'Pokebola Comum', 70, 70, 1);

-- Inserir dados na tabela EQUIPE
INSERT INTO EQUIPE (TREINADOR_ID, POKEMON) VALUES
  (1, 1);

-- Inserir dados na tabela BATALHA
INSERT INTO BATALHA (POKEMON1, POKEMON2) VALUES
  (1, 2);

-- Inserir dados na tabela NPC
INSERT INTO NPC (LOCALIDADE, SEXO, INFO) VALUES
  (3, 'F', 'Guia da Cidade Inicial'),
  (4, 'M', 'Professor Oak'),
  (5,'F', 'Enfermeira Joy'),
  (6, 'F', 'Lojista'),
  (8, 'M', 'Brock'),
  (12, 'F', 'Guia em Lavender'),
  

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
  (1, 'Poção', 5, 200);

