import psycopg2
import os
from psycopg2 import sql
import random

primeira_vez_leste_pallet = True
mensagem_floresta = False
batalha_terminada = False
esta_em_batalha = False

cor_verde = '\033[92m'
cor_amarelo = '\033[93m'
cor_azul = '\033[36m'
cor_vermelho = '\033[91m'
reset_cor = '\033[0m'


def connect_database():
    try:
        conn = psycopg2.connect(
            database ="postgres",
            user ="postgres",
            password ="1234",
            host ="localhost",
            port ="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar-se ao banco de dados:", e)
        return None

def mostrar_treinador(conn, id_treinador):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM treinador WHERE treinador_id = %s", (id_treinador,))
    treinador = cursor.fetchone()

    if treinador:
        os.system('cls')
        print("Informações do Treinador:")
        print(f"Nome: {treinador[1]}")
        print(f"Sexo: {treinador[2]}")
        # Obter o nome da localidade por extenso
        cursor.execute("SELECT nome FROM localidade WHERE localizacao = %s", (treinador[3],))
        nome_localidade = cursor.fetchone()[0] if cursor.rowcount > 0 else "Desconhecida"
        print(f"Localização: {nome_localidade}")

        print(f"Quantidade de insígnias: {treinador[4]}")
        print(f"Pokemons capturados: {treinador[5]}")
        print(f"Dinheiro: {treinador[6]}")

        input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Treinador não encontrado!")

def verificar_local_atual(conn, id_treinador):
    cursor = conn.cursor()

    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    resultado = cursor.fetchone()

    if resultado:
        treinador_localizacao = resultado[0]

        cursor.execute("SELECT nome, info FROM localidade WHERE localizacao = %s", (treinador_localizacao,))
        local_atual = cursor.fetchall()

        if local_atual:
            os.system('cls')
            for local in local_atual:
                print(f"Local atual: {local[0]}\nDescrição do local: {local[1]}")
        else:
            os.system('cls')
            print("Erro: Localidade não encontrada para o treinador.")
    else:
        os.system('cls')
        print("Erro: Treinador não encontrado.")

def verificar_se_ha_npc_na_sala(conn, id_treinador):
    cursor = conn.cursor()

    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    resultado_treinador = cursor.fetchone()

    if resultado_treinador:
        treinador_localizacao = resultado_treinador[0]

        cursor.execute("SELECT npc_id, info FROM npc WHERE localidade = %s", (treinador_localizacao,))
        npcs_na_mesma_sala = cursor.fetchall()

        if npcs_na_mesma_sala:
            #os.system('cls')
            print("\nPersonagens no local atual:")
            for npc in npcs_na_mesma_sala:
                print(f"{npc[1]}")
        else:
            #os.system('cls')
            print("\nNão há NPCs neste local.")
            print("(Você pode interagir mesmo que não haja NPCs no local.)")
    else:
        os.system('cls')
        print("Erro: Treinador não encontrado.")
    
    #input("\nPressione Enter para continuar...")

def comprar_item(conn, id_treinador):
    cursor = conn.cursor()

    # Obter a localização do treinador
    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    treinador_localizacao = cursor.fetchone()

    if treinador_localizacao:
        treinador_localizacao = treinador_localizacao[0]

        # Verificar se o treinador está em um Pokemart
        cursor.execute("SELECT npc_id, info FROM npc WHERE localidade = %s AND info = 'Lojista'", (treinador_localizacao,))
        esta_no_pokemart = cursor.fetchall()

        if esta_no_pokemart:
            os.system('cls')
            print("Catálogo de itens disponíveis:\n\n")
            cursor.execute("SELECT item_nome, quantidade, preco FROM catalogo_pokemart")
            catalogo = cursor.fetchall()

            for item in catalogo:
                print(f"Item: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]}\n")

            # Solicitar ao treinador que escolha um item para comprar
            item_escolhido = input("\nDigite o nome do item que deseja comprar: ")

            # Verificar se o item escolhido está no catálogo
            item_no_catalogo = next((item for item in catalogo if item[0] == item_escolhido), None) 

            if item_no_catalogo:
                nome_item, quantidade_disponivel, preco_item = item_no_catalogo

                # Solicitar a quantidade desejada
                quantidade_desejada = int(input(f"Digite a quantidade desejada (até {quantidade_disponivel}): "))

                # Verificar se o treinador tem dinheiro suficiente
                cursor.execute("SELECT dinheiro FROM treinador WHERE treinador_id = %s", (id_treinador,))
                dinheiro_treinador = cursor.fetchone()[0]

                custo_total = preco_item * quantidade_desejada

                if dinheiro_treinador >= custo_total:
                    try:
                        # Tentar inserir o item na mochila
                        cursor.execute("INSERT INTO mochila (nome_item, dono, quantidade) VALUES (%s, %s, %s)",
                                       (nome_item, id_treinador, quantidade_desejada))
                    except psycopg2.IntegrityError as e:
                        # Se houver um erro de integridade, significa que o item já existe na mochila
                        conn.rollback()
                        cursor.execute("UPDATE mochila SET quantidade = quantidade + %s WHERE nome_item = %s AND dono = %s",
                                       (quantidade_desejada, nome_item, id_treinador))

                    # Atualizar a quantidade no catálogo
                    nova_quantidade = quantidade_disponivel - quantidade_desejada
                    cursor.execute("UPDATE catalogo_pokemart SET quantidade = %s WHERE item_nome = %s",
                                   (nova_quantidade, nome_item))

                    # Atualizar o dinheiro do treinador
                    novo_dinheiro = dinheiro_treinador - custo_total
                    cursor.execute("UPDATE treinador SET dinheiro = %s WHERE treinador_id = %s",
                                   (novo_dinheiro, id_treinador))

                    conn.commit()
                    os.system('cls')
                    print(f"Compra realizada com sucesso! Você comprou {quantidade_desejada} {nome_item}(s).")
                    input("\nPressione Enter para continuar...")
                else:
                    os.system('cls')
                    print("Dinheiro insuficiente para comprar o item.")
                    input("\nPressione Enter para continuar...")
            else:
                os.system('cls')
                print("Item não encontrado no catálogo.")
                input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("Não está no Pokemart.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Erro: Treinador não encontrado.")
        input("\nPressione Enter para continuar...")

    cursor.close()


def andar(conn, id_treinador):
    os.system('cls')
    cursor = conn.cursor()

    # Obtém a localização atual do treinador
    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    resultado_treinador = cursor.fetchone()

    if resultado_treinador:
        treinador_localizacao = resultado_treinador[0]

        # Verifica se é possível andar para a frente
        if treinador_localizacao < 13:
            # Atualiza a localização somando +1
            nova_localizacao = treinador_localizacao + 1
            cursor.execute("UPDATE treinador SET localizacao = %s WHERE treinador_id = %s", (nova_localizacao, id_treinador))

            # Commit para efetivar a atualização
            conn.commit()

            # Obtém o nome do treinador
            cursor.execute("SELECT nome_treinador FROM treinador WHERE treinador_id = %s", (id_treinador,))
            nome_treinador = cursor.fetchone()

            if nome_treinador:
                nome_treinador = nome_treinador[0]

                # Obtém o nome da nova localização
                cursor.execute("SELECT nome FROM localidade WHERE localizacao = %s", (nova_localizacao,))
                nome_cidade = cursor.fetchone()

                if nome_cidade:
                    nome_cidade = nome_cidade[0]
                    print(f"O treinador {nome_treinador} andou para {nome_cidade}.")
                else:
                    print(f"Nome da cidade não encontrado para a localização {nova_localizacao}.")
            else:
                print(f"Nome do treinador não encontrado para o ID {id_treinador}.")
        else:
            print("O treinador já está na localização final.")
    else:
        print(f"Treinador {id_treinador} não encontrado.")

    cursor.close()


def voltar(conn, id_treinador):
    os.system('cls')
    cursor = conn.cursor()

    # Obtém a localização atual do treinador
    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    resultado_treinador = cursor.fetchone()

    if resultado_treinador:
        treinador_localizacao = resultado_treinador[0]

        # Verifica se é possível voltar
        if treinador_localizacao > 1:
            # Atualiza a localização subtraindo 1
            nova_localizacao = treinador_localizacao - 1
            cursor.execute("UPDATE treinador SET localizacao = %s WHERE treinador_id = %s", (nova_localizacao, id_treinador))

            # Commit para efetivar a atualização
            conn.commit()

            # Obtém o nome do treinador
            cursor.execute("SELECT nome_treinador FROM treinador WHERE treinador_id = %s", (id_treinador,))
            nome_treinador = cursor.fetchone()

            if nome_treinador:
                nome_treinador = nome_treinador[0]

                # Obtém o nome da nova localização
                cursor.execute("SELECT nome FROM localidade WHERE localizacao = %s", (nova_localizacao,))
                nome_cidade = cursor.fetchone()

                if nome_cidade:
                    nome_cidade = nome_cidade[0]
                    print(f"O treinador {nome_treinador} voltou para a cidade {nome_cidade}.")
                else:
                    print(f"Nome da cidade não encontrado para a localização {nova_localizacao}.")
            else:
                print(f"Nome do treinador não encontrado para o ID {id_treinador}.")
        else:
            print("O treinador já está na localização inicial.")
    else:
        print(f"Treinador {id_treinador} não encontrado.")

    cursor.close()

def novo_treinador(conn, genero, nome_treinador):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TREINADOR (NOME_TREINADOR, SEXO, LOCALIZACAO, QUANT_INSIGNIAS, QUANT_PK_CAPTURADOS, DINHEIRO) VALUES (%s, %s, %s, %s, %s, %s)",
                   (nome_treinador, genero, 1, 0, 0, 1000))
    conn.commit()
    cursor.close()

