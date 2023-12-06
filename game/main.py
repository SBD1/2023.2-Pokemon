import psycopg2
import os
from psycopg2 import sql

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
            print("Local atual:")
            for local in local_atual:
                print(f"Nome: {local[0]}, Descrição: {local[1]}")
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
            os.system('cls')
            print("NPCs na sala:")
            for npc in npcs_na_mesma_sala:
                print(f"ID: {npc[0]}, Função: {npc[1]}")
        else:
            os.system('cls')
            print("Não há NPCs nesta sala.")
    else:
        os.system('cls')
        print("Erro: Treinador não encontrado.")
    
    input("\nPressione Enter para continuar...")

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
            print("Catálogo de itens disponíveis:\n")
            cursor.execute("SELECT item_nome, quantidade, preco FROM catalogo_pokemart")
            catalogo = cursor.fetchall()

            for item in catalogo:
                print(f"Item: {item[0]}, Quantidade: {item[1]}, Preço: {item[2]}")

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
                    print("Professor: Bem-vindo! Venha escolher o seu primeiro pokémon.\n")
                    print("Pokémons Iniciais disponíveis:")
                    for pokemon in pokemons:
                        print(f"ID: {pokemon[0]}, Número Pokédex: {pokemon[1]}, Nome: {pokemon[2]}")

                    # Solicita ao treinador que escolha um Pokémon Inicial
                    while True:
                        escolha_pokemon = input("Digite o nome do Pokémon Inicial que deseja (Bulbasaur, Charmander, Squirtle) ou 0 para sair: ")

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
                                print(f"{nome_pokemon} foi adicionado à sua equipe como seu Pokémon Inicial!")
                                input("\nPressione Enter para continuar...")
                                
                                # Diálogo após a escolha do Pokémon
                                os.system('cls')
                                print("\nProfessor: Agora pegue isto, é uma Pokedex. Você irá utilizá-la para registrar todos os pokémons existentes no Mundo.")
                                print("\nVocê obteve Pokédex!")

                                # Registra o Pokémon na Pokédex
                                cursor.execute("INSERT INTO REGISTRO_POKEDEX (NUMERO_POKEMON, TREINADOR_ID) VALUES (%s, %s)",
                                               (numero_pokedex, id_treinador))

                                conn.commit()
                                print(f"\n{nome_pokemon} foi registrado na Pokédex!")
                                input("\nPressione Enter para continuar...")

                                break
                        else:
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
    print("Guia da cidade inicial: Olá, bem-vindo à cidade de Pallet, aqui é onde sua jornada começa. Você pode ir seguir para o norte para chegar ao laboratório do Professor Carvalho ou voltar para o sul para ir para sua casa.\nTome aqui esse presente para te ajudar na sua jornada.\n\n")

    cursor = conn.cursor()

    # Verificar se a entrada já existe
    cursor.execute("SELECT COUNT(*) FROM MOCHILA WHERE NOME_ITEM = 'Pokebola Comum' AND DONO = %s", (id_treinador,))
    quantidade_existente = cursor.fetchone()[0]

    if quantidade_existente == 0:
        # Se não existir, realizar a inserção
        cursor.execute("INSERT INTO MOCHILA (NOME_ITEM, DONO, QUANTIDADE) VALUES ('Pokebola Comum', %s, 5)", (id_treinador,))
    else:
        # Se existir, realizar a atualização
        cursor.execute("UPDATE MOCHILA SET QUANTIDADE = QUANTIDADE + 5 WHERE NOME_ITEM = 'Pokebola Comum' AND DONO = %s", (id_treinador,))

    conn.commit()

    print("Você recebeu 5 Pokébolas!")
    input("\nPressione Enter para continuar...")
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
                    print("Você está no Centro Pokemon.")
                    #curar_pokemon(conn, id_treinador)
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
                    print("Leste de Palet:\n")
                    dialogo_leste_palet(conn, id_treinador)
                elif info == 'Treinador de Campo':
                    print('Treinador de Campo: Olá, sou um treinador pokémon, vamos batalhar! Se você me vencer, eu te darei uma recompensa!')
                    #batalha(conn, id_treinador, npc_id)
                elif info == 'Brock':
                    print('Brock: Olá, sou Brock, o líder de ginásio de Pewter, se você me vencer, eu te darei a insígnia da rocha!')
                    #batalha(conn, id_treinador, npc_id)
                elif info == 'Treinador da Rota 4':
                    print('Treinador da Rota 4: Olá, sou um treinador pokémon, vamos batalhar! Se você me vencer, eu te darei uma recompensa!')
                    #batalha(conn, id_treinador, npc_id)
                elif info == 'Misty':
                    print('Misty: Olá, sou Misty, a líder de ginásio de Cerulean, se você me vencer, eu te darei a insígnia da água!')
                    #batalha(conn, id_treinador, npc_id)
                else:
                    print("Você está em uma localização desconhecida.")
            else:
                print("Não há NPCs nesta localização.")
    else:
        print("Treinador não encontrado.")

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
    else:
        print("A mochila está vazia.")

    input("\nPressione Enter para continuar...")

