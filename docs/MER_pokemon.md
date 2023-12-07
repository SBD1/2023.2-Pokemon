# MER:
O MER é um modelo conceitual de alto nível de abstração que representa as entidades com os seus atributos, além dos seus respectivos relacionamentos.


## Entidades:
- **Treinador:** Representa um personagem que realiza batalhas Pokémon.
- **Localidade:** Representa um local no mundo Pokémon.
- **Mochila:** Representa a mochila do treinador, que guarda os itens para ele.
- **Tipo_Item:** Representa todos os tipos de item do jogo.
- **TMs:** Representam as técnicas de movimentos especiais que um Pokémon pode aprender.
- **Itens Comuns:** Representam itens comuns que podem ser encontrados no mundo Pokémon.
- **Itens Chave:** Representam itens chave que são necessários para acessar um local.
- **Pokebola:** Representam Pokébolas, itens usados para capturar Pokémon.
- **Frutas:** Representam frutas que podem ser encontradas no mundo Pokémon.
- **Pokemon:** Representa uma instância de um pokemon da pokedex.
- **Equipe:** Representa o conjunto de Pokémon que o treinador está utilizando.
- **Tipo:** Representa os tipos de pokemons e habilidades existentes.
- **Habilidade:** Representa o conjunto de Habilidades que o Pokémon pode usar em batalha.
- **Efeito:** Representa os efeitos que uma Habilidade pode causar.
- **NPC:** Representam personagens não jogáveis que podem ser encontrados no mundo Pokémon.
- **Ginasio:** Representa um ginásio Pokémon.
- **PokeNPC** Representa os NPCs que são possíveis batalhar.
- **PokeCenter** Representa um PokeCenter ("hospital") para Pokémons.
- **Enfermeira** Representa a profissão do NPC que cuida do pokecenter.
- **PokeMart** Representa um PokeMart (loja) Pokémon.
- **Lojista**  Representa a profissão do npc que cuida do PokeMart.
- **Pokedex:** Representa um catálogo de todos os pokemons existentes no mundo.
- **Registro_Pokedex:** Representa os Pokémon que o treinador já encontrou.
- **Loot:** Representa os itens que o treinador pode ou não obter após vencer uma batalha.
- **Catalogo_Pokemart:** Representa os itens que estão disponíveis para venda em diferentes PokeMart.
- **Caminho:** Descreve qual localidade liga para qual.


## Relacionamentos:

**Treinador _captura_ Pokémon**

- Um treinador captura um ou vários pokémons (1,N)
- Um Pokémon é capturado por nenhum ou um treinador (0,1)

**Treinador _descobre_ Pokedex**

- Um treinador descobre apenas uma Pokédex (1,1)
- Uma pokédex é descoberta por apenas um treinador (1,1)

**Treinador _está em_ Localidade**

- Um treinador está em apenas uma localidade (1,1)
- Uma localidade pode conter nenhum ou vários treinadores (0,N)

**Treinador _carrega_ Mochila**

- Um treinador carrega apenas uma mochila (1,1)
- Uma mochila é carregada por apenas um treinador (1,1)
  
**Pokedex _instacia_ Pokémon**

- Uma pokédex instancia um ou vários pokémons (1,N)
- Um pokémon é instanciado por nenhuma ou uma pokédex (0,1)
  
**Pokémon _batalha_ Pokémon**

- Um pokémon batalha com apenas um pokémon (1,1)
- (autorelacionamento)

**Pokémon _evolui_**

- Um pokemon evoluí-se nenhuma ou várias vezes (0,N)
- (autorelacionamento)
  
**Pokémon _compõe_ Equipe**
- Um Pokemon compõe nenhuma ou uma equipe (0,1)
- Uma equipe é composta por um ou mais Pokémons (1,N)

**Pokémon _possui_ Tipo**
- Um Pokemon possui um ou vários tipos (1,N)
- Um tipo é possuido por um ou vários Pokémons (1,N)

**Pokémon _tem_ Habilidade**
- Um Pokemon tem uma ou várias habilidades (1,N)
- Uma habilidade é tida por um ou vários pokémons (1,N)

**Habilidade _causa_ Efeito**
- Uma Habilidade causa nenhum ou um efeito (0,1)
- Um Efeito é causado por apenas uma habilidade (1,1)

