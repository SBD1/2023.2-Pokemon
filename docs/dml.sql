-- Inserir dados na tabela "Treinador"
INSERT INTO Treinador (treinador_id, nome_treinador, localizacao, insignias, pokemons_capturados, registros_pokedex, dinheiro, sexo)
VALUES (1, 'Ash', 'Pallet', 8, 151, 151, 10000, 'M');

-- Inserir dados na tabela "Itens_Comuns"
INSERT INTO Itens_Comuns (nome_item, efeito)
VALUES ('Potion', 'Restaura 20 HP de um Pokémon');

-- Inserir dados na tabela "Itens_Chave"
INSERT INTO Itens_Chave (nome_item, utilidade)
VALUES ('Bike', 'Permite que o treinador se mova mais rápido');

-- Inserir dados na tabela "Frutas"
INSERT INTO Frutas (nome_item, efeito)
VALUES ('Oran Berry', 'Restaura 10 HP quando consumida');

-- Inserir dados na tabela "Tipo"
INSERT INTO Tipo (tipo_id, nome_tipo)
VALUES (1, 'Fogo');

-- Inserir dados na tabela "Efeito"
INSERT INTO Efeito (efeito_id, nome_efeito, acuracia, dano, info)
VALUES (1, 'Queimadura', 85, 20, 'Causa dano ao longo do tempo');

-- Inserir dados na tabela "Habilidade"
INSERT INTO Habilidade (habilidade_id, nome_habilidade, alcance, dano, tipo, acuracia, efeito, info)
VALUES (1, 'Ember', 'P', 40, 1, 100, 1, 'Lança pequenas chamas no oponente');

-- Inserir dados na tabela "TMs"
INSERT INTO TMs (nome_item, habilidade_id)
VALUES ('TM35', 1);

-- Inserir dados na tabela "Pokebolas"
INSERT INTO Pokebolas (nome_item, forca)
VALUES ('Ultra Ball', 2);

-- Inserir dados na tabela "Mochila"
INSERT INTO Mochila (dono, nome_item, quantidade, origem)
VALUES (1, 'Ultra Ball', 5, 'Pokebolas');

-- Inserir dados na tabela "Pokemon"
INSERT INTO Pokemon (pokemon_id, numero_pokedex, nature, nivel, hp, defesa, habilidade1, treinador_id)
VALUES (1, 25, 'Brave', 50, 150, 75, 'Ember', 1);

-- Inserir dados na tabela "Equipe"
INSERT INTO Equipe (treinador_id, pokemon)
VALUES (1, 1);

-- Inserir dados na tabela "Batalha"
INSERT INTO Batalha (batalha_id, pokemon1, pokemon2)
VALUES (1, 1, 1);

-- Inserir dados na tabela "Lugar"
INSERT INTO Lugar (localizacao, nome, x, y, info)
VALUES ('Pallet', 'Pallet Town', 10, 20, 'Uma cidade tranquila');

-- Inserir dados na tabela "Npc"
INSERT INTO Npc (npc_id, treinador, localidade, sexo, ginasio, info)
VALUES (1, 1, 'Pallet', 'M', 'Gym Leader', 'Líder do Ginásio');

-- Inserir dados na tabela "Tipos"
INSERT INTO Tipos (tipo_id, nome_tipo)
VALUES ('Fogo', 'Fogo');

-- Inserir dados na tabela "Loot"
INSERT INTO Loot (loot_id, nome_item, quantidade, localidade)
VALUES (1, 'Potion', 3, 'Pallet');

-- Inserir dados na tabela "Ginasio"
INSERT INTO Ginasio (nome_ginasio, lider_id, tipo1, tipo2, cidade, loot)
VALUES ('Gym Leader', 1, 'Fogo', 'Fogo', 'Pallet', 1);

-- Inserir dados na tabela "Batalhador"
INSERT INTO Batalhador (npc_treinador_id, tipo1, localidade, loot)
VALUES (1, 'Fogo', 'Pallet', 1);

-- Inserir dados na tabela "PokeCenter"
INSERT INTO PokeCenter (pokecenter_id, cura_disponivel, localidade, info)
VALUES (1, 3, 'Pallet', 'Centro de Cura Pokémon');

-- Inserir dados na tabela "EnfermeiraJoy"
INSERT INTO EnfermeiraJoy (pokecenter_id, npc_id)
VALUES (1, 1);

-- Inserir dados na tabela "PokeMart"
INSERT INTO PokeMart (pokemart_id, itens_disponiveis, localidade, info)
VALUES (1, 5, 'Pallet', 'Loja de Itens Pokémon');

-- Inserir dados na tabela "Lojista"
INSERT INTO Lojista (pokemart_id, npc_id)
VALUES (1, 1);

-- Inserir dados na tabela "Itens_Vendidos"
INSERT INTO Itens_Vendidos (pokemart_id, item_id, quantidade, preco)
VALUES (1, 'Potion', 10, 200);

-- Inserir dados na tabela "Pokemons_Descobertos"
INSERT INTO Pokemons_Descobertos (numero_pokemon, treinador_id)
VALUES (25, 1);

-- Inserir dados na tabela "Pokedex"
INSERT INTO Pokedex (numero_pokedex, nome_pokemon, tipo1, regiao, info, pesquisa)
VALUES (25, 'Pikachu', 'Elétrico', 'Kanto', 'Rato elétrico amarelo', 0);

SELECT * FROM Mochila, Pokemon, Treinador