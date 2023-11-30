-- TSP POKEDEX

CREATE OR REPLACE
FUNCTION CHECA_TIPO_POKEMON() RETURNS TRIGGER AS $checa_tipo_pokemon$
declare
	id_tipo Integer;
begin
	select Count(*) into id_tipo from Tipo where tipo_id = NEW.tipo1 or tipo_id = new.tipo2;
	if id_tipo < 1 or (id_tipo < 2 and new.tipo2 <> NULL) then
		Raise exception 'Tipo do pokemon inválido';
		return null;
	end if;

	return new;
END;
$checa_tipo_pokemon$ LANGUAGE PLPGSQL;
CREATE OR REPLACE
FUNCTION EVOLUI_POKEMON(ID_EVOLUIDO int, NUM_POKEDEX_EV int) RETURNS VOID AS $evolui_pokemon$
declare
	prox_pokedex int;
begin 
	select sucessor into prox_pokedex from evolucoes where antecessor = num_pokedex_ev;
	INSERT into pokemon (
		 numero_pokedex,
		 treinador_id,
		 habilidade1,
		 habilidade2,
		 habilidade3,
		 habilidade4,
		 nature,nivel,
		 nivel_evolucao,
		 hp,
		 defesa,
		 ataque,
		 sp_ataque,
		 sp_defesa,
		 velocidade,
		 acuracia,
		 sexo,
		 status,
		 pokebola,
		 taxa_captura,
		 altura,
		 peso,
		 localizacao)
		 VALUES (
		 prox_pokedex,
		 (select treinador_id,habilidade1,habilidade2,habilidade3,habilidade4,nature,nivel,xp from pokemon where pokemon_id = id_evoluido),
		 (select nivel_evolucao from pokedex where numero_pokedex = prox_pokedex),
		 (select hp,defesa,ataque,sp_ataque,sp_defesa,velocidade,acuracia,sexo,status,pokebola from pokemon where pokemon_id = id_evoluido),
		 (select taxa_captura from pokedex where numero_pokedex = prox_pokedex),
		 (select altura,peso,localizacao from pokemon where pokemon_id = id_evoluido)
		 );
END;
$evolui_pokemon$ LANGUAGE PLPGSQL;
DROP
FUNCTION GANHA_BATALHA(integer);
CREATE OR REPLACE
FUNCTION GANHA_BATALHA(VENCEDOR int) RETURNS VOID AS $ganha_batalha$
declare
	xp_atual smallint;
	nivel_atual smallint;
	nivel_ev SMALLINT;
begin 
	-- vencedor = pokemon id do vencedor
	select xp into xp_atual from pokemon where pokemon_id = vencedor;
	if xp_atual + 10 >= 100 then
		select nivel_evolucao into nivel_ev from pokedex where numero_pokedex = (select numero_pokedex from pokemon where pokemon_id = vencedor);
		select nivel into nivel_atual from pokemon where pokemon_id = vencedor;
		IF nivel_ev = nivel_atual + 1 THEN
			update pokemon set pokemon.nivel = pokemon.nivel+1, pokemon.xp = pokemon.xp+10-100 WHERE pokemon.pokemon_id = pokemon;
			select evolui_pokemon(vencedor,(select numero_pokedex from pokemon where pokemon_id = vencedor));
			return;
		END IF;
		update pokemon set pokemon.nivel = pokemon.nivel+1, pokemon.xp = pokemon.xp+10-100 WHERE pokemon.pokemon_id = pokemon;
	else
		update pokemon set pokemon.xp = pokemon.xp+10 WHERE pokemon.pokemon_id = pokemon;
	end if;
END;
$ganha_batalha$ LANGUAGE PLPGSQL;
DROP TRIGGER IF EXISTS CHECADOR_TIPOS
				ON POKEDEX;
DROP TRIGGER IF EXISTS CHECADOR_TIPOS
				ON GINASIO;
DROP TRIGGER IF EXISTS CHECADOR_TIPOS
				ON BATALHADOR;
CREATE TRIGGER CHECADOR_TIPOS

BEFORE
INSERT

				OR
UPDATE
				ON POKEDEX

			FOR EACH ROW EXECUTE PROCEDURE CHECA_TIPO_POKEMON();
CREATE TRIGGER CHECADOR_TIPOS

BEFORE
INSERT

				OR
UPDATE
				ON GINASIO

			FOR EACH ROW EXECUTE PROCEDURE CHECA_TIPO_POKEMON();
CREATE TRIGGER CHECADOR_TIPOS

BEFORE
INSERT

				OR
UPDATE
				ON BATALHADOR

			FOR EACH ROW EXECUTE PROCEDURE CHECA_TIPO_POKEMON();

-- TSP BATALHA

CREATE OR REPLACE
FUNCTION CHECK_NOVA_BATALHA() RETURNS TRIGGER AS $check_nova_batalha$
DECLARE
	pokemons_existentes INTEGER;