def escolher_pokemon(conn, id_treinador):
    cursor = conn.cursor()

    # Obtém a localização atual do treinador
    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    resultado_treinador = cursor.fetchone()

    if resultado_treinador:
        treinador_localizacao = resultado_treinador[0]

        # Obtém o NPC na mesma localização
        cursor.execute("SELECT npc_id, info FROM npc WHERE localidade = %s", (treinador_localizacao,))
        npc = cursor.fetchone()

        if npc:
            npc_id, info = npc

            if info == 'Professor Oak':
                # Obtém os Pokémon Iniciais disponíveis
                cursor.execute("SELECT pokemon_id, numero_pokedex, nome_pokemon_ins FROM pokemon WHERE numero_pokedex IN (1, 4, 7)")
                pokemons = cursor.fetchall()

                if pokemons:
                    print("Professor: Bem-vindo! Venha escolher o seu primeiro Pokémon.\n")
                    print("Pokémons Iniciais disponíveis:\n")
                    for pokemon in pokemons:
                        nome_pokemon = pokemon[2]

                        if nome_pokemon == 'Bulbasaur':
                            nome_pokemon_colorido = f"{cor_verde}{nome_pokemon}{reset_cor}"
                        elif nome_pokemon == 'Charmander':
                            nome_pokemon_colorido = f"{cor_vermelho}{nome_pokemon}{reset_cor}"
                        elif nome_pokemon == 'Squirtle':
                            nome_pokemon_colorido = f"{cor_azul}{nome_pokemon}{reset_cor}"
                        else:
                            nome_pokemon_colorido = nome_pokemon

                        print(f"Nome: {nome_pokemon_colorido}")

                    # Solicita ao treinador que escolha um Pokémon Inicial
                    while True:
                        escolha_pokemon = input("\nDigite o nome do Pokémon Inicial que deseja (Bulbasaur, Charmander, Squirtle) ou 0 para sair: ")

                        if escolha_pokemon == '0':
                            os.system('cls')
                            print("Escolha de Pokémon Inicial cancelada.")
                            input("\nPressione Enter para continuar...")
                            break

                        # Verifica se o Pokémon escolhido está disponível
                        pokemon_disponivel = next((pokemon for pokemon in pokemons if pokemon[2].lower() == escolha_pokemon.lower()), None)

                        if pokemon_disponivel:
                            pokemon_id, numero_pokedex, nome_pokemon = pokemon_disponivel

                            # Verifica se o treinador já tem um Pokémon
                            cursor.execute("SELECT pokemon_id FROM pokemon WHERE treinador_id = %s", (id_treinador,))
                            pokemon_treinador = cursor.fetchone()

                            if pokemon_treinador:
                                os.system('cls')
                                print("O treinador já tem um Pokémon.")
                                input("\nPressione Enter para continuar...")
                            else:
                                # Adiciona o Pokémon ao treinador
                                cursor.execute("UPDATE pokemon SET treinador_id = %s WHERE pokemon_id = %s", (id_treinador, pokemon_id))

                                # Atualiza a quantidade de Pokémon capturados
                                cursor.execute("UPDATE treinador SET quant_pk_capturados = quant_pk_capturados + 1 WHERE treinador_id = %s",
                                               (id_treinador,))
                                
                                os.system('cls')
                                cursor.execute("INSERT into equipe (treinador_id, pokemon) VALUES (%s, %s)", (id_treinador, pokemon_id,))
                                print(f"{nome_pokemon} foi adicionado à sua equipe como seu Pokémon Inicial!")
                                input("\nPressione Enter para continuar...")
                                
                                # Diálogo após a escolha do Pokémon
                                os.system('cls')
                                print("Professor: Agora pegue isto, é uma Pokedex. Você irá utilizá-la para registrar todos os pokémons existentes no Mundo.")
                                print("\nVocê obteve Pokédex!")

                                # Registra o Pokémon na Pokédex
                                cursor.execute("INSERT INTO REGISTRO_POKEDEX (NUMERO_POKEMON, TREINADOR_ID, CAPTURADO) VALUES (%s, %s, 'Sim')",
                                               (numero_pokedex, id_treinador))

                                conn.commit()
                                print(f"\n{nome_pokemon} foi registrado na Pokédex!")
                                input("\nPressione Enter para continuar...")

                                break
                        else:
                            os.system('cls')
                            print("Escolha inválida. Tente novamente.")
                            input("\nPressione Enter para continuar...")

                else:
                    os.system('cls')
                    print("Não há Pokémons Iniciais disponíveis.")
                    input("\nPressione Enter para continuar...")
            else:
                os.system('cls')
                print("Você não está em um local adequado para escolher um Pokémon Inicial.")
                input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("Não há NPCs nesta localização.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Treinador não encontrado.")
        input("\nPressione Enter para continuar...")

    cursor.close()

def dialogo_quarto_treinador():
    os.system('cls')
    print("Quarto do treinador:\n")
    print("8:00 AM - Seu quarto.")
    print("(Pensamento): Que belo dia! Acho que vou descer as escadas e conversar com minha mãe!")
    input("\nPressione Enter para continuar...")

def dialogoMae():
    print("Mãe: Bom dia, Filho! Chegou o grande dia, vá até o laboratório do Professor Carvalho para ganhar o seu primeiro Pokémon. Ah, e não se esqueça de tomar seu café!\n")
    input("\nPressione Enter para continuar...")

def dialogo_leste_palet(conn, id_treinador):
    global primeira_vez_leste_pallet 
    cursor = conn.cursor()
    if primeira_vez_leste_pallet:
        print("\nGuia da cidade inicial: Olá, bem-vindo à cidade de Pallet, aqui é onde sua jornada começa.\nVocê pode ir seguir para o norte para chegar ao laboratório do Professor Carvalho ou voltar para o sul para ir para sua casa.\n\nTome aqui esse presente para te ajudar na sua jornada.\n\n")

        # Verificar se a entrada já existe
        cursor.execute("SELECT COUNT(*) FROM MOCHILA WHERE NOME_ITEM = 'Pokeball' AND DONO = %s", (id_treinador,))
        quantidade_existente = cursor.fetchone()[0]

        if quantidade_existente == 0:
            # Se não existir, realizar a inserção
            cursor.execute("INSERT INTO MOCHILA (NOME_ITEM, DONO, QUANTIDADE) VALUES ('Pokeball', %s, 5)", (id_treinador,))
        else:
            # Se existir, realizar a atualização
            cursor.execute("UPDATE MOCHILA SET QUANTIDADE = QUANTIDADE + 5 WHERE NOME_ITEM = 'Pokeball' AND DONO = %s", (id_treinador,))

        conn.commit()

        print("Você recebeu 5 Pokébolas!\n")
        input("\nPressione Enter para continuar...")
        primeira_vez_leste_pallet = False
    else:
        print("\nGuia da cidade inicial: Olá, bem-vindo à cidade de Pallet, aqui é onde sua jornada começa.\nVocê pode ir seguir para o norte para chegar ao laboratório do Professor Carvalho ou voltar para o sul para ir para sua casa.\n\n")
        print("Não vou te dar mais 5 pokébolas kkkkk\n")
        input("\nPressione Enter para continuar...")
    cursor.close()

def usar_pokecenter(conn, id_treinador):
    os.system('cls')
    cursor = conn.cursor()

    # Obtém a localização atual do treinador
    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    resultado_treinador = cursor.fetchone()

    cursor.execute("SELECT nome FROM localidade WHERE localizacao = %s", (resultado_treinador[0],))
    nome_localidade = cursor.fetchone()[0]

    print(f"Você está no {nome_localidade}.\n")

    if resultado_treinador:
        
        # Obtém os Pokémon feridos do treinador (com HP menor que 100)
        cursor.execute("SELECT pokemon_id, nome_pokemon_ins, hp FROM pokemon WHERE treinador_id = %s AND hp < 100", (id_treinador,))
        pokemons_feridos = cursor.fetchall()

        if pokemons_feridos:
            print("Pokémon(s) ferido(s) encontrados:")
            for pokemon in pokemons_feridos:
                print(f"- {pokemon[1]} (ID: {pokemon[0]}, HP: {pokemon[2]})")

            # Pergunta se deseja curar os Pokémon feridos
            resposta = input("\nDeseja curar os Pokémon feridos? (S/N) (50$ por pokemon curado): ").strip().lower()

            if resposta == 's':
                # Obtém a quantidade de Pokémon feridos do treinador (com HP menor que 100)
                cursor.execute("SELECT COUNT(*) FROM pokemon WHERE treinador_id = %s AND hp < 100", (id_treinador,))
                quantidade_pokemon_feridos = cursor.fetchone()[0]

                # Obtém o dinheiro do treinador
                cursor.execute("SELECT dinheiro FROM treinador WHERE treinador_id = %s", (id_treinador,))
                dinheiro_treinador = cursor.fetchone()[0]

                # Calcula o custo total
                custo_total = quantidade_pokemon_feridos * 50

                if dinheiro_treinador >= custo_total:
                    # Atualiza o HP de todos os Pokémon feridos do treinador
                    cursor.execute("UPDATE pokemon SET hp = 100 WHERE treinador_id = %s AND hp < 100", (id_treinador,))

                    # Atualiza o dinheiro do treinador
                    novo_dinheiro = dinheiro_treinador - custo_total
                    cursor.execute("UPDATE treinador SET dinheiro = %s WHERE treinador_id = %s", (novo_dinheiro, id_treinador))

                    conn.commit()
                    os.system('cls')
                    print("Os Pokémon feridos foram curados.")
                    print(f"Valor total pago: {custo_total}$.")
                    input("\nPressione Enter para continuar...")
                else:
                    os.system('cls')
                    print("Dinheiro insuficiente para curar os Pokémon feridos.")
                    input("\nPressione Enter para continuar...")
            else:
                os.system('cls')
                print("Os Pokémon feridos não foram curados.")
                input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("O treinador não possui Pokémon feridos.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Treinador não encontrado.")
        input("\nPressione Enter para continuar...")

    cursor.close()



def ver_mochila(conn, id_treinador):
    cursor = conn.cursor()

    # Seleciona todos os itens na mochila do treinador
    cursor.execute("SELECT nome_item, quantidade FROM mochila WHERE dono = %s", (id_treinador,))
    itens_mochila = cursor.fetchall()

    os.system('cls')
    print("Mochila do Treinador:")
    if itens_mochila:
        for item in itens_mochila:
            print(f"{item[0]}: {item[1]}")
        print("\nDeseja usar algum item? (S/N)")
        resposta = input().strip().lower()
        if resposta == 's':
            return usar_item(conn, id_treinador)
    else:
        print("A mochila está vazia.")

    input("\nPressione Enter para continuar...")