def inserir_pokemon_base(conn):
    cursor = conn.cursor()

    # Dados dos Pokémon iniciais
    dados_pokemon = [
        (1, 'Bulbasaur', 1, 'Audacioso', 5, 25, 15, 20, 18, 18, 20, 'M', 0, 'Saudável', 'Pokebola Comum', 70, 70, 4),
        (4, 'Charmander', 1, 'Audacioso', 5, 25, 15, 20, 18, 18, 20, 'M', 0, 'Saudável', 'Pokebola Comum', 70, 70, 4),
        (7, 'Squirtle', 1, 'Audacioso', 5, 25, 15, 20, 18, 18, 20, 'M', 0, 'Saudável', 'Pokebola Comum', 70, 70, 4)
    ]

    for pokemon in dados_pokemon:
        cursor.execute("""
            INSERT INTO POKEMON (
                NUMERO_POKEDEX, NOME_POKEMON_INS, HABILIDADE1, NATURE, NIVEL, HP, DEFESA, ATAQUE, SP_ATAQUE, SP_DEFESA, VELOCIDADE,
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
        # Obtém os Pokémon registrados na Pokédex com informações detalhadas
        cursor.execute("""
            SELECT rp.numero_pokemon, p.nome_pokemon, p.tipo1, p.tipo2, p.nivel_evolucao,
                   p.taxa_captura, p.som_emitido, p.regiao, p.info
            FROM registro_pokedex rp
            JOIN pokedex p ON rp.numero_pokemon = p.numero_pokedex
            WHERE rp.treinador_id = %s
        """, (id_treinador,))
        
        pokemons_registrados = cursor.fetchall()

        if pokemons_registrados:
            os.system('cls')
            print("Pokédex do Treinador:")
            for pokemon in pokemons_registrados:
                print(f"#{pokemon[0]} - {pokemon[1]}")
                print(f"Tipo(s): {pokemon[2]}{' / ' + pokemon[3] if pokemon[3] else ''}")
                print(f"Nível de Evolução: {pokemon[4]}" if pokemon[4] else "")
                print(f"Taxa de Captura: {pokemon[5]}")
                print(f"Som Emitido: {pokemon[6]}")
                print(f"Região: {pokemon[7]}")
                print(f"Informações: {pokemon[8]}")
                print("\n" + "-"*40 + "\n")  # Adicione uma linha separadora entre os Pokémon

        else:
            os.system('cls')
            print("A Pokédex está vazia.")
    else:
        os.system('cls')
        print("O treinador não possui a Pokédex e nenhum Pokémon capturado.")

    input("\nPressione Enter para continuar...")

    cursor.close()


def aventura_pokemon():
    conn = connect_database()
    if conn:
        cursor = conn.cursor()
    

        # Em seguida, exclua todas as tuplas da tabela treinador
        cursor.execute("TRUNCATE treinador RESTART IDENTITY CASCADE;")

        conn.commit()
        print("Olá! Bem-vindo ao Mundo Pokemon!\nEu sou o professor Carvalho, e vou te ajudar a começar sua aventura!\n")

        genero = input("Primeiramente, você é um garoto (M) ou uma garota (F)? ").upper()

        nome_treinador = input(f"Qual é o seu nome, treinador{'a' if genero == 'F' else ''}? ")

        # Bloco adicional para criar um treinador
        if genero in ['M', 'F'] and nome_treinador:
            novo_treinador(conn, genero, nome_treinador)
            inserir_pokemon_base(conn)
            os.system('cls')
            print(f"{nome_treinador}! Um mundo de aventuras cheio de Pokemons está te esperando, vamos nessa!")
            input("\nPressione Enter para continuar...")

        id_treinador = 1  

        while True:
            verificar_local_atual(conn, id_treinador)
            print("\nEscolha uma ação:")
            print("1. Interagir")
            print("2. Andar")
            print("3. Voltar")
            print("4. Ver Pokedex")
            print("5. Ver NPCs na sala")
            print("6. Ver informações do treinador")
            print("7. Ver Pokemon")
            print("8. Ver Mochila")
            print("9. Sair")


            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                interagir(conn, id_treinador)
                
            elif escolha == "2":
                andar(conn, id_treinador)
                
            elif escolha == "3":
                voltar(conn, id_treinador)
                
            elif escolha == "4":
                ver_pokedex(conn, id_treinador)
            elif escolha == "5":
                verificar_se_ha_npc_na_sala(conn, id_treinador)
                
            elif escolha == "6":
                mostrar_treinador(conn, id_treinador)
            elif escolha == "8":
                ver_mochila(conn, id_treinador)
                

    conn.close()

if __name__ == "__main__":
    aventura_pokemon()