**Mochila _guarda_ Tipo_Item**
- Uma Mochila guarda nenhum ou vários itens (0,N)
- Um item é guardado por nenhuma ou apenas uma mochila (0,1)

**TM _contém_ Habilidade**
- Um TM contém apenas uma habilidade (1,1)
- Uma habilidade é contida por apenas um TM (1,1)

**Localidade _direciona_ Localidade**
- Uma Localidade direciona para apenas uma localidade (1,1)
- (autorelacionamento)

**Localidade _possui_ NPC**
- Uma Localidade possui nenhum ou vários NPCs (0,N)
- Um NPC é possuído por uma ou várias localidades (1,N)

**Localidade _contém_ Ginásio**
- Uma Localidade contém nenhum ou um Ginásio (0,1)
- Um Ginásio está contido em nenhuma ou uma localidade (0,1)

**Localidade _contém_ PokeCenter**
- Uma Localidade contém nenhum ou um PokeCenter (0,1)
- Um PokeCenter está contido em nenhuma ou uma localidade (0,1)

**Localidade _contém_ PokeMart**
- Uma Localidade contém nenhum ou um PokeMart (0,1)
- Um PokeMart está contido em nenhuma ou uma localidade (0,1)

**Ginásio _gera_ Loot**
- Um Ginásio gera um ou vários loots (1,N)
- Um loot é gerado por nenhum ou um Ginásio (0,1)

**Ginásio _gera_ Loot**
- Um Ginásio gera um ou vários loots (1,N)
- Um loot é gerado por nenhum ou um Ginásio (0,1)

**Enfermeira _mantém_ PokeCenter**
- Uma Enfermeira mantém apenas um PokeCenter (1,1)
- Um PokeCenter é mantido por apenas uma Enfermeira (1,1)

**Lojista _mantém_ PokeMart**
- Um Lojista mantém apenas um PokeMart (1,1)
- Um PokeMart é mantido por apenas um Lojista (1,1)

**PokeNPC _mantém_ Ginásio**
- Um PokeNPC mantém apenas um Ginásio (1,1)
- Um Ginásio é mantido por apenas um ou vários PokeNPC (1,N)

**PokeNPC _gera_ Loot**
- Um PokeNPC gera apenas um loot (1,1)
- Um loot é gerado por nenhum ou um PokeNPC (0,1)

**Catalogo_PokeMart _contém_ Tipo_Item**
- Um Catalogo_PokeMart contém um ou vários Tipo_Item (1,N)
- Um Tipo_Item é contido por nenhum ou vários Catalogo_PokeMart (0,N)

**Loot _contém_ Tipo_Item**
- Um Loot contém um ou vários Tipo_Item (1,N)
- Um Tipo_Item é contido por nenhum ou vários Loots (0,N)

# DER:

![image](https://github.com/SBD1/2023.2-Pokemon/blob/main/docs/imagens/derv5.jpg)

## Para melhor visualização do diagrama
Para visualizar o diagrama em melhor qualidade acesse: https://miro.com/app/board/uXjVNH71dJM=/?share_link_id=763107297566


## Histórico de versões

| Versão |    Data    | Descrição                                           | Autor                                          |
| :----: | :--------: | --------------------------                          | ---------------------------------------------- |
| `1.0`  | 25/09/2023 | Criação do DER                                      | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.1`  | 28/09/2023 | Criação do MER                                      | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.2`  | 01/10/2023 | Modularização do documento para um arquivo separado | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.3`  | 02/10/2023 | Atualização do MER e do DER                         | [Murilo Souto](https://github.com/murilopbs)  |
| `1.4`  | 02/10/2023 | Atualização do DER                                  | [Ian Costa](https://github.com/ian-dcg)  |
| `1.5`  | 04/12/2023 | Atualização do DER pós correção do professor        | [Ian Costa](https://github.com/ian-dcg)  |
| `1.6`  | 04/12/2023 | Atualização das entidades pós correção do professor | [Ian Costa](https://github.com/ian-dcg)  |
| `1.7`  | 04/12/2023 | Atualização dos relacionamentos pós correção do professor | [Ian Costa](https://github.com/ian-dcg)  |
| `1.8`  | 04/12/2023 | Adição do link do quadro Miro do DER                 | [Ian Costa](https://github.com/ian-dcg)  |