def usar_item(conn, id_treinador):
    cursor = conn.cursor()

    # Seleciona todos os itens na mochila do treinador
    cursor.execute("SELECT nome_item, quantidade FROM mochila WHERE dono = %s", (id_treinador,))
    itens_mochila = cursor.fetchall()

    os.system('cls')
    print("Mochila do Treinador:")
    if itens_mochila:
        for item in itens_mochila:
            print(f"{item[0]}: {item[1]}")
        print("\nDigite o nome do item que deseja usar ou 0 para sair: ")
        resposta = input().strip().lower()
        if resposta == '0':
            return
        else:
            # Verifica se o item escolhido está na mochila
            item_na_mochila = next((item for item in itens_mochila if item[0].lower() == resposta.lower()), None)

            if item_na_mochila:
                nome_item, quantidade_item = item_na_mochila

                if nome_item == 'Potion':
                    usar_potion(conn, id_treinador, quantidade_item)
                elif nome_item == 'Super Potion':
                    usar_super_potion(conn, id_treinador, quantidade_item)
                elif nome_item == 'Hyper Potion':
                    usar_hyper_potion(conn, id_treinador, quantidade_item)
                elif nome_item == 'Revive':
                    usar_revive(conn, id_treinador, quantidade_item)
                elif nome_item == 'Max Revive':
                    usar_max_revive(conn, id_treinador, quantidade_item)
                elif nome_item == 'Pokeball':
                    return usar_pokeball(conn, id_treinador, quantidade_item, nome_item)
                else:
                    os.system('cls')
                    print("Item não encontrado.")
                    input("\nPressione Enter para continuar...")  

def usar_pokeball(conn, id_treinador, quantidade_item, nome_item):
    global esta_em_batalha
    cursor = conn.cursor()
    if not esta_em_batalha:
        os.system('cls')
        print("Você não pode usar uma pokeball fora de uma batalha.")
        input("\nPressione Enter para continuar...")
    else:
        return nome_item
        


def usar_max_revive(conn, id_treinador, quantidade_item):
    cursor = conn.cursor()

    # Selecione apenas os pokemons que o Status é 'Desmaiado'
    cursor.execute("SELECT pokemon_id, nome_pokemon_ins, hp FROM pokemon WHERE treinador_id = %s AND status = 'Desmaiado'", (id_treinador,))
    pokemons_desmaiados = cursor.fetchall()

    if pokemons_desmaiados:
        print("\nPokémon(s) desmaiado(s) encontrados:")
        for pokemon in pokemons_desmaiados:
            print(f"- {pokemon[1]} (ID: {pokemon[0]}, HP: {pokemon[2]})")
        print("Digite o ID do Pokémon que deseja reviver: ")
        resposta = input().strip().lower()
        pokemon_escolhido = next((pokemon for pokemon in pokemons_desmaiados if str(pokemon[0]) == resposta), None)
        if pokemon_escolhido:
            pokemon_id, nome_pokemon, hp = pokemon_escolhido

            cura_hp = 100

            novo_hp = min(100, hp + cura_hp)

            cursor.execute("UPDATE pokemon SET hp = %s, status = 'Saudável' WHERE pokemon_id = %s", (novo_hp, pokemon_id))
            cursor.execute("UPDATE mochila SET quantidade = quantidade - 1 WHERE nome_item = 'Max Revive' AND dono = %s", (1, id_treinador,))

            conn.commit()
            os.system('cls')
            print(f"{nome_pokemon} foi revivido com {cura_hp} HP.")
            input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("Pokémon não encontrado.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Não há Pokémon desmaiados para usar o item.")
        input("\nPressione Enter para continuar...")

    cursor.close()

def usar_revive(conn, id_treinador, quantidade_item):
    cursor = conn.cursor()

    # Selecione apenas os pokemons que o Status é 'Desmaiado'
    cursor.execute("SELECT pokemon_id, nome_pokemon_ins, hp FROM pokemon WHERE treinador_id = %s AND status = 'Desmaiado'", (id_treinador,))
    pokemons_desmaiados = cursor.fetchall()

    if pokemons_desmaiados:
        print("\nPokémon(s) desmaiado(s) encontrados:")
        for pokemon in pokemons_desmaiados:
            print(f"- {pokemon[1]} (ID: {pokemon[0]}, HP: {pokemon[2]})")
        print("Digite o ID do Pokémon que deseja reviver: ")
        resposta = input().strip().lower()
        pokemon_escolhido = next((pokemon for pokemon in pokemons_desmaiados if str(pokemon[0]) == resposta), None)
        if pokemon_escolhido:
            pokemon_id, nome_pokemon, hp = pokemon_escolhido

            cura_hp = 20

            novo_hp = min(100, hp + cura_hp)

            cursor.execute("UPDATE pokemon SET hp = %s, status = 'Saudável' WHERE pokemon_id = %s", (novo_hp, pokemon_id))
            cursor.execute("UPDATE mochila SET quantidade = quantidade - %s WHERE nome_item = 'Revive' AND dono = %s", (1, id_treinador,))

            conn.commit()
            os.system('cls')
            print(f"{nome_pokemon} foi revivido com {cura_hp} HP.")
            input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("Pokémon não encontrado.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Não há Pokémon desmaiados para usar o item.")
        input("\nPressione Enter para continuar...")

    cursor.close()

def usar_potion(conn, id_treinador, quantidade_item):
    cursor = conn.cursor()

    # Selecione apenas os pokemons que o Status não é 'Desmaiado'
    cursor.execute("SELECT pokemon_id, nome_pokemon_ins, hp FROM pokemon WHERE treinador_id = %s AND (hp < 100 AND status != 'Desmaiado')", (id_treinador,))
    pokemons_feridos = cursor.fetchall()

    if pokemons_feridos:
        print("\nPokémon(s) ferido(s) e não desmaiado(s) encontrados:")
        for pokemon in pokemons_feridos:
            print(f"- {pokemon[1]} (ID: {pokemon[0]}, HP: {pokemon[2]})")
        print("Digite o ID do Pokémon que deseja curar: ")
        resposta = input().strip().lower()
        pokemon_escolhido = next((pokemon for pokemon in pokemons_feridos if str(pokemon[0]) == resposta), None)
        if pokemon_escolhido:
            pokemon_id, nome_pokemon, hp = pokemon_escolhido

            cura_hp = 20

            novo_hp = min(100, hp + cura_hp)

            cursor.execute("UPDATE pokemon SET hp = %s WHERE pokemon_id = %s", (novo_hp, pokemon_id))
            cursor.execute("UPDATE mochila SET quantidade = quantidade - %s WHERE nome_item = 'Potion' AND dono = %s", (1, id_treinador,))
            conn.commit()
            os.system('cls')
            print(f"{nome_pokemon} foi curado em {cura_hp} HP.")
            input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("Pokémon não encontrado.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Não há Pokémon feridos ou desmaiados para usar o item.")
        input("\nPressione Enter para continuar...")

    cursor.close()

def usar_super_potion(conn, id_treinador, quantidade_item):
    cursor = conn.cursor()

    # Selecione apenas os pokemons que o Status não é 'Desmaiado'
    cursor.execute("SELECT pokemon_id, nome_pokemon_ins, hp FROM pokemon WHERE treinador_id = %s AND (hp < 100 AND status != 'Desmaiado')", (id_treinador,))
    pokemons_feridos = cursor.fetchall()

    if pokemons_feridos:
        print("\nPokémon(s) ferido(s) e não desmaiado(s) encontrados:")
        for pokemon in pokemons_feridos:
            print(f"- {pokemon[1]} (ID: {pokemon[0]}, HP: {pokemon[2]})")
        print("Digite o ID do Pokémon que deseja curar: ")
        resposta = input().strip().lower()
        pokemon_escolhido = next((pokemon for pokemon in pokemons_feridos if str(pokemon[0]) == resposta), None)
        if pokemon_escolhido:
            pokemon_id, nome_pokemon, hp = pokemon_escolhido

            cura_hp = 50

            novo_hp = min(100, hp + cura_hp)

            cursor.execute("UPDATE pokemon SET hp = %s WHERE pokemon_id = %s", (novo_hp, pokemon_id))
            cursor.execute("UPDATE mochila SET quantidade = quantidade - %s WHERE nome_item = 'Super Potion' AND dono = %s", (1, id_treinador,))
            conn.commit()
            os.system('cls')
            print(f"{nome_pokemon} foi curado em {cura_hp} HP.")
            input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("Pokémon não encontrado.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Não há Pokémon feridos ou desmaiados para usar o item.")
        input("\nPressione Enter para continuar...")

    cursor.close()

def usar_hyper_potion(conn, id_treinador, quantidade_item):
    cursor = conn.cursor()

    # Selecione apenas os pokemons que o Status não é 'Desmaiado'
    cursor.execute("SELECT pokemon_id, nome_pokemon_ins, hp FROM pokemon WHERE treinador_id = %s AND (hp < 100 AND status != 'Desmaiado')", (id_treinador,))
    pokemons_feridos = cursor.fetchall()

    if pokemons_feridos:
        print("\nPokémon(s) ferido(s) e não desmaiado(s) encontrados:")
        for pokemon in pokemons_feridos:
            print(f"- {pokemon[1]} (ID: {pokemon[0]}, HP: {pokemon[2]})")
        print("Digite o ID do Pokémon que deseja curar: ")
        resposta = input().strip().lower()
        pokemon_escolhido = next((pokemon for pokemon in pokemons_feridos if str(pokemon[0]) == resposta), None)
        if pokemon_escolhido:
            pokemon_id, nome_pokemon, hp = pokemon_escolhido

            cura_hp = 100

            novo_hp = min(100, hp + cura_hp)

            cursor.execute("UPDATE pokemon SET hp = %s WHERE pokemon_id = %s", (novo_hp, pokemon_id))
            cursor.execute("UPDATE mochila SET quantidade = quantidade - %s WHERE nome_item = 'hyperpotion' AND dono = %s", (1, id_treinador,))
            conn.commit()
            os.system('cls')
            print(f"{nome_pokemon} foi curado em {cura_hp} HP.")
            input("\nPressione Enter para continuar...")
        else:
            os.system('cls')
            print("Pokémon não encontrado.")
            input("\nPressione Enter para continuar...")
    else:
        os.system('cls')
        print("Não há Pokémon feridos ou desmaiados para usar o item.")
        input("\nPressione Enter para continuar...")

    cursor.close()


def inserir_pokemon_base(conn):
    cursor = conn.cursor()

    dados_pokemon = [
        (1, None, 'Bulbasaur', 1, 4, None, None, 'Audacioso', 5, 100, 15, 10, 20, 18, 20, 'M', 0, 'Saudável', 'Pokeball', 20, 10, 4),
        (2, None, 'Ivysaur', 1, 4, None, None, 'Audacioso', 5, 100, 25, 12, 40, 18, 25, 'M', 0, 'Saudável', 'Pokeball', 40, 20, 4),
        (3, None, 'Venusaur', 1, 4, None, None, 'Audacioso', 5, 100, 45, 14, 60, 18, 35, 'M', 0, 'Saudável', 'Pokeball', 100, 200, 4),
        (4, None, 'Charmander', 1, 2, None, None, 'Docil', 5, 100, 15, 20, 15, 18, 30, 'M', 0, 'Saudável', 'Pokeball', 30, 30, 4),
        (5, None, 'Charmeleon', 1, 2, None, None, 'Docil', 5, 100, 25, 35, 18, 18, 37, 'M', 0, 'Saudável', 'Pokeball', 60, 50, 4),
        (6, None, 'Charizard', 1, 2, None, None, 'Docil', 5, 100, 45, 50, 22, 18, 45, 'M', 0, 'Saudável', 'Pokeball', 180, 150, 4),
        (7, None, 'Squirtle', 1, 3, None, None, 'Bravo', 5, 100, 15, 12, 20, 18, 28, 'M', 0, 'Saudável', 'Pokeball', 30, 30, 4),
        (8, None, 'Wartortle', 1, 3, None, None, 'Bravo', 5, 100, 25, 22, 40, 18, 34, 'M', 0, 'Saudável', 'Pokeball', 60, 50, 4),
        (9, None, 'Blastoise', 1, 3, None, None, 'Bravo', 5, 100, 45, 47, 60, 18, 45, 'M', 0, 'Saudável', 'Pokeball', 150, 200, 4),
        (10, None, 'Caterpie', 1, 18, None, None, 'Alegre', 5, 100, 5, 5, 10, 18, 10, 'M', 0, 'Saudável', None, 5, 2, 4),
        (11, None, 'Metapod', 1, 18, None, None, 'Curioso', 5, 100, 10, 5, 15, 18, 10, 'M', 0, 'Saudável', None, 7, 3, 4),
        (12, None, 'Butterfree', 1, 18, None, None, 'Educado', 5, 100, 7, 4, 30, 18, 35, 'F', 0, 'Saudável', None, 15, 3, 4),
        (13, None, 'Weedle', 1, 18, None, None, 'Observador', 5, 100, 9, 4, 15, 18, 15, 'M', 0, 'Saudável', None, 5, 3, 4),
        (14, None, 'Kakuna', 1, 18, None, None, 'Relaxado', 5, 100, 20, 4, 18, 18, 17, 'M', 0, 'Saudável', None, 7, 3, 4),
        (15, None, 'Beedrill', 1, 18, None, None, 'Valente', 5, 100, 35, 20, 18, 18, 35, 'F', 0, 'Saudável', None, 20, 3, 4),
        (16, None, 'Pidgey', 1, 8, None, None, 'Atrevido', 5, 100, 10, 20, 12, 18, 20, 'M', 0, 'Saudável', None, 20, 5, 4),
        (17, None, 'Pidgeotto', 1, 8, None, None, 'Exaltado', 5, 100, 20, 30, 25, 18, 30, 'M', 0, 'Saudável', None, 35, 10, 4),
        (18, None, 'Pidgeot', 1, 8, None, None, 'Empenhado', 5, 100, 40, 40, 35, 18, 37, 'M', 0, 'Saudável', None, 45, 25, 4),
        (19, None, 'Rattata', 1, 19, None, None, 'Divertido', 5, 100, 10, 10, 5, 18, 22, 'M', 0, 'Saudável', None, 7, 5, 4),
        (20, None, 'Raticate', 1, 19, None, None, 'Nervoso', 5, 100, 27, 15, 7, 18, 27, 'M', 0, 'Saudável', None, 16, 10, 4),
        #(74, 2, 'Geodude', 6, 11, None, None, 'Nervoso', 5, 100, 30, 30, 5, 18, 12, 'M', 0, 'Saudável', 'Pokeball', 40, 60, 4),
        (95, 2, 'Onix', 6, 11, None, None, 'Nervoso', 5, 100, 50, 40, 15, 18, 10, 'M', 0, 'Saudável', 'Pokeball', 400, 1000, 4),
        #(118, 3, 'Goldeen', 3, 20, None, None, 'Tranquilo', 5, 100, 16, 10, 25, 18, 26, 'F', 0, 'Saudável', 'Pokeball', 30, 15, 4),
        (120, 3, 'Staryu', 3, 20, None, None, 'Relaxado', 5, 100, 12, 10, 18, 18, 20, 'F', 0, 'Saudável', 'Pokeball', 15, 2, 4),
    ]

    for pokemon in dados_pokemon:
        cursor.execute("""
            INSERT INTO POKEMON (
                NUMERO_POKEDEX, TREINADOR_ID, NOME_POKEMON_INS, HABILIDADE1, HABILIDADE2, HABILIDADE3, HABILIDADE4, NATURE, NIVEL, HP, DEFESA, ATAQUE, SP_ATAQUE, SP_DEFESA, VELOCIDADE,
                SEXO, XP, STATUS, POKEBOLA, ALTURA, PESO, LOCALIZACAO
            ) VALUES %s;
        """, (pokemon,))

    conn.commit()
    cursor.close()

def ver_pokedex(conn, id_treinador):
    cursor = conn.cursor()

    # Obtém o número de Pokémon capturados pelo treinador
    cursor.execute("SELECT quant_pk_capturados FROM treinador WHERE treinador_id = %s", (id_treinador,))
    quantidade_capturados = cursor.fetchone()[0]

    if quantidade_capturados > 0:
        # Obtém os Pokémon registrados na Pokédex com informações detalhadas, ordenados pelo número da Pokédex
        cursor.execute("""
            SELECT rp.numero_pokemon, p.nome_pokemon, p.tipo1, p.tipo2, p.nivel_evolucao,
                   p.taxa_captura, p.som_emitido, p.regiao, p.info, rp.capturado
            FROM registro_pokedex rp
            JOIN pokedex p ON rp.numero_pokemon = p.numero_pokedex
            WHERE rp.treinador_id = %s
            ORDER BY rp.numero_pokemon
        """, (id_treinador,))
        
        pokemons_registrados = cursor.fetchall()

        if pokemons_registrados:
            os.system('cls')
            print("Pokédex do Treinador:")
            for pokemon in pokemons_registrados:
                cor_nome = cor_verde if pokemon[9] == 'Sim' else cor_vermelho

                print(f"#{pokemon[0]} - {cor_nome}{pokemon[1]}{reset_cor}")
                print(f"Tipo(s): {pokemon[2]}{' / ' + pokemon[3] if pokemon[3] else ''}")
                print(f"Nível de Evolução: {pokemon[4]}" if pokemon[4] else "")
                print(f"Taxa de Captura: {pokemon[5]}")
                #print(f"Som Emitido: {pokemon[6]}")
                print(f"Região: {pokemon[7]}")
                print(f"Capturado: {pokemon[9]}")
                print(f"Informações: {pokemon[8]}")
                print("-"*40)  # Adicione uma linha separadora entre os Pokémon

        else:
            os.system('cls')
            print("A Pokédex está vazia.")
    else:
        os.system('cls')
        print("O treinador não possui a Pokédex e nenhum Pokémon capturado.")

    input("\nPressione Enter para continuar...")
    os.system('cls')

    cursor.close()


def ver_pokemon(conn, id_treinador):
    cursor = conn.cursor()

    # Obtém os Pokémon do treinador com informações de habilidades
    cursor.execute("""
        SELECT
            POKEMON.POKEMON_ID,
            POKEMON.NOME_POKEMON_INS,
            POKEMON.NIVEL,
            POKEMON.HP,
            POKEMON.SEXO,
            POKEMON.STATUS,
            HABILIDADE1.NOME_HABILIDADE AS HABILIDADE1,
            HABILIDADE2.NOME_HABILIDADE AS HABILIDADE2,
            HABILIDADE3.NOME_HABILIDADE AS HABILIDADE3,
            HABILIDADE4.NOME_HABILIDADE AS HABILIDADE4,
            POKEMON.XP
        FROM
            POKEMON
            LEFT JOIN HABILIDADE AS HABILIDADE1 ON POKEMON.HABILIDADE1 = HABILIDADE1.HABILIDADE_ID
            LEFT JOIN HABILIDADE AS HABILIDADE2 ON POKEMON.HABILIDADE2 = HABILIDADE2.HABILIDADE_ID
            LEFT JOIN HABILIDADE AS HABILIDADE3 ON POKEMON.HABILIDADE3 = HABILIDADE3.HABILIDADE_ID
            LEFT JOIN HABILIDADE AS HABILIDADE4 ON POKEMON.HABILIDADE4 = HABILIDADE4.HABILIDADE_ID
        WHERE
            POKEMON.TREINADOR_ID = %s
    """, (id_treinador,))

    pokemons_treinador = cursor.fetchall()

    if pokemons_treinador:
        os.system('cls')
        print("Pokémons do Treinador:\n")
        for pokemon in pokemons_treinador:
            print(f"Nome: {pokemon[1]}\n")
            print(f"HP: {pokemon[3]}, Status: {pokemon[5]}, Sexo: {pokemon[4]}")
            print(f"Nível: {pokemon[2]}, XP: {pokemon[10]}\n")
            print(f"Habilidade 1: {pokemon[6] if pokemon[6] else 'Não aprendeu ainda'}")
            print(f"Habilidade 2: {pokemon[7] if pokemon[7] else 'Não aprendeu ainda'}")
            print(f"Habilidade 3: {pokemon[8] if pokemon[8] else 'Não aprendeu ainda'}")
            print(f"Habilidade 4: {pokemon[9] if pokemon[9] else 'Não aprendeu ainda'}")
            print("-" * 30)
    else:
        os.system('cls')
        print("O treinador não possui nenhum Pokémon.")

    input("\nPressione Enter para continuar...")

    cursor.close()


