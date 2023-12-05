-- TSP POKEDEX

CREATE OR REPLACE
FUNCTION CHECA_TIPO_POKEMON() RETURNS TRIGGER AS $checa_tipo_pokemon$
declare
	id_tipo Integer;
begin
	select Count(*) into id_tipo from Tipo where nome_tipo = NEW.tipo1 or nome_tipo = new.tipo2;
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
				ON POKENPC

			FOR EACH ROW EXECUTE PROCEDURE CHECA_TIPO_POKEMON();
-- TSP POKEMON

CREATE OR REPLACE
FUNCTION nomeia_pokemon() RETURNS TRIGGER AS $nomeia_pokemon$
declare
    current_name varchar(20);
begin
	if new.nome_pokemon_ins is null then
        select nome_pokemon into current_name from pokedex where pokedex.NUMERO_POKEDEX = new.NUMERO_POKEDEX;
        new.nome_pokemon_ins := current_name;
    end if;
    return new;
END;
$nomeia_pokemon$ LANGUAGE PLPGSQL
DROP TRIGGER IF EXISTS aplica_nome_poke
				ON pokemon;
CREATE TRIGGER aplica_nome_poke
BEFORE
INSERT
				OR
UPDATE
				ON pokemon
			FOR EACH ROW EXECUTE PROCEDURE nomeia_pokemon();

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
-- TSP Habilidade

CREATE OR REPLACE
FUNCTION nova_habilidade() RETURNS TRIGGER AS $nova_habilidade$
BEGIN
	new.tipo_dano:= upper(new.tipo_dano);
	if new.tipo_dano not in ('F', 'D') THEN
		raise exception 'Tipo de dano não é F para físico ou D para à distância';
		return null;
	end if;
	RETURN NEW;
END;
$nova_habilidade$ LANGUAGE PLPGSQL;

CREATE TRIGGER cria_habilidade before
INSERT
OR
UPDATE
ON Habilidade

			FOR EACH ROW EXECUTE PROCEDURE nova_habilidade();

-- TSP Tipo item

CREATE OR REPLACE
FUNCTION novo_tipo_item() RETURNS TRIGGER AS $novo_tipo_item$
BEGIN
	new.tipo_item:= upper(new.tipo_item);
	if new.tipo_item not in ('C','K','F','T','P') THEN
		raise exception 'Tipo de item rejeitado. São aceitos somente "C" para comum; "K" para chave; "P" para pokebolas; "F" para frutas e "T" para TMs.';
		return null;
	end if;
	RETURN NEW;
END;
$novo_tipo_item$ LANGUAGE PLPGSQL;

CREATE TRIGGER cria_tipo_item before
INSERT
OR
UPDATE
ON Tipo_item

			FOR EACH ROW EXECUTE PROCEDURE novo_tipo_item();

-- SP ataca

CREATE OR REPLACE
FUNCTION ATACA_BATALHA(POKEMON1 int, POKEMON2 int, ID_HABILIDADE int) RETURNS VOID AS $ataca_batalha$
declare
	vida_pokemon smallint;
	atq_pokemon smallint;
	spatq_pokemon smallint;
	def_pokemon smallint;
	spdef_pokemon smallint;
	dano_habilidade smallint;
	alvo char(1);
BEGIN
	select hp into vida_pokemon from pokemon where pokemon.pokemon_id = pokemon2;
	select defesa into def_pokemon from pokemon where pokemon.pokemon_id = pokemon2;
	select sp_defesa into spdef_pokemon from pokemon where pokemon.pokemon_id = pokemon2;
	select ataque into atq_pokemon from pokemon where pokemon.pokemon_id = pokemon1;
	select sp_ataque into spatq_pokemon from pokemon where pokemon.pokemon_id = pokemon1;
	select dano into dano_habilidade from habilidade where habilidade.habilidade_id = id_habilidade;
	select tipo_dano into alvo from habilidade where habilidade.habilidade_id = id_habilidade;
	if alvo = 'D' then
		dano_habilidade:= dano_habilidade + (spatq_pokemon * 0.1) - (spdef_pokemon * 0.1);
	else
		dano_habilidade:= dano_habilidade + (atq_pokemon * 0.1) - (def_pokemon * 0.1);
	end if;
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

CREATE OR REPLACE FUNCTION JOGA_POKEBOLA(POKEMON int, POKEBOLA VARCHAR(60), TREINADOR int) RETURNS VOID AS $joga_pokebola$
DECLARE
    consegue integer;
    taxa_cap smallint;
    forca_bola smallint;
BEGIN
    IF (SELECT treinador FROM pokemon WHERE pokemon.pokemon_id = POKEMON) IS NOT NULL THEN
        RAISE EXCEPTION 'Este pokemon já possui um treinador';
        RETURN;
    ELSIF (SELECT quantidade FROM mochila WHERE mochila.dono = TREINADOR AND mochila.nome_item = POKEBOLA) < 1 THEN
        RAISE EXCEPTION 'O treinador não possui pokebolas suficientes';
        RETURN;
    END IF;

    UPDATE mochila SET quantidade = quantidade - 1 WHERE mochila.dono = TREINADOR AND mochila.nome_item = POKEBOLA;
    SELECT forca INTO forca_bola FROM pokebolas WHERE pokebolas.nome_item = POKEBOLA;
    SELECT round(CAST (random()*100 AS Integer) - forca_bola, 0) INTO consegue;
    SELECT taxa_captura INTO taxa_cap FROM pokedex WHERE numero_pokedex = (SELECT numero_pokedex FROM pokemon WHERE pokemon_id = POKEMON);

    IF consegue <= taxa_cap THEN
        SELECT captura_pokemon(POKEMON, POKEBOLA, TREINADOR);
    END IF;
END;
$joga_pokebola$ LANGUAGE PLPGSQL;

REVOKE INSERT, UPDATE, DELETE ON TIPO_ITEM FROM PUBLIC;
REVOKE INSERT, UPDATE, DELETE ON ITEM_COMUM FROM PUBLIC;
REVOKE INSERT, UPDATE, DELETE ON ITEM_CHAVE FROM PUBLIC;
REVOKE INSERT, UPDATE, DELETE ON POKEBOLA FROM PUBLIC;
REVOKE INSERT, UPDATE, DELETE ON FRUTA FROM PUBLIC;
REVOKE INSERT, UPDATE, DELETE ON TM FROM PUBLIC;

-- SP Itens

CREATE OR REPLACE FUNCTION NOVO_ITEM_COMUM(ITEM_NOME VARCHAR(60),  EFEITO VARCHAR(150)) RETURNS VOID AS $novo_item_comum$
BEGIN
    IF (SELECT nome_item FROM tipo_item WHERE tipo_item.nome_item = item_nome) IS NOT NULL THEN
        RAISE EXCEPTION 'Item já registrado';
        RETURN;
    end if;
    INSERT into tipo_item (nome_item,tipo_item) VALUES (item_nome, 'C');
	INSERT into item_comum (nome_item,efeito) VALUES (item_nome, efeito);
END;
$novo_item_comum$ LANGUAGE PLPGSQL;