BEGIN 
	SELECT COUNT(*) INTO pokemons_existentes FROM pokemon WHERE pokemon_id = NEW.pokemon1 OR pokemon_id = NEW.pokemon2;
	IF pokemons_existentes < 2 THEN
		RAISE EXCEPTION 'Pokemons inválidos';
		RETURN NULL;
	END IF;
	RETURN NEW;
END;
$check_nova_batalha$ LANGUAGE PLPGSQL;
CREATE OR REPLACE
FUNCTION DESCOBRE_POKEMON() RETURNS TRIGGER AS $descobre_pokemon$
DECLARE
	treinador INTEGER;
	numero_dex INTEGER;
	quant_descoberto INTEGER;
BEGIN 
	select treinador_id into treinador from pokemon WHERE pokemon.pokemon_id = new.pokemon1;
	select numero_pokedex into numero_dex from pokemon where pokemon.pokemon_id = NEW.pokemon1;
	select count(*) into quant_descoberto from pokemons_descobertos WHERE treinador_id = treinador and numero_pokemon = numero_dex;
	if quant_descoberto = 0 then
		INSERT into pokemons_descobertos (treinador_id,numero_pokemon) values (treinador,numero_dex);
	end if;

	select numero_pokedex into numero_dex from pokemon where pokemon.pokemon_id = NEW.pokemon2;
	select count(*) into quant_descoberto from pokemons_descobertos WHERE treinador_id = treinador and numero_pokemon = numero_dex;
	if quant_descoberto = 0 then
		INSERT into pokemons_descobertos (treinador_id,numero_pokemon) values (treinador,numero_dex);
	end if;
	RETURN NEW;
END;
$descobre_pokemon$ LANGUAGE PLPGSQL;
DROP TRIGGER IF EXISTS NOVA_BATALHA
				ON BATALHA;
CREATE TRIGGER NOVA_BATALHA

BEFORE
INSERT

				OR
UPDATE
				ON BATALHA

			FOR EACH ROW EXECUTE PROCEDURE CHECK_NOVA_BATALHA();
DROP TRIGGER IF EXISTS REGISTRA_POKEMON
				ON BATALHA;
CREATE TRIGGER REGISTRA_POKEMON AFTER
INSERT
OR
UPDATE
ON BATALHA

			FOR EACH ROW EXECUTE PROCEDURE DESCOBRE_POKEMON();

-- SP ataca

CREATE OR REPLACE
FUNCTION ATACA_BATALHA(POKEMON1 int, POKEMON2 int, ID_HABILIDADE int) RETURNS VOID AS $ataca_batalha$
declare
	vida_pokemon smallint;
	dano_habilidade smallint;
BEGIN 
	select hp into vida_pokemon from pokemon where pokemon.pokemon_id = pokemon2;
	select dano into dano_habilidade from habilidade where habilidade.habilidade_id = id_habilidade;

	if dano_habilidade > vida_pokemon then
		update pokemon set hp = 0, status = 'Desmaiado' where pokemon.pokemon_id = pokemon2;
		select ganha_batalha(pokemon1);
	else
		update pokemon set hp = vida_pokemon-dano_habilidade where pokemon.pokemon_id = pokemon2;
	end if;
END;
$ataca_batalha$ LANGUAGE PLPGSQL;

-- SP captura

CREATE OR REPLACE
FUNCTION CAPTURA_POKEMON(POKEMON int, POKEBOLA VARCHAR(60),TREINADOR int) RETURNS VOID AS $captura_pokemon$
BEGIN 
	update pokemon set pokemon.treinador = treinador, pokemon.pokebola = pokebola WHERE pokemon.pokemon_id = pokemon;

END;
$captura_pokemon$ LANGUAGE PLPGSQL;
CREATE OR REPLACE
FUNCTION JOGA_POKEBOLA(POKEMON int, POKEBOLA VARCHAR(60),TREINADOR int) RETURNS VOID AS $joga_pokebola$
DECLARE
	consegue BOOLEAN;
	taxa_cap smallint;
BEGIN
	if (select treinador from pokemon where pokemon.pokemon_id = pokemon) != NULL THEN
		raise exception 'Este pokemon já possui um treinador';
		return;
	end if;
	update mochila set mochila.quantidade = mochila.quantidade - 1 WHERE mochila.dono = treinador and mochila.nome_item = pokebola;
	SELECT into consegue round(CAST (random()*100 AS Integer),0);
	select taxa_captura into taxa_cap from pokedex where numero_pokedex = (select numero_pokedex from pokemon WHERE pokemon_id = pokemon);
	IF consegue <= taxa_cap then
		select captura_pokemon(pokemon, pokebola, treinador);
	end if;
	commit;
END;
$joga_pokebola$ LANGUAGE PLPGSQL;