def floresta_viridian(conn, id_treinador):
    global mensagem_floresta
    os.system('cls')
    if not mensagem_floresta:
        print("Você está na Floresta de Viridian.\n")
        print("Aqui você tem chance de encontrar Pokémons selvagens.\n")
        input("\n\nPressione Enter para continuar...")
        mensagem_floresta = True
    cursor = conn.cursor()

    # Verificar se há um Pokémon selvagem na floresta
    chance_encontro = random.random()  # Gera um número aleatório entre 0 e 1
    if chance_encontro < 0.8:  # Exemplo: 80% de chance de encontrar um Pokémon selvagem
        # Selecionar um Pokémon selvagem aleatório
        cursor.execute("SELECT pokemon_id, nome_pokemon_ins, nivel, hp, status, nature, numero_pokedex FROM pokemon WHERE treinador_id IS NULL AND pokebola IS NULL ORDER BY RANDOM() LIMIT 1")
        pokemon_selvagem = cursor.fetchone()


        os.system('cls')
        print("Um Pokémon selvagem apareceu!!!\n")

        if pokemon_selvagem:
            pokemon_id, nome_pokemon, nivel, hp, status, nature, numero_pokedex = pokemon_selvagem

            # Verifica se o Pokémon já está registrado na Pokédex
            cursor.execute("SELECT * FROM registro_pokedex WHERE numero_pokemon = %s AND treinador_id = %s", (numero_pokedex, id_treinador,))
            registro_existente = cursor.fetchone()
            
            # Define a cor do nome do Pokémon com base na existência do registro
            cor_nome = cor_verde if registro_existente else cor_vermelho

            print(f"{nome_pokemon} (Nível {nivel})")
            print(f"HP: {hp} | Status: {status} | Natureza: {nature}")
            print("\nEscolha uma opção:")
            print("1. Batalhar (irá registrá-lo na Pokédex)")
            print("2. Fugir")

            if registro_existente:
                print(f"\n{cor_nome}{nome_pokemon}{reset_cor} já está registrado na sua Pokédex.\n")
            else:
                print(f"\n{cor_vermelho}{nome_pokemon}{reset_cor} ainda não está registrado na sua Pokédex.\n")

            escolha = input().strip()
            if escolha == '1':
                os.system('cls')
                # Verificar se o Pokémon já foi registrado pelo treinador
                cursor.execute("SELECT * FROM registro_pokedex WHERE numero_pokemon = %s AND treinador_id = %s", (numero_pokedex, id_treinador,))
                registro_existente = cursor.fetchone()

                if registro_existente:
                    print(f"{nome_pokemon} já está registrado na sua Pokédex.\n")
                print("Você irá batalhar")
                input("\nPressione Enter para continuar...")
                batalha_pokemon_selvagem(conn, id_treinador, pokemon_selvagem, registro_existente)
            elif escolha == '2':
                print("Você fugiu da batalha.")
                input("\nPressione Enter para continuar...")
            else:
                print("Opção inválida.")
    else:
        os.system('cls')
        print("Você explorou mas não encontrou nenhum Pokémon selvagem. Interaja novamente para continuar procurando!\n")
        input("\nPressione Enter para continuar...")
    cursor.close()

def batalha_pokemon_selvagem(conn, id_treinador, pokemon_selvagem, registro_existente):
    os.system('cls')
    global batalha_terminada
    global esta_em_batalha
    esta_em_batalha = True
    batalha_terminada = False
    atacou_primeiro = None
    cursor = conn.cursor()

    pokemon_id_selvagem, nome_pokemon_selvagem, nivel_selvagem, hp_selvagem, status_selvagem, nature_selvagem, numero_pokedex_selvagem = pokemon_selvagem

    # Obter informações do Pokémon do treinador
    cursor.execute("SELECT * FROM pokemon WHERE treinador_id = %s", (id_treinador,))
    pokemon_treinador = cursor.fetchone()

    if pokemon_treinador:
        pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

        os.system('cls')
        print("Você está em uma batalha!\n")

    while not batalha_terminada:

        os.system('cls')
        
        # Atualize a variável hp com o valor mais recente do banco de dados
        cursor.execute("SELECT hp, status FROM pokemon WHERE treinador_id = %s", (id_treinador,))
        resultado_treinador = cursor.fetchone()
        hp_treinador, status_treinador = resultado_treinador[0], resultado_treinador[1]
        print(f"Seu Pokémon: {nome_pokemon_treinador} (Nível {nivel_treinador})")
        print(f"HP: {hp_treinador} | Status: {status_treinador} | Natureza: {nature_treinador}\n")

        # Atualize a variável hp_selvagem com o valor mais recente do banco de dados
        cursor.execute("SELECT hp, status FROM pokemon WHERE pokemon_id = %s", (pokemon_id_selvagem,))
        resultado_selvagem = cursor.fetchone()
        hp_selvagem, status_selvagem = resultado_selvagem[0], resultado_selvagem[1]
        print(f"{nome_pokemon_selvagem} (Nível {nivel_selvagem})")
        print(f"HP: {hp_selvagem} | Status: {status_selvagem} | Natureza: {nature_selvagem}\n")

        print("Escolha uma opção:")
        print("1. Atacar")
        print("2. Usar Item")
        print("3. Tentar Capturar")
        print("4. Fugir")

        escolha = input().strip()

        if escolha == '1':
            atacou_primeiro = check_ataca_primeiro(conn, id_treinador, pokemon_treinador, pokemon_selvagem)
            if atacou_primeiro:
                display_habilidades(conn, id_treinador, pokemon_treinador, pokemon_selvagem)
            else:
                habilidades_pokemon_selvagem(conn, id_treinador, pokemon_selvagem, pokemon_treinador)
            os.system('cls')
            # Atualize a variável hp com o valor mais recente do banco de dados
            cursor.execute("SELECT hp, status FROM pokemon WHERE treinador_id = %s", (id_treinador,))
            resultado_treinador = cursor.fetchone()
            hp_treinador, status_treinador = resultado_treinador[0], resultado_treinador[1]
            # Atualize a variável hp_selvagem com o valor mais recente do banco de dados
            cursor.execute("SELECT hp, status FROM pokemon WHERE pokemon_id = %s", (pokemon_id_selvagem,))
            resultado_selvagem = cursor.fetchone()
            hp_selvagem, status_selvagem = resultado_selvagem[0], resultado_selvagem[1]

            # Checa se o pokemon selvagem desmaiou e termina a batalha
            if hp_selvagem <= 0:
                print(f"Seu Pokémon: {nome_pokemon_treinador} (Nível {nivel_treinador})")
                print(f"HP: {hp_treinador} | Status: {status_treinador} | Natureza: {nature_treinador}\n")

                print(f"{nome_pokemon_selvagem} (Nível {nivel_selvagem})")
                print(f"HP: {hp_selvagem} | Status: {status_selvagem} | Natureza: {nature_selvagem}\n")

                print(f"{nome_pokemon_selvagem} selvagem desmaiou!\n")
                input("\nPressione Enter para continuar...")

                os.system('cls')
                print(f"\nVocê derrotou o Pokémon selvagem!\n")
                print(f"Você ganhou 10 de XP!\n")
                input("\nPressione Enter para continuar...")
                batalha_terminada = True
                break

            # Checa se o pokemon selvagem desmaiou e termina a batalha
            if hp_treinador <= 0:
                print(f"Seu Pokémon: {nome_pokemon_treinador} (Nível {nivel_treinador})")
                print(f"HP: {hp_treinador} | Status: {status_treinador} | Natureza: {nature_treinador}\n")

                print(f"{nome_pokemon_selvagem} (Nível {nivel_selvagem})")
                print(f"HP: {hp_selvagem} | Status: {status_selvagem} | Natureza: {nature_selvagem}\n")

                print(f"{nome_pokemon_treinador} desmaiou!\n")
                input("\nPressione Enter para continuar...")

                os.system('cls')
                print(f"\nVocê foi derrotado. A batalha acabou\n")
                input("\nPressione Enter para continuar...")
                batalha_terminada = True
                break

            os.system('cls')
            if not atacou_primeiro:
                display_habilidades(conn, id_treinador, pokemon_treinador, pokemon_selvagem)
            else:
                os.system('cls')
                habilidades_pokemon_selvagem(conn, id_treinador, pokemon_selvagem, pokemon_treinador)

        elif escolha == '2':
            ver_mochila(conn, id_treinador)
        elif escolha == '3':
            nome_pokebola_utilizada = ver_mochila(conn, id_treinador)
            capturar_pokemon(conn, pokemon_id_selvagem, nome_pokebola_utilizada, id_treinador, registro_existente, pokemon_selvagem)
            input("\nPressione Enter para continuar...")
            if not batalha_terminada:
                habilidades_pokemon_selvagem(conn, id_treinador, pokemon_selvagem, pokemon_treinador)
        elif escolha == '4':
            fugir_batalha(conn, id_treinador, registro_existente, pokemon_selvagem)
        else:
            print("Opção inválida. Tente novamente.")

        #atacou_primeiro = None
    esta_em_batalha = False
    cursor.close()


def capturar_pokemon(conn, pokemon_id, pokebola, id_treinador, registro_existente, pokemon_selvagem):
    global batalha_terminada

    try:
        cursor = conn.cursor()

        # Chamar a função JOGA_POKEBOLA no banco de dados
        cursor.execute("SELECT JOGA_POKEBOLA(%s, %s, %s);", (pokemon_id, pokebola, id_treinador,))
        os.system('cls')
        print(f"O treinador jogou uma {pokebola}!!!\n")
        input("\nPressione Enter para continuar...")
        os.system('cls')
        print("Capturando...\n")
        input("\nPressione Enter para continuar...")
        os.system('cls')
        for notice in conn.notices:
                if 'A captura falhou!' in notice:
                    print('A captura falhou.\n')
                elif 'Pokemon capturado!' in notice:       
                    print('Pokemon capturado!\n')
                    cursor.execute("INSERT INTO equipe (treinador_id, pokemon) VALUES (%s, %s)", (id_treinador, pokemon_id,))
                    if not registro_existente:
                        # Insira o Pokémon na tabela registro_pokedex
                        cursor.execute("INSERT INTO registro_pokedex (numero_pokemon, treinador_id, capturado) VALUES (%s, %s, %s)", (pokemon_selvagem[6], id_treinador, 'Sim'))
                        conn.commit()
                        print(f"\n{cor_verde}{pokemon_selvagem[1]}{reset_cor} foi registrado na Pokédex!\n")
                    batalha_terminada = True
        conn.notices.clear()

        # Commit das alterações
        conn.commit()

    except psycopg2.Error as e:
        # Exibir mensagem de erro em caso de falha
        conn.rollback()
        message = str(e).split('CONTEXT')[0]
        print(f"{message}")

    finally:
        # Fechar o cursor
        cursor.close()

def fugir_batalha(conn, id_treinador, registro_existente, pokemon_selvagem):
    global batalha_terminada
    cursor = conn.cursor()

    sucesso_fuga = random.choice([True, False])
    os.system('cls')
    if sucesso_fuga:
        print("Você conseguiu fugir da batalha!")
        if not registro_existente:
            # Insira o Pokémon na tabela registro_pokedex
            cursor.execute("INSERT INTO registro_pokedex (numero_pokemon, treinador_id, capturado) VALUES (%s, %s, %s)", (pokemon_selvagem[6], id_treinador, 'Não'))
            conn.commit()
            print(f"\n{cor_verde}{pokemon_selvagem[1]}{reset_cor} foi registrado na Pokédex!\n")
        input("\nPressione Enter para continuar...")
        batalha_terminada = True
    else:
        print("Você não conseguiu fugir!")
        input("\nPressione Enter para continuar...")

    cursor.close()

def check_ataca_primeiro(conn, id_treinador, pokemon_treinador, pokemon_selvagem):
    cursor = conn.cursor()

    # Obter informações de velocidade dos Pokémon
    cursor.execute("SELECT velocidade FROM pokemon WHERE treinador_id = %s AND pokemon_id = %s", (id_treinador, pokemon_treinador[0]))
    velocidade_treinador = cursor.fetchone()[0]

    cursor.execute("SELECT velocidade FROM pokemon WHERE pokemon_id = %s", (pokemon_selvagem[0],))
    velocidade_selvagem = cursor.fetchone()[0]

    # Compara as velocidades para determinar quem ataca primeiro
    if velocidade_treinador > velocidade_selvagem:
        print(f"Seu Pokémon ataca primeiro!")
        input("\nPressione Enter para continuar...")
        return True
    elif velocidade_treinador < velocidade_selvagem:
        print(f"O Pokémon selvagem ataca primeiro!")
        input("\nPressione Enter para continuar...")
        return False
    else:
        print(f"Ambos os Pokémon têm a mesma velocidade. A ordem de ataque é aleatória.")
        input("\nPressione Enter para continuar...")
        return random.choice([True, False])

    cursor.close()

def habilidades_pokemon_selvagem(conn, id_treinador, pokemon_selvagem, pokemon_treinador):
    cursor = conn.cursor()

    pokemon_id_selvagem, nome_pokemon_selvagem, nivel_selvagem, hp_selvagem, status_selvagem, nature_selvagem, numero_pokedex_selvagem = pokemon_selvagem
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    # Obtém as habilidades do Pokémon selvagem
    query = """
    SELECT p.*, h1.NOME_HABILIDADE as habilidade1_nome, h2.NOME_HABILIDADE as habilidade2_nome,
           h3.NOME_HABILIDADE as habilidade3_nome, h4.NOME_HABILIDADE as habilidade4_nome
    FROM pokemon p
    LEFT JOIN habilidade h1 ON p.HABILIDADE1 = h1.HABILIDADE_ID
    LEFT JOIN habilidade h2 ON p.HABILIDADE2 = h2.HABILIDADE_ID
    LEFT JOIN habilidade h3 ON p.HABILIDADE3 = h3.HABILIDADE_ID
    LEFT JOIN habilidade h4 ON p.HABILIDADE4 = h4.HABILIDADE_ID
    WHERE p.pokemon_id = %s
    """
    cursor.execute(query, (pokemon_id_selvagem,))
    pokemon_info = cursor.fetchone()

    if pokemon_info:
        (
            pokemon_id, numero_pokedex, treinador_id, nome_pokemon,
            habilidade1_id, habilidade2_id, habilidade3_id, habilidade4_id,
            nature, nivel, hp, defesa, ataque, sp_ataque, sp_defesa,
            velocidade, sexo, xp, status, pokebola, altura, peso, localizacao,
            habilidade1_nome, habilidade2_nome, habilidade3_nome, habilidade4_nome
        ) = pokemon_info

        os.system('cls')
        print("O pokemon selvagem atacou!\n")
        print(f"Pokémon: {nome_pokemon} (Nível {nivel})")
        print(f"HP: {hp} | Status: {status} | Natureza: {nature}\n\n")

        escolha = str(random.randint(1, 2)).strip()

        habilidades = {
            '1': habilidade1_nome,
            '2': habilidade2_nome,
            #'3': habilidade3_nome if habilidade3_nome else "Ainda não aprendeu",
            #'4': habilidade4_nome if habilidade4_nome else "Ainda não aprendeu"
        }

        habilidade_id = {
            '1': habilidade1_id,
            '2': habilidade2_id,
            #'3': habilidade3_id if habilidade3_id else None,
            #'4': habilidade4_id if habilidade4_id else None
        }

        if escolha in habilidades:
            # Atacar com a habilidade escolhida
            print(f"{nome_pokemon} usou {habilidades[escolha]}\n")
            if habilidade_id[escolha]:
                calcular_dano_selvagem(conn, pokemon_selvagem, pokemon_treinador, habilidade_id[escolha])
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Erro.")
    input("\nPressione Enter para continuar...")
    cursor.close()



def display_habilidades(conn, id_treinador, pokemon_treinador, pokemon_selvagem):
    cursor = conn.cursor()

    pokemon_id_selvagem, nome_pokemon_selvagem, nivel_selvagem, hp_selvagem, status_selvagem, nature_selvagem, numero_pokedex_selvagem = pokemon_selvagem
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    # Obtém as habilidades do Pokémon do treinador
    query = """
    SELECT p.*, h1.NOME_HABILIDADE as habilidade1_nome, h2.NOME_HABILIDADE as habilidade2_nome,
           h3.NOME_HABILIDADE as habilidade3_nome, h4.NOME_HABILIDADE as habilidade4_nome
    FROM pokemon p
    LEFT JOIN habilidade h1 ON p.HABILIDADE1 = h1.HABILIDADE_ID
    LEFT JOIN habilidade h2 ON p.HABILIDADE2 = h2.HABILIDADE_ID
    LEFT JOIN habilidade h3 ON p.HABILIDADE3 = h3.HABILIDADE_ID
    LEFT JOIN habilidade h4 ON p.HABILIDADE4 = h4.HABILIDADE_ID
    WHERE p.treinador_id = %s
    """
    cursor.execute(query, (id_treinador,))
    pokemon_info = cursor.fetchone()

    if pokemon_info:
        (
            pokemon_id, numero_pokedex, treinador_id, nome_pokemon,
            habilidade1_id, habilidade2_id, habilidade3_id, habilidade4_id,
            nature, nivel, hp, defesa, ataque, sp_ataque, sp_defesa,
            velocidade, sexo, xp, status, pokebola, altura, peso, localizacao,
            habilidade1_nome, habilidade2_nome, habilidade3_nome, habilidade4_nome
        ) = pokemon_info

        os.system('cls')
        print("Você ataca!\n")
        print(f"Seu Pokémon: {nome_pokemon} (Nível {nivel})")
        print(f"HP: {hp} | Status: {status} | Natureza: {nature}\n")
        print(f"1. {habilidade1_nome}")
        print(f"2. {habilidade2_nome}")
        print(f"3. {habilidade3_nome}" if habilidade3_nome else "3. (Ainda não aprendeu)")
        print(f"4. {habilidade4_nome}" if habilidade4_nome else "4. (Ainda não aprendeu)")

        escolha = input().strip()

        habilidades = {
            '1': habilidade1_nome,
            '2': habilidade2_nome,
            '3': habilidade3_nome if habilidade3_nome else "Ainda não aprendeu",
            '4': habilidade4_nome if habilidade4_nome else "Ainda não aprendeu"
        }

        habilidade_id = {
            '1': habilidade1_id,
            '2': habilidade2_id,
            '3': habilidade3_id if habilidade3_id else None,
            '4': habilidade4_id if habilidade4_id else None
        }

        if escolha in habilidades:
            # Atacar com a habilidade escolhida
            print(f"\n{nome_pokemon} usou {habilidades[escolha]}")
            if habilidade_id[escolha]:
                calcular_dano(conn, pokemon_treinador, pokemon_selvagem, habilidade_id[escolha])
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Treinador não possui Pokémon.")
    input("\nPressione Enter para continuar...")
    cursor.close()

