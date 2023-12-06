TRUNCATE treinador RESTART identity cascade;
TRUNCATE localidade RESTART identity cascade;
TRUNCATE pokedex RESTART identity cascade;

-- Inserir dados na tabela LOCALIDADE
INSERT INTO LOCALIDADE (NOME, INFO, MAPA) VALUES
  ( 'Quarto do Treinador', 'Quarto onde o treinador cresceu.', 'Mapa001'),
  ( 'Sala do Treinador', 'Sala da casa do treinador.', 'Mapa002'),
  ( 'Leste de Pallet', 'Canto leste da cidade de pallet onde o Treinador inicia sua jornada.', 'Mapa003'),
  ( 'Laboratório do professor Oak', 'Laboratório onde o treinador recebe seu primeiro pokemon', 'Mapa004'),
  ('Floresta de Viridian', 'Uma floresta densa localizada perto da cidade de Viridian.', 'Mapa005'),
  ('PokeCenter de Pewter', 'Centro Pokémon localizado na cidade de Pewter.', 'Mapa006'),
  ('PokeMart de Pewter', 'Pokemart localizado na cidade de Pewter.', 'Mapa007'),
  ('Ginásio de Brock', 'Ginásio da cidade de Pewter, liderado por Brock, especialista em Pokémon do tipo Pedra.', 'Mapa008'),
  ('Rota 4', 'Uma área aberta cheia de árvores e pokémon.', 'Mapa009'),
  ('Monte Moon', 'Uma montanha misteriosa e cavernosa onde muitos treinadores encontram Pokémon noturnos.', 'Mapa010'),
  ('PokeCenter de Cerulean', 'Centro Pokémon localizado na cidade de Cerulean', 'Mapa011'),
  ('PokeMart de Cerulean', 'Pokemart localizado na cidade de Cerulean.', 'Mapa012'),
  ('Ginásio de Misty', 'Ginásio da cidade de Cerulean, liderada por Misty, especialista em Pokémon do tipo Água.', 'Mapa013');

-- Inserir dados na tabela CAMINHO
SELECT NOVO_CAMINHO('Quarto do Treinador'::VARCHAR(50), 'Sala do Treinador'::VARCHAR(50));
SELECT NOVO_CAMINHO('Sala do Treinador'::VARCHAR(50), 'Leste de Pallet'::VARCHAR(50));
SELECT NOVO_CAMINHO('Leste de Pallet'::VARCHAR(50), 'Laboratório do professor Oak'::VARCHAR(50));

-- Inserir dados na tabela TREINADOR
INSERT INTO TREINADOR (NOME_TREINADOR, SEXO, LOCALIZACAO, QUANT_INSIGNIAS, QUANT_PK_CAPTURADOS, DINHEIRO) VALUES
  ('Ash Ketchum', 'M', 1, 0, 0, 1000),
  ('Murilo', 'F', 1, 0, 0, 1000);

