# 2023.2-Pokemon
Repositório da matéria de Sistemas de Bancos de Dados 1 sobre a modelagem do banco de dados de um jogo do Pokémon
<br><br><br>
<img src="https://scontent.fbsb23-1.fna.fbcdn.net/v/t1.18169-9/13925422_152568501845177_8127161986761319001_n.png?_nc_cat=101&ccb=1-7&_nc_sid=9267fe&_nc_ohc=gR9IEySLzm8AX9Zwghp&_nc_ht=scontent.fbsb23-1.fna&oh=00_AfD8ohdWs32Tiv659Re250BSZ2I5vVGJGTajQCItFcXj9g&oe=65381071"/>

## Alunos

| Nome                             | Matrícula | Github                                         |
| -------------------------------- | --------- | ---------------------------------------------- |
| Felipe de Sousa Coelho           | 211061707 | [@fsousac](https://github.com/fsousac)         |
| XXXALUNOXXX                      | XXXALUNOXXX | XXXALUNOXXX                                  |
| XXXALUNOXXX                      | XXXALUNOXXX | XXXALUNOXXX                                  |
| Murilo Perazzo Barbosa Souto     | 190129221 | [@murilopbs](https://github.com/murilopbs)     |

## Sobre

O objetivo deste projeto é desenvolver um sistema de banco de dados ao criar um jogo envolvendo o universo Pokémon. Neste projeto, aplicaremos os princípios fundamentais de gerenciamento de banco de dados na prática. O desafio consiste em desenvolver um sistema de banco de dados sólido que representará o mundo Pokémon, incluindo treinadores, Pokémon, batalhas. 

## Considerações feitas na modelagem de entidades e relacionamentos e na criação do modelo relacional

* Não hã batalhas em duplas.


## Entregas

### [Módulo 1](https://miro.com/app/board/uXjVMhnb5go=/?share_link_id=944002834733)
  Foi realizada para a entrega do módulo 1 a modelagem do banco de dados do jogo, incluindo o Modelo Entidade-Relacionamento e Diagrama Entidade-Relacionamento (MER e DER), o Modelo Relacional (MREL) e o Dicionário de Dados (DD).

  #### MER:
  **Entidades:**
  
  * **Local:** Representa um local no mundo Pokémon.
  * **Ginásio:** Representa um ginásio Pokémon.
  * **TMs:** Representam as técnicas de movimentos especiais que um Pokémon pode aprender.
  * **Itens Comuns:** Representam itens comuns que podem ser encontrados no mundo Pokémon.
  * **Itens Chave:** Representam itens chave que são necessários para acessar um local.
  * **Pokebolas:** Representam Pokébolas, itens usados para capturar Pokémon.
  * **Ervas:** Representam ervas que podem ser encontradas no mundo Pokémon.
  * **Shop:** Representa uma loja Pokémon.
  * **Loot:** Representa um pacote de itens.
  * **Habilidades:** Representa as habilidades que um Pokémon pode ter.
  * **Pokemon:** Representa um Pokémon.
  * **Batalha:** Representa uma batalha entre dois Pokémon.
  * **Treinador:** Representa um treinador Pokémon.
  * **Pokedex:** Representa a Pokédex, um dispositivo que registra informações sobre Pokémon.
  * **Captura:** Representa um relacionamento um-para-um entre um Pokémon e uma pokebola, indicando que a pokebola capturou aquele Pokémon.
  * **NPCs:** Representam personagens não jogáveis que podem ser encontrados no mundo Pokémon.
  
  **Relacionamentos:**
  
  * **Local - Shop:** Um-para-um. Um local pode ter somete um shop.
  * **Local - Ginásio:** Um-para-um. Uma cidade pode ter somente um ginásio.
  * **Local - NPCs:** Um-para-um. Um NPC ocupa somente um local.
  * **Local - Loot:** Um-para-muitos. Um local pode ter muitos loots.
  * **Local - Pokemon:** Um-para-muitos. Um local pode ter muitos pokemon.
  * **Loot - TMs:** Um-para-muitos. Um loot pode ter muitos TMs.
  * **Loot - Itens Comuns:** Um-para-muitos. Um loot pode ter muitos itens comuns.
  * **Loot - Itens Chave:** Um-para-muitos. Um loot pode ter muitos itens chave.
  * **Loot - Ervas:** Um-para-muitos. Um loot pode ter muitas ervas.
  * **Loot - Pokebolas:** Um-para-muitos. Um loot pode ter muitas pokebolas.
  * **Ginásio - NPCs:** Um-para-muitos. Um ginásio pode ter muitos treinadores NPCs.
  * **Ginásio - NPCs:** Um-para-um. Um ginásio pode somente um líder NPC.
  * **Ginásio - Treinador:** Um-para-um. Um treinador pode enfrentar vários ginásios.
  * **Ginásio - Loot:** Um-para-muitos. Um ginásio pode ter vários pacotes de loot.
  * **Shop - Itens Chave:** Um-para-muitos. Uma loja pode ter muitos itens chave.
  * **Shop - Ervas:** Um-para-muitos. Uma loja pode ter muitas ervas.
  * **Shop - Itens Comuns:** Um-para-muitos. Uma loja pode ter muitos itens comuns.
  * **Shop - Pokebolas:** Um-para-muitos. Uma loja pode ter muitas pokebolas.
  * **Shop - TMs:** Um-para-muitos. Uma loja pode ter muitos TMs.
  * **Pokemon - Habilidades:** Um-para-muitos. Um Pokémon pode ter muitas habilidades.
  * **Pokemon - Pokemon:** Um-para-um. Um pokemon batalha apenas com um pokemon.
  * **Pokemon - Pokedex:** Um-para-muitos. Uma pokedex registra vários pokemons.
  * **Pokemon - Pokebola:** Um-para-muitos. Um tipo de pokebola registra vários pokemons.
  * **Treinador - Pokemon:** Um-para-muitos. Um treinador pode ter muitos Pokémon.
  * **Treinador - Pokedex:** Um-para-um. Um treinador pode ter somente uma Pokedex.
  * **Treinador - NPCs:** Um-para-um. Um treinador pode ser somente um NPC.
  * **Treinador - Itens Chave:** Um-para-muitos. Um treinador pode ter muitos itens chave.
  * **Treinador - Itens Comuns:** Um-para-muitos. Um treinador pode ter muitos itens de posse.
  * **Treinador - Pokebolas:** Um-para-muitos. Um treinador pode ter muitas Pokébolas.
  * **Treinador - TMs:** Um-para-muitos. Um treinador pode ter muitos TMs.
  * **Treinador - Ervas:** Um-para-muitos. Um treinador pode ter muitas ervas.
  * **Treinador - Treinador:** Um-para-um. Um treinador batalha apenas com um treinador.

  #### DER:
  
  ![image](https://github.com/SBD1/2023.2-Pokemon/assets/95441810/2706085f-5923-4aa6-853c-fddd7e590d93)

  
  #### MREL:
  
 ![image](https://github.com/SBD1/2023.2-Pokemon/assets/95441810/399687aa-1326-4270-91ef-e7a5ce844dba)