def calcular_dano(conn, pokemon_treinador, pokemon_selvagem, habilidade_id):
    cursor = conn.cursor()

    pokemon_id_selvagem, nome_pokemon_selvagem, nivel_selvagem, hp_selvagem, status_selvagem, nature_selvagem, numero_pokedex_selvagem = pokemon_selvagem
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    try:
        # Chamar a stored procedure ATACA_BATALHA
        cursor.execute("SELECT ATACA_BATALHA(%s, %s, %s);", (pokemon_id_treinador, pokemon_id_selvagem, habilidade_id ))
        
        # Commit das alterações
        conn.commit()

    except Exception as e:
        print(f"Erro ao calcular dano {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()

def calcular_dano_selvagem(conn, pokemon_selvagem, pokemon_treinador, habilidade_id):
    cursor = conn.cursor()

    pokemon_id_selvagem, nome_pokemon_selvagem, nivel_selvagem, hp_selvagem, status_selvagem, nature_selvagem, numero_pokedex_selvagem = pokemon_selvagem
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    try:
        # Chamar a stored procedure ATACA_BATALHA
        cursor.execute("SELECT ATACA_BATALHA(%s, %s, %s);", (pokemon_id_selvagem, pokemon_id_treinador, habilidade_id ))
        
        # Commit das alterações
        conn.commit()

    except Exception as e:
        print(f"Erro ao calcular dano {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()

def batalha_pokemon_npc(conn, id_treinador, pokemon_npc, npc_id):
    os.system('cls')
    global batalha_terminada
    global esta_em_batalha
    esta_em_batalha = True
    batalha_terminada = False
    atacou_primeiro = None
    cursor = conn.cursor()

    pokemon_id_npc, nome_pokemon_npc, nivel_npc, hp_npc, status_npc, nature_npc, numero_pokedex_npc = pokemon_npc
    
    # Obter informações do Pokémon do treinador
    cursor.execute("SELECT * FROM pokemon WHERE treinador_id = %s", (id_treinador,))
    pokemon_treinador = cursor.fetchone()

    if pokemon_treinador:
        pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

        os.system('cls')
        print(f"Você jogou {nome_pokemon_treinador}!\n")
        input("\nPressione Enter para continuar...")

    #Obter informações do nome do adversário
    cursor.execute("SELECT nome_treinador FROM treinador WHERE treinador_id = %s", (npc_id,))
    nometreinador_npc = cursor.fetchone()[0]

    if pokemon_npc:
        print("\n")
        print(f"\n{nometreinador_npc} jogou {nome_pokemon_npc}!!\n")
        input("\nPressione Enter para continuar...")


    while not batalha_terminada:

        os.system('cls')
        
        # Atualize a variável hp com o valor mais recente do banco de dados
        cursor.execute("SELECT hp, status FROM pokemon WHERE treinador_id = %s", (id_treinador,))
        resultado_treinador = cursor.fetchone()
        hp_treinador, status_treinador = resultado_treinador[0], resultado_treinador[1]
        print(f"Seu Pokémon: {nome_pokemon_treinador} (Nível {nivel_treinador})")
        print(f"HP: {hp_treinador} | Status: {status_treinador} | Natureza: {nature_treinador}\n")

        # Atualize a variável hp_npc com o valor mais recente do banco de dados
        cursor.execute("SELECT hp, status FROM pokemon WHERE pokemon_id = %s", (pokemon_id_npc,))
        resultado_npc = cursor.fetchone()
        hp_npc, status_npc = resultado_npc[0], resultado_npc[1]
        print(f"{nome_pokemon_npc} (Nível {nivel_npc})")
        print(f"HP: {hp_npc} | Status: {status_npc} | Natureza: {nature_npc}\n")

        print("Escolha uma opção:")
        print("1. Atacar")
        print("2. Usar Item")

        escolha = input().strip()

        if escolha == '1':
            atacou_primeiro = check_ataca_primeiro(conn, id_treinador, pokemon_treinador, pokemon_npc)
            if atacou_primeiro:
                display_habilidades(conn, id_treinador, pokemon_treinador, pokemon_npc)
            else:
                habilidades_pokemon_npc(conn, id_treinador, pokemon_npc, pokemon_treinador)
            os.system('cls')
            # Atualize a variável hp com o valor mais recente do banco de dados
            cursor.execute("SELECT hp, status FROM pokemon WHERE treinador_id = %s", (id_treinador,))
            resultado_treinador = cursor.fetchone()
            hp_treinador, status_treinador = resultado_treinador[0], resultado_treinador[1]
            # Atualize a variável hp_npc com o valor mais recente do banco de dados
            cursor.execute("SELECT hp, status FROM pokemon WHERE pokemon_id = %s", (pokemon_id_npc,))
            resultado_npc = cursor.fetchone()
            hp_npc, status_npc = resultado_npc[0], resultado_npc[1]

            # Checa se o pokemon npc desmaiou e termina a batalha
            if hp_npc <= 0:
                print(f"Seu Pokémon: {nome_pokemon_treinador} (Nível {nivel_treinador})")
                print(f"HP: {hp_treinador} | Status: {status_treinador} | Natureza: {nature_treinador}\n")

                print(f"{nome_pokemon_npc} (Nível {nivel_npc})")
                print(f"HP: {hp_npc} | Status: {status_npc} | Natureza: {nature_npc}\n")

                print(f"{nome_pokemon_npc} desmaiou!\n")
                input("\nPressione Enter para continuar...")

                os.system('cls')
                print(f"\nVocê derrotou {nome_pokemon_npc}!\n")
                print(f"Você ganhou 10 de XP!\n")

                cursor.execute("SELECT * FROM registro_pokedex WHERE numero_pokemon = %s AND treinador_id = %s", (numero_pokedex_npc, id_treinador,))
                registro_existente = cursor.fetchone()
                if registro_existente:
                    print(f"\n{cor_verde}{nome_pokemon_npc}{reset_cor} já está registrado na sua Pokédex.\n")
                else:
                    cursor.execute("INSERT INTO registro_pokedex (numero_pokemon, treinador_id, capturado) VALUES (%s, %s, %s)", (numero_pokedex_npc, id_treinador, 'Não'))
                    print(f"\n{cor_verde}{nome_pokemon_npc}{reset_cor} foi registrado na Pokédex.\n")

                input("\nPressione Enter para continuar...")
                os.system('cls')
                print(f"\nVocê derrotou {nometreinador_npc}!\n")
                print(f"{nometreinador_npc}: Muito bem! Você conseguiu me derrotar.\nComo prometido, aqui está sua insígnia!\n")
                if nometreinador_npc == 'Brock':
                    print(f"\nVocê ganhou a insígnia da Pedra!\n")
                elif nometreinador_npc == 'Misty':
                    print(f"\nVocê ganhou a insígnia da Água!\n")
                print(f"Você ganhou 500$ pela vitória!\n")
                cursor.execute("UPDATE treinador SET quant_insignias = quant_insignias + 1 WHERE treinador_id = %s", (id_treinador,))
                cursor.execute("UPDATE treinador SET dinheiro = dinheiro + 500 WHERE treinador_id = %s", (id_treinador,))
                input("\nPressione Enter para continuar...")
                batalha_terminada = True
                break

            # Checa se o pokemon npc desmaiou e termina a batalha
            if hp_treinador <= 0:
                print(f"Seu Pokémon: {nome_pokemon_treinador} (Nível {nivel_treinador})")
                print(f"HP: {hp_treinador} | Status: {status_treinador} | Natureza: {nature_treinador}\n")

                print(f"{nome_pokemon_npc} (Nível {nivel_npc})")
                print(f"HP: {hp_npc} | Status: {status_npc} | Natureza: {nature_npc}\n")

                print(f"{nome_pokemon_treinador} desmaiou!\n")
                input("\nPressione Enter para continuar...")

                os.system('cls')
                print(f"\nVocê foi derrotado. A batalha acabou\n")
                cursor.execute("SELECT * FROM registro_pokedex WHERE numero_pokemon = %s AND treinador_id = %s", (numero_pokedex_npc, id_treinador,))
                registro_existente = cursor.fetchone()
                if registro_existente:
                    print(f"\n{cor_verde}{nome_pokemon_npc}{reset_cor} já está registrado na sua Pokédex.\n")
                else:
                    cursor.execute("INSERT INTO registro_pokedex (numero_pokemon, treinador_id, capturado) VALUES (%s, %s, %s)", (numero_pokedex_npc, id_treinador, 'Não'))
                    print(f"\n{cor_verde}{nome_pokemon_npc}{reset_cor} foi registrado na Pokédex.\n")
                input("\nPressione Enter para continuar...")
                batalha_terminada = True
                break

            os.system('cls')
            if not atacou_primeiro:
                display_habilidades(conn, id_treinador, pokemon_treinador, pokemon_npc)
            else:
                os.system('cls')
                habilidades_pokemon_npc(conn, id_treinador, pokemon_npc, pokemon_treinador)

        elif escolha == '2':
            ver_mochila(conn, id_treinador)
        else:
            print("Opção inválida. Tente novamente.")

        #atacou_primeiro = None
    esta_em_batalha = False
    cursor.close()

def check_ataca_primeiro(conn, id_treinador, pokemon_treinador, pokemon_npc):
    cursor = conn.cursor()

    # Obter informações de velocidade dos Pokémon
    cursor.execute("SELECT velocidade FROM pokemon WHERE treinador_id = %s AND pokemon_id = %s", (id_treinador, pokemon_treinador[0]))
    velocidade_treinador = cursor.fetchone()[0]

    cursor.execute("SELECT velocidade FROM pokemon WHERE pokemon_id = %s", (pokemon_npc[0],))
    velocidade_npc = cursor.fetchone()[0]

    # Compara as velocidades para determinar quem ataca primeiro
    if velocidade_treinador > velocidade_npc:
        print(f"Seu Pokémon ataca primeiro!")
        input("\nPressione Enter para continuar...")
        return True
    elif velocidade_treinador < velocidade_npc:
        print(f"O Pokémon oponente ataca primeiro!")
        input("\nPressione Enter para continuar...")
        return False
    else:
        print(f"Ambos os Pokémon têm a mesma velocidade. A ordem de ataque é aleatória.")
        input("\nPressione Enter para continuar...")
        return random.choice([True, False])

    cursor.close()

def habilidades_pokemon_npc(conn, id_treinador, pokemon_npc, pokemon_treinador):
    cursor = conn.cursor()

    pokemon_id_npc, nome_pokemon_npc, nivel_npc, hp_npc, status_npc, nature_npc, numero_pokedex_npc = pokemon_npc
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    # Obtém as habilidades do Pokémon npc
    query = """
    SELECT p.*, h1.NOME_HABILIDADE as habilidade1_nome, h2.NOME_HABILIDADE as habilidade2_nome,
           h3.NOME_HABILIDADE as habilidade3_nome, h4.NOME_HABILIDADE as habilidade4_nome
    FROM pokemon p
    LEFT JOIN habilidade h1 ON p.HABILIDADE1 = h1.HABILIDADE_ID
    LEFT JOIN habilidade h2 ON p.HABILIDADE2 = h2.HABILIDADE_ID
    LEFT JOIN habilidade h3 ON p.HABILIDADE3 = h3.HABILIDADE_ID
    LEFT JOIN habilidade h4 ON p.HABILIDADE4 = h4.HABILIDADE_ID
    WHERE p.pokemon_id = %s
    """
    cursor.execute(query, (pokemon_id_npc,))
    pokemon_info = cursor.fetchone()

    if pokemon_info:
        (
            pokemon_id, numero_pokedex, treinador_id, nome_pokemon,
            habilidade1_id, habilidade2_id, habilidade3_id, habilidade4_id,
            nature, nivel, hp, defesa, ataque, sp_ataque, sp_defesa,
            velocidade, sexo, xp, status, pokebola, altura, peso, localizacao,
            habilidade1_nome, habilidade2_nome, habilidade3_nome, habilidade4_nome
        ) = pokemon_info

        os.system('cls')
        print("O pokemon oponente atacou!\n")
        print(f"Pokémon: {nome_pokemon} (Nível {nivel})")
        print(f"HP: {hp} | Status: {status} | Natureza: {nature}\n\n")

        escolha = str(random.randint(1, 2)).strip()

        habilidades = {
            '1': habilidade1_nome,
            '2': habilidade2_nome,
            #'3': habilidade3_nome if habilidade3_nome else "Ainda não aprendeu",
            #'4': habilidade4_nome if habilidade4_nome else "Ainda não aprendeu"
        }

        habilidade_id = {
            '1': habilidade1_id,
            '2': habilidade2_id,
            #'3': habilidade3_id if habilidade3_id else None,
            #'4': habilidade4_id if habilidade4_id else None
        }

        if escolha in habilidades:
            # Atacar com a habilidade escolhida
            print(f"{nome_pokemon} usou {habilidades[escolha]}\n")
            if habilidade_id[escolha]:
                calcular_dano_npc(conn, pokemon_npc, pokemon_treinador, habilidade_id[escolha])
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Erro.")
    input("\nPressione Enter para continuar...")
    cursor.close()



def display_habilidades(conn, id_treinador, pokemon_treinador, pokemon_npc):
    cursor = conn.cursor()

    pokemon_id_npc, nome_pokemon_npc, nivel_npc, hp_npc, status_npc, nature_npc, numero_pokedex_npc = pokemon_npc
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    # Obtém as habilidades do Pokémon do treinador
    query = """
    SELECT p.*, h1.NOME_HABILIDADE as habilidade1_nome, h2.NOME_HABILIDADE as habilidade2_nome,
           h3.NOME_HABILIDADE as habilidade3_nome, h4.NOME_HABILIDADE as habilidade4_nome
    FROM pokemon p
    LEFT JOIN habilidade h1 ON p.HABILIDADE1 = h1.HABILIDADE_ID
    LEFT JOIN habilidade h2 ON p.HABILIDADE2 = h2.HABILIDADE_ID
    LEFT JOIN habilidade h3 ON p.HABILIDADE3 = h3.HABILIDADE_ID
    LEFT JOIN habilidade h4 ON p.HABILIDADE4 = h4.HABILIDADE_ID
    WHERE p.treinador_id = %s
    """
    cursor.execute(query, (id_treinador,))
    pokemon_info = cursor.fetchone()

    if pokemon_info:
        (
            pokemon_id, numero_pokedex, treinador_id, nome_pokemon,
            habilidade1_id, habilidade2_id, habilidade3_id, habilidade4_id,
            nature, nivel, hp, defesa, ataque, sp_ataque, sp_defesa,
            velocidade, sexo, xp, status, pokebola, altura, peso, localizacao,
            habilidade1_nome, habilidade2_nome, habilidade3_nome, habilidade4_nome
        ) = pokemon_info

        os.system('cls')
        print("Você ataca!\n")
        print(f"Seu Pokémon: {nome_pokemon} (Nível {nivel})")
        print(f"HP: {hp} | Status: {status} | Natureza: {nature}\n")
        print(f"1. {habilidade1_nome}")
        print(f"2. {habilidade2_nome}")
        print(f"3. {habilidade3_nome}" if habilidade3_nome else "3. (Ainda não aprendeu)")
        print(f"4. {habilidade4_nome}" if habilidade4_nome else "4. (Ainda não aprendeu)")

        escolha = input().strip()

        habilidades = {
            '1': habilidade1_nome,
            '2': habilidade2_nome,
            '3': habilidade3_nome if habilidade3_nome else "Ainda não aprendeu",
            '4': habilidade4_nome if habilidade4_nome else "Ainda não aprendeu"
        }

        habilidade_id = {
            '1': habilidade1_id,
            '2': habilidade2_id,
            '3': habilidade3_id if habilidade3_id else None,
            '4': habilidade4_id if habilidade4_id else None
        }

        if escolha in habilidades:
            # Atacar com a habilidade escolhida
            print(f"\n{nome_pokemon} usou {habilidades[escolha]}")
            if habilidade_id[escolha]:
                calcular_dano(conn, pokemon_treinador, pokemon_npc, habilidade_id[escolha])
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Treinador não possui Pokémon.")
    input("\nPressione Enter para continuar...")
    cursor.close()

def calcular_dano(conn, pokemon_treinador, pokemon_npc, habilidade_id):
    cursor = conn.cursor()

    pokemon_id_npc, nome_pokemon_npc, nivel_npc, hp_npc, status_npc, nature_npc, numero_pokedex_npc = pokemon_npc
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    try:
        # Chamar a stored procedure ATACA_BATALHA
        cursor.execute("SELECT ATACA_BATALHA(%s, %s, %s);", (pokemon_id_treinador, pokemon_id_npc, habilidade_id ))
        
        # Commit das alterações
        conn.commit()

    except Exception as e:
        print(f"Erro ao calcular dano {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()

def calcular_dano_npc(conn, pokemon_npc, pokemon_treinador, habilidade_id):
    cursor = conn.cursor()

    pokemon_id_npc, nome_pokemon_npc, nivel_npc, hp_npc, status_npc, nature_npc, numero_pokedex_npc = pokemon_npc
    pokemon_id_treinador, numero_pokedex_treinador, treinador_id_treinador, nome_pokemon_treinador, habilidade1_treinador, habilidade2_treinador, habilidade3_treinador, habilidade4_treinador, nature_treinador, nivel_treinador, hp_treinador, defesa_treinador, ataque_treinador, sp_ataque_treinador, sp_defesa_treinador, velocidade_treinador, sexo_treinador, xp_treinador, status_treinador, pokebola_treinador, altura_treinador, peso_treinador, localizacao_treinador = pokemon_treinador

    try:
        # Chamar a stored procedure ATACA_BATALHA
        cursor.execute("SELECT ATACA_BATALHA(%s, %s, %s);", (pokemon_id_npc, pokemon_id_treinador, habilidade_id ))
        
        # Commit das alterações
        conn.commit()

    except Exception as e:
        print(f"Erro ao calcular dano {e}")

    finally:
        # Fechar o cursor e a conexão
        cursor.close()

def interagir(conn, id_treinador):
    cursor = conn.cursor()

    # Obtém a localização atual do treinador
    cursor.execute("SELECT localizacao FROM treinador WHERE treinador_id = %s", (id_treinador,))
    resultado_treinador = cursor.fetchone()

    if resultado_treinador:
        treinador_localizacao = resultado_treinador[0]

        if treinador_localizacao == 1:
            dialogo_quarto_treinador()
        if treinador_localizacao == 5:
            floresta_viridian(conn, id_treinador)
        
        else:
            # Obtém o NPC na mesma localização
            cursor.execute("SELECT npc_id, info FROM npc WHERE localidade = %s", (treinador_localizacao,))
            npc = cursor.fetchone()

            if npc:
                npc_id, info = npc

                if info == 'Lojista':
                    print("Você está no Pokemart.")
                    comprar_item(conn, id_treinador)
                elif info == 'Enfermeira':
                    usar_pokecenter(conn, id_treinador)
                elif info == 'Professor Oak':
                   os.system('cls')
                   print("Laboratório do Professor Carvalho:\n")
                   escolher_pokemon(conn, id_treinador)
                elif info == 'Mãe':
                    os.system('cls')
                    print("Sala de Casa:\n")
                    dialogoMae()
                elif info == 'Guia da Cidade Inicial':
                    os.system('cls')
                    print("Leste de Pallet:\n")
                    dialogo_leste_palet(conn, id_treinador)
                #elif info == 'Treinador de Campo':
                    #print('Treinador de Campo: Olá, sou um treinador pokémon, vamos batalhar! Se você me vencer, eu te darei uma recompensa!')
                    #batalha(conn, id_treinador, npc_id)
                elif info == 'Brock':
                    os.system('cls')
                    print("Ginásio de Pewter:\n")
                    print('Brock: Olá, Bem vindo! Sou Brock, o líder de ginásio de Pewter, se você me vencer, eu te darei a insígnia da rocha!')
                    input("\nPressione Enter para continuar...")
                    os.system('cls')
                    print('\nDesafiar Brock? (S/N)')
                    escolha = input().strip().upper()
                    input("\nPressione Enter para continuar...")
                    if escolha == 'S': 
                        cursor.execute("SELECT pokemon_id, nome_pokemon_ins, nivel, hp, status, nature, numero_pokedex FROM pokemon WHERE treinador_id = %s", ('2'))
                        pokemon_npc = cursor.fetchone()
                        batalha_pokemon_npc(conn, id_treinador, pokemon_npc, 2)
                    else:
                        print('Brock: Tudo bem, até mais!')
                    
                elif info == 'Treinador da Rota 4':
                    print('Treinador da Rota 4: Olá, sou um treinador pokémon, vamos batalhar! Se você me vencer, eu te darei uma recompensa!')
                    #batalha(conn, id_treinador, npc_id)

                elif info == 'Misty':
                    os.system('cls')
                    print("Ginásio de Cerulean:\n")
                    print('Misty: Olá, Bem vindo! Sou Misty, a líder de ginásio de Cerulean, se você me vencer, eu te darei a insígnia da água!')
                    input("\nPressione Enter para continuar...")
                    os.system('cls')
                    print('\nDesafiar Misty? (S/N)')
                    escolha = input().strip().upper()
                    input("\nPressione Enter para continuar...")
                    if escolha == 'S': 
                        cursor.execute("SELECT pokemon_id, nome_pokemon_ins, nivel, hp, status, nature, numero_pokedex FROM pokemon WHERE treinador_id = %s", ('3'))
                        pokemon_npc = cursor.fetchone()
                        batalha_pokemon_npc(conn, id_treinador, pokemon_npc, 3)
                    else:
                        print('Misty: Tudo bem, até mais!')
                    
                else:
                    print("Você está em uma localização desconhecida.")
            else:
                print("Não há NPCs nesta localização.")
    else:
        print("Treinador não encontrado.")

    cursor.close()

def aventura_pokemon():
    os.system('cls')
    conn = connect_database()
    if conn:
        cursor = conn.cursor()

        # Em seguida, exclua todas as tuplas da tabela treinador
        cursor.execute("TRUNCATE treinador RESTART IDENTITY CASCADE;")

        conn.commit()
        print("\nOlá! Bem-vindo ao Mundo Pokemon!\n\nEu sou o professor Carvalho, e vou te ajudar a começar sua aventura!\n")

        genero = input("\nPrimeiramente, você é um garoto (M) ou uma garota (F)? ").upper()

        nome_treinador = input(f"\nQual é o seu nome, treinador{'a' if genero == 'F' else ''}? ")

        # Bloco adicional para criar um treinador
        if genero in ['M', 'F'] and nome_treinador:
            novo_treinador(conn, genero, nome_treinador) #1
            novo_treinador(conn, 'M', 'Brock') #2
            novo_treinador(conn, 'M', 'Misty') #3
            inserir_pokemon_base(conn)
            os.system('cls')
            print(f"\n{nome_treinador}! Um mundo de aventuras cheio de Pokemons está te esperando, vamos nessa!")
            input("\nPressione Enter para continuar...")
        
        id_treinador = 1  
        
        cursor.execute("INSERT into MOCHILA VALUES (%s, %s, %s)", ('Pokeball', id_treinador,  10))
        cursor.execute("INSERT into MOCHILA VALUES (%s, %s, %s)", ('Potion', id_treinador,  5))

        while True:
            os.system('cls')
            verificar_local_atual(conn, id_treinador)
            verificar_se_ha_npc_na_sala(conn, id_treinador)
            print("\nEscolha uma ação:")
            print("1. Interagir")
            print("2. Andar")
            print("3. Voltar")
            print("4. Ver NPCs no local")
            print("5. Ver informações do treinador")
            print("6. Ver Pokedex")
            print("7. Ver Pokemon")
            print("8. Ver Mochila")
            print("9. Sair")


            escolha = input("\nEscolha uma opção: ")

            if escolha == "1":
                interagir(conn, id_treinador)
                
            elif escolha == "2":
                andar(conn, id_treinador)
                
            elif escolha == "3":
                voltar(conn, id_treinador)
                
            elif escolha == "4":
                verificar_se_ha_npc_na_sala(conn, id_treinador)
                
            elif escolha == "5":
                mostrar_treinador(conn, id_treinador)

            elif escolha == "6":
                ver_pokedex(conn, id_treinador)
                
            elif escolha == "7":
                ver_pokemon(conn, id_treinador)

            elif escolha == "8":
                ver_mochila(conn, id_treinador)

            elif escolha == "9":
                print("\nObrigado por jogar!")
                break
            else:
                print("Escolha inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    aventura_pokemon()