-- Inserir dados na tabela ITEM_COMUM
SELECT NOVO_ITEM_COMUM('Potion'::VARCHAR(60), 'Cura 20 pontos de HP'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Antidote'::VARCHAR(60), 'Cura envenenamento'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Paralyze Heal'::VARCHAR(60), 'Cura paralisia'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Awakening'::VARCHAR(60), 'Acorda o Pokémon de sono'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Burn Heal'::VARCHAR(60), 'Cura queimaduras'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Ice Heal'::VARCHAR(60), 'Cura congelamento'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Full Heal'::VARCHAR(60), 'Cura de todos os status'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Escape Rope'::VARCHAR(60), 'Teleporta para fora de cavernas'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Super Potion'::VARCHAR(60), 'Cura 50 pontos de HP'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Revive'::VARCHAR(60), 'Revive um Pokémon desmaiado'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Max Revive'::VARCHAR(60), 'Revive um Pokémon com HP máximo'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Ultra Ball'::VARCHAR(60), 'Melhora a chance de captura'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Great Ball'::VARCHAR(60), 'Boa para capturar Pokémon'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Max Potion'::VARCHAR(60), 'Cura completamente os pontos de HP'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Hyper Potion'::VARCHAR(60), 'Cura 200 pontos de HP'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Elixir'::VARCHAR(60), 'Restaura alguns PP de todos os golpes'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Max Elixir'::VARCHAR(60), 'Restaura todos os PP de todos os golpes'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('Full Restore'::VARCHAR(60), 'Cura completamente todos os status'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('X Attack'::VARCHAR(60), 'Aumenta o ataque durante uma batalha'::VARCHAR(150));
SELECT NOVO_ITEM_COMUM('X Defense'::VARCHAR(60), 'Aumenta a defesa durante uma batalha'::VARCHAR(150));


-- Inserir dados na tabela ITEM_CHAVE
SELECT NOVO_ITEM_CHAVE('Old Key'::VARCHAR(60), 'Abre portas antigas'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Secret Card'::VARCHAR(60), 'Acesso a áreas secretas'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Magnet Card'::VARCHAR(60), 'Ativa plataformas magnéticas'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Aqua Emblem'::VARCHAR(60), 'Permite o acesso a áreas aquáticas'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Nature Sigil'::VARCHAR(60), 'Interage com elementos naturais'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Tech Pass'::VARCHAR(60), 'Libera dispositivos tecnológicos'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Eon Ticket'::VARCHAR(60), 'Permite o embarque no transporte especial'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Soul Relic'::VARCHAR(60), 'Desbloqueia selos espirituais'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Celestial Key'::VARCHAR(60), 'Abre portais celestiais'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Dimensional Pass'::VARCHAR(60), 'Acesso a dimensões alternativas'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Mystic Rune'::VARCHAR(60), 'Ativa dispositivos místicos'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Ancient Crest'::VARCHAR(60), 'Desbloqueia artefatos antigos'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Shadow Key'::VARCHAR(60), 'Abre passagens sombrias'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Flare Badge'::VARCHAR(60), 'Concede permissão em áreas vulcânicas'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Gale Pass'::VARCHAR(60), 'Libera caminhos em ambientes ventosos'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Frost Charm'::VARCHAR(60), 'Permite atravessar regiões geladas'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Solar Medallion'::VARCHAR(60), 'Interage com dispositivos solares'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Lunar Key'::VARCHAR(60), 'Abre portas à luz da lua'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Terra Talisman'::VARCHAR(60), 'Ativa mecanismos terrestres'::VARCHAR(150));
SELECT NOVO_ITEM_CHAVE('Abyssal Amulet'::VARCHAR(60), 'Permite explorar áreas subaquáticas'::VARCHAR(150));


-- Inserir dados na tabela FRUTA
SELECT NOVA_FRUTA('Oran Berry'::VARCHAR(60), 'Restaura 10 pontos de HP.'::VARCHAR(150));
SELECT NOVA_FRUTA('Sitrus Berry'::VARCHAR(60), 'Restaura 30 pontos de HP.'::VARCHAR(150));
SELECT NOVA_FRUTA('Pecha Berry'::VARCHAR(60), 'Cura envenenamento.'::VARCHAR(150));
SELECT NOVA_FRUTA('Rawst Berry'::VARCHAR(60), 'Cura queimaduras.'::VARCHAR(150));
SELECT NOVA_FRUTA('Cheri Berry'::VARCHAR(60), 'Cura paralisia.'::VARCHAR(150));
SELECT NOVA_FRUTA('Leppa Berry'::VARCHAR(60), 'Restaura 10 PP de um movimento.'::VARCHAR(150));
SELECT NOVA_FRUTA('Persim Berry'::VARCHAR(60), 'Cura confusão.'::VARCHAR(150));
SELECT NOVA_FRUTA('Lum Berry'::VARCHAR(60), 'Cura de qualquer condição.'::VARCHAR(150));
SELECT NOVA_FRUTA('Figy Berry'::VARCHAR(60), 'Restaura HP quando o Pokémon tem menos da metade.'::VARCHAR(150));
SELECT NOVA_FRUTA('Wiki Berry'::VARCHAR(60), 'Restaura HP quando o Pokémon tem menos da metade.'::VARCHAR(150));
SELECT NOVA_FRUTA('Mago Berry'::VARCHAR(60), 'Restaura PP quando o Pokémon tem menos da metade.'::VARCHAR(150));
SELECT NOVA_FRUTA('Aguav Berry'::VARCHAR(60), 'Restaura HP quando o Pokémon tem menos da metade.'::VARCHAR(150));
SELECT NOVA_FRUTA('Iapapa Berry'::VARCHAR(60), 'Restaura HP quando o Pokémon tem menos da metade.'::VARCHAR(150));
SELECT NOVA_FRUTA('Hondew Berry'::VARCHAR(60), 'Aumenta os EVs de Special Attack.'::VARCHAR(150));
SELECT NOVA_FRUTA('Grepa Berry'::VARCHAR(60), 'Aumenta os EVs de Attack.'::VARCHAR(150));
SELECT NOVA_FRUTA('Tamato Berry'::VARCHAR(60), 'Aumenta os EVs de Speed.'::VARCHAR(150));
SELECT NOVA_FRUTA('Cornn Berry'::VARCHAR(60), 'Aumenta os EVs de Special Defense.'::VARCHAR(150));
SELECT NOVA_FRUTA('Magost Berry'::VARCHAR(60), 'Aumenta os EVs de Defense.'::VARCHAR(150));
SELECT NOVA_FRUTA('Rabuta Berry'::VARCHAR(60), 'Aumenta os EVs de HP.'::VARCHAR(150));
SELECT NOVA_FRUTA('Nomel Berry'::VARCHAR(60), 'Aumenta os EVs de Special Attack.'::VARCHAR(150));

-- Inserir dados na tabela TMs
SELECT NOVA_POKEBOLA('Pokeball'::VARCHAR(60), 0::SMALLINT);
SELECT NOVA_POKEBOLA('Greatball'::VARCHAR(60), 40::SMALLINT);
SELECT NOVA_POKEBOLA('Ultraball'::VARCHAR(60), 60::SMALLINT);
SELECT NOVA_POKEBOLA('Masterball'::VARCHAR(60), 100::SMALLINT);
SELECT NOVA_POKEBOLA('Quick Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Dusk Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Nest Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Repeat Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Timer Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Fast Ball'::VARCHAR(60), 30::SMALLINT);
SELECT NOVA_POKEBOLA('Premier Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Heal Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Net Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Dive Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Luxury Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Sport Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Dream Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Friend Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Love Ball'::VARCHAR(60), 20::SMALLINT);
SELECT NOVA_POKEBOLA('Level Ball'::VARCHAR(60), 20::SMALLINT);

-- Inserir dados na tabela TIPO
INSERT INTO TIPO (NOME_TIPO) VALUES-- Inserir dados na tabela TIPO
  ('Fogo'), ('Agua'), ('Grama'), ('Eletrico'), ('Pedra'), ('Normal'),
  ('Fantasma'), ('Noturno'), ('Aço'), ('Dragão'), ('Lutador'), ('Psiquico'), ('Gelo'),
  ('Inseto'), ('Venenoso'), ('Voador'), ('Solo'), ('Rocha'), ('Metalico'), ('Fada'), ('Terra');

-- Inserir dados na tabela EFEITO
INSERT INTO EFEITO (NOME_EFEITO, ACURACIA, DANO, INFO) VALUES
  ('Queimar', 80, 10, 'Causa dano ao longo do tempo');

-- Inserir dados na tabela HABILIDADE
INSERT INTO HABILIDADE (NOME_HABILIDADE, TIPO_DANO, DANO, TIPO, ACURACIA, EFEITO, INFO) VALUES
  ('Tackle', 'F', 20, 'Normal', 95, NULL, 'Ataque básico de investida'),
  ('Ember', 'D', 30, 'Fogo', 90, 'Queimar', 'Dispara uma brasa ardente no oponente'),
  ('Water Gun', 'D', 25, 'Agua', 100, NULL, 'Jato de água pressurizado'),
  ('Razor Leaf', 'D', 22, 'Grama', 95, NULL, 'Lâminas afiadas de folhas lançadas'),
  ('Thunder Shock', 'D', 28, 'Eletrico', 85, NULL, 'Choque elétrico no oponente'),
  ('Rock Smash', 'F', 25, 'Pedra', 90, NULL, 'Soco forte com uma pedra'),
  ('Double Tackle', 'F', 18, 'Normal', 100, NULL, 'Dois investidas rápidas seguidas'),
  ('Gust', 'D', 22, 'Voador', 90, NULL, 'Rajada cortante de vento'),
  ('Roar', 'F', 0, 'Normal', 100, NULL, 'Rugido intimidante para reduzir a defesa'),
  ('Thunderbolt', 'D', 35, 'Eletrico', 85, NULL, 'Raio elétrico poderoso'),
  ('Stone Edge', 'F', 30, 'Pedra', 80, NULL, 'Corte afiado com uma pedra'),
  ('Poison Jab', 'D', 20, 'Venenoso', 90, NULL, 'Golpe com veneno'),
  ('Agility', 'F', 0, 'Normal', 100, NULL, 'Movimento rápido para aumentar a velocidade'),
  ('Petal Blizzard', 'D', 28, 'Grama', 85, NULL, 'Desencadeia um furacão de pétalas afiadas'),
  ('Confusion', 'D', 25, 'Psiquico', 90, NULL, 'Causa confusão na mente do oponente'),
  ('Ice Beam', 'D', 30, 'Gelo', 80, NULL, 'Dispara um raio congelante'),
  ('Sonic Attack', 'F', 22, 'Normal', 95, NULL, 'Ataque sônico rápido de alta frequência'),
  ('Venomous Bite', 'D', 18, 'Venenoso', 100, NULL, 'Mordida com veneno'),
  ('Quick Attack', 'F', 15, 'Normal', 100, NULL, 'Ataque rápido e preciso'),
  ('Surf', 'D', 70, 'Agua', 100, NULL, 'Invoca a força de uma onda contra seu oponente');

-- Inserir dados na tabela TM
  SELECT NOVO_TM('TM01'::VARCHAR(60), 'Tackle'::VARCHAR(20));
  SELECT NOVO_TM('TM02'::VARCHAR(60), 'Ember'::VARCHAR(20));
  SELECT NOVO_TM('TM03'::VARCHAR(60), 'Water Gun'::VARCHAR(20));
  SELECT NOVO_TM('TM04'::VARCHAR(60), 'Razor Leaf'::VARCHAR(20));
  SELECT NOVO_TM('TM05'::VARCHAR(60), 'Thunder Shock'::VARCHAR(20));
  SELECT NOVO_TM('TM06'::VARCHAR(60), 'Rock Smash'::VARCHAR(20));
  SELECT NOVO_TM('TM07'::VARCHAR(60), 'Double Tackle'::VARCHAR(20));
  SELECT NOVO_TM('TM08'::VARCHAR(60), 'Gust'::VARCHAR(20));
  SELECT NOVO_TM('TM09'::VARCHAR(60), 'Roar'::VARCHAR(20));
  SELECT NOVO_TM('TM10'::VARCHAR(60), 'Thunderbolt'::VARCHAR(20));
  SELECT NOVO_TM('TM11'::VARCHAR(60), 'Stone Edge'::VARCHAR(20));
  SELECT NOVO_TM('TM12'::VARCHAR(60), 'Poison Jab'::VARCHAR(20));
  SELECT NOVO_TM('TM13'::VARCHAR(60), 'Agility'::VARCHAR(20));
  SELECT NOVO_TM('TM14'::VARCHAR(60), 'Petal Blizzard'::VARCHAR(20));
  SELECT NOVO_TM('TM15'::VARCHAR(60), 'Confusion'::VARCHAR(20));
  SELECT NOVO_TM('TM16'::VARCHAR(60), 'Ice Beam'::VARCHAR(20));
  SELECT NOVO_TM('TM17'::VARCHAR(60), 'Venomous Bite'::VARCHAR(20));
  SELECT NOVO_TM('TM18'::VARCHAR(60), 'Quick Attack'::VARCHAR(20));
  SELECT NOVO_TM('TM19'::VARCHAR(60), 'Surf'::VARCHAR(20));
  SELECT NOVO_TM('TM20'::VARCHAR(60), 'Sonic Attack'::VARCHAR(20));

-- Inserir dados na tabela MOCHILA
INSERT INTO MOCHILA (NOME_ITEM, DONO, QUANTIDADE) VALUES
  ('Potion', 1, 3),
  ('Pokeball', 1, 1);

-- Inserir dados na tabela POKEDEX
INSERT INTO POKEDEX (NUMERO_POKEDEX, NOME_POKEMON, TIPO1, TIPO2, NIVEL_EVOLUCAO, TAXA_CAPTURA, SOM_EMITIDO, REGIAO, INFO) VALUES
  (1, 'Bulbasaur', 'Grama', 'Venenoso', 16, 45, 5, 'Kanto', 'Conhecido por sua planta nas costas.'),
    (2, 'Ivysaur', 'Grama', 'Venenoso', 32, 45, 5, 'Kanto', 'Quando cresce, sua planta floresce.'),
    (3, 'Venusaur', 'Grama', 'Venenoso', NULL, 45, 5, 'Kanto', 'Diz-se que floresce em resposta a um grande aumento de energia.'),
    (4, 'Charmander', 'Fogo', NULL, 16, 45, 4, 'Kanto', 'Chama na ponta da cauda arde brilhantemente.'),
    (5, 'Charmeleon', 'Fogo', NULL, 36, 45, 4, 'Kanto', 'Quando chama queima mais intensamente, indica que está prestes a evoluir.'),
    (6, 'Charizard', 'Fogo', 'Voador', NULL, 45, 4, 'Kanto', 'Solta chamas que podem derreter qualquer coisa.'),
    (7, 'Squirtle', 'Agua', NULL, 16, 45, 3, 'Kanto', 'Pequeno e ágil, ele é o Pokémon inicial de água em Kanto.'),
    (8, 'Wartortle', 'Agua', NULL, 36, 45, 3, 'Kanto', 'Cauda comprida e peluda é sinal de boa saúde.'),
    (9, 'Blastoise', 'Agua', NULL, NULL, 45, 3, 'Kanto', 'Tem canhões de água poderosos nas costas.'),
    (10, 'Caterpie', 'Inseto', NULL, 7, 255, 1, 'Kanto', 'Evolui para Metapod.'),
    (11, 'Metapod', 'Inseto', NULL, 10, 120, 1, 'Kanto', 'Evolui para Butterfree.'),
    (12, 'Butterfree', 'Inseto', 'Voador', NULL, 45, 1, 'Kanto', 'Têm pó que causa sono.'),
    (13, 'Weedle', 'Inseto', 'Venenoso', 7, 255, 1, 'Kanto', 'Evolui para Kakuna.'),
    (14, 'Kakuna', 'Inseto', 'Venenoso', 10, 120, 1, 'Kanto', 'Evolui para Beedrill.'),
    (15, 'Beedrill', 'Inseto', 'Venenoso', NULL, 45, 1, 'Kanto', 'Muito agressivo, ataca com agulhas envenenadas.'),
    (16, 'Pidgey', 'Normal', 'Voador', 18, 255, 1, 'Kanto', 'Um Pokémon comum encontrado em muitas áreas.'),
    (17, 'Pidgeotto', 'Normal', 'Voador', 36, 120, 1, 'Kanto', 'Gosta de subir até grandes alturas.'),
    (18, 'Pidgeot', 'Normal', 'Voador', NULL, 45, 1, 'Kanto', 'Suas asas batem com força, criando ventos poderosos.'),
    (19, 'Rattata', 'Normal', NULL, 20, 255, 4, 'Kanto', 'Rápido e ágil, ele é comum em muitas áreas urbanas.'),
    (20, 'Raticate', 'Normal', NULL, NULL, 127, 4, 'Kanto', 'Altamente territorial, pode ser muito agressivo.');

-- Inserir dados na tabela EVOLUCAO
INSERT INTO EVOLUCAO (ANTERIOR, SUCESSOR) VALUES
  (1, 2);

-- Inserir dados na tabela REGISTRO_POKEDEX
INSERT INTO REGISTRO_POKEDEX (NUMERO_POKEMON, TREINADOR_ID) VALUES
  (1, 1);

-- Inserir dados na tabela POKEMON
INSERT INTO POKEMON (NUMERO_POKEDEX, TREINADOR_ID,NOME_POKEMON_INS , HABILIDADE1, NATURE, NIVEL, HP, DEFESA, ATAQUE, SP_ATAQUE, SP_DEFESA, VELOCIDADE, SEXO, XP, STATUS, POKEBOLA, ALTURA, PESO, LOCALIZACAO) VALUES
  (1, 1,NULL, 1, 'Audaciosa', 5, 25, 15, 20, 18, 18, 20, 'M', 0, 'Saudável', 'Pokeball', 70, 70, 1),
  (1, 1,NULL, 1, 'Audaciosa', 5, 25, 15, 20, 18, 18, 20, 'M', 0, 'Saudável', 'Pokeball', 70, 70, 1);

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
  ('Ginásio Inicial', 1, 'Agua', 1, 1);

-- Inserir dados na tabela POKENPC
INSERT INTO POKENPC (NPC_TREINADOR_ID, TREINADOR, TIPO1, LOCALIDADE, GINASIO, LOOT) VALUES
  (1, 2, 'Agua', 1, 'Ginásio Inicial', 1);

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
  (1, 'Potion', 5, 200);