-- TSP POKEDEX

CREATE OR REPLACE FUNCTION CHECA_TIPO_POKEMON() RETURNS TRIGGER AS $checa_tipo_pokemon$
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


DROP TRIGGER IF EXISTS CHECADOR_TIPOS ON POKEDEX;


DROP TRIGGER IF EXISTS CHECADOR_TIPOS ON GINASIO;


DROP TRIGGER IF EXISTS CHECADOR_TIPOS ON BATALHADOR;


CREATE TRIGGER CHECADOR_TIPOS
BEFORE
INSERT
OR
UPDATE ON POKEDEX
FOR EACH ROW EXECUTE PROCEDURE CHECA_TIPO_POKEMON();


CREATE TRIGGER CHECADOR_TIPOS
BEFORE
INSERT
OR
UPDATE ON GINASIO
FOR EACH ROW EXECUTE PROCEDURE CHECA_TIPO_POKEMON();


CREATE TRIGGER CHECADOR_TIPOS
BEFORE
INSERT
OR
UPDATE ON BATALHADOR
FOR EACH ROW EXECUTE PROCEDURE CHECA_TIPO_POKEMON();

-- TSP BATALHA

CREATE OR REPLACE FUNCTION CHECK_NOVA_BATALHA() RETURNS TRIGGER AS $check_nova_batalha$
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


CREATE OR REPLACE FUNCTION descobre_pokemon() RETURNS TRIGGER AS $descobre_pokemon$
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

DROP TRIGGER IF EXISTS NOVA_BATALHA ON BATALHA;


CREATE TRIGGER NOVA_BATALHA
BEFORE
INSERT
OR
UPDATE ON BATALHA
FOR EACH ROW EXECUTE PROCEDURE CHECK_NOVA_BATALHA();

DROP TRIGGER IF EXISTS registra_pokemon ON BATALHA;

CREATE TRIGGER registra_pokemon
after
INSERT
OR
UPDATE ON BATALHA
FOR EACH ROW EXECUTE PROCEDURE descobre_pokemon();

-- TSP Lugar

CREATE OR REPLACE FUNCTION CRIA_COORDENADAS() RETURNS TRIGGER AS $cria_coordenadas$
DECLARE
	localizacao varchar(12);
BEGIN
	localizacao := new.x::text || ', ' || new.y::text;
	new.localizacao := localizacao;
	return new;
END;
$cria_coordenadas$ LANGUAGE PLPGSQL;


CREATE OR REPLACE FUNCTION CONFERE_COORDENADA() RETURNS TRIGGER AS $confere_coordenada$
DECLARE
	num integer;
BEGIN
	select count(*) into num from lugar where x=new.x and y=new.y;
	if num > 0 then
		raise exception 'Coordenada ja inserida';
		return null;
	end if;
	return new;
END;
$confere_coordenada$ LANGUAGE PLPGSQL;


DROP TRIGGER IF EXISTS GERA_COORDENADAS ON LUGAR;


CREATE TRIGGER GERA_COORDENADAS
BEFORE
INSERT
OR
UPDATE ON LUGAR
FOR EACH ROW EXECUTE PROCEDURE CRIA_COORDENADAS();


DROP TRIGGER IF EXISTS CONFERE_COORDENADA ON LUGAR;


CREATE TRIGGER CONFERE_COORDENADA
BEFORE
INSERT
OR
UPDATE ON LUGAR
FOR EACH ROW EXECUTE PROCEDURE CONFERE_COORDENADA();

-- SP ataca

CREATE OR REPLACE FUNCTION ATACA_BATALHA(POKEMON1 int, POKEMON2 int, ID_HABILIDADE int) RETURNS VOID AS $ataca_batalha$
declare
	vida_pokemon smallint;
	dano_habilidade smallint;
BEGIN
	select hp into vida_pokemon from pokemon where pokemon.pokemon_id = pokemon2;
	select dano into dano_habilidade from habilidade where habilidade.habilidade_id = id_habilidade;

	if dano_habilidade > vida_pokemon then
		update pokemon set hp = 0, status = 'Desmaiado' where pokemon.pokemon_id = pokemon2;
	else
		update pokemon set hp = vida_pokemon-dano_habilidade where pokemon.pokemon_id = pokemon2;
	end if;
END;
$ataca_batalha$ LANGUAGE PLPGSQL;

-- SP captura

CREATE OR REPLACE FUNCTION CAPTURA_POKEMON(POKEMON int, POKEBOLA VARCHAR(60),TREINADOR int) RETURNS VOID AS $captura_pokemon$
declare
	vida_pokemon smallint;
	dano_habilidade smallint;
BEGIN
	update pokemon set pokemon.treinador = treinador, pokemon.pokebola = pokebola WHERE pokemon.pokemon_id = pokemon;

END;
$captura_pokemon$ LANGUAGE PLPGSQL;
