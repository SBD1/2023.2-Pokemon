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

- **Mapa - Região:** Um-para-muitos. O mapa pode possuir uma ou várias regiões.
- **Região - PokeMart:** Um-para-um. Uma Região pode conter no máximo um PokeMart.
- **Região - Ginasio:** Um-para-um. Uma Região pode conter no máximo um Ginásio. 
- **Região - NPC:** Um-para-um. Um NPC ocupa somente um local.
- **Região - Loot:** Um-para-muitos. Um local pode ter muitos loots.
- **Região - Pokemon:** Um-para-muitos. Um local pode ter muitos pokemon.
- **Loot - TMs:** Um-para-muitos. Um loot pode ter muitos TMs.
- **Loot - Itens Comuns:** Um-para-muitos. Um loot pode ter muitos itens comuns.
- **Loot - Itens Chave:** Um-para-muitos. Um loot pode ter muitos itens chave.
- **Loot - Ervas:** Um-para-muitos. Um loot pode ter muitas ervas.
- **Loot - Pokebolas:** Um-para-muitos. Um loot pode ter muitas pokebolas.
- **Ginasio - NPC:** Um-para-muitos. Um ginásio pode ter muitos treinadores NPC.
- **Ginasio - NPC:** Um-para-um. Um ginásio pode somente um líder NPC.
- **Ginasio - Treinador:** Um-para-um. Um treinador pode enfrentar vários ginásios.
- **Ginasio - Loot:** Um-para-muitos. Um ginásio pode ter vários pacotes de loot.
- **PokeMart - Itens Chave:** Um-para-muitos. Uma loja pode ter muitos itens chave.
- **PokeMart - Frutas:** Um-para-muitos. Uma loja pode ter muitas Frutas.
- **PokeMart - Itens Comuns:** Um-para-muitos. Uma loja pode ter muitos itens comuns.
- **PokeMart - Pokebolas:** Um-para-muitos. Uma loja pode ter muitas pokebolas.
- **PokeMart - TMs:** Um-para-muitos. Uma loja pode ter muitos TMs.
- **Habilidade - Efeito:** Um-para-um. Uma habilidade pode causar apenas um efeito no máximo.
- **Pokemon - Habilidades:** Um-para-muitos. Um Pokémon pode ter muitas habilidades.
- **Pokemon - Pokemon:** Um-para-um. Um pokemon batalha apenas com um pokemon.
- **Pokemon - Pokedex:** Um-para-muitos. Uma pokedex registra vários pokemons.
- **Pokemon - Pokebola:** Um-para-muitos. Um tipo de pokebola registra vários pokemons.
- **Treinador - Pokemon:** Um-para-muitos. Um treinador pode ter muitos Pokémon.
- **Treinador - Pokedex:** Um-para-um. Um treinador pode ter somente uma Pokedex.
- **Treinador - NPC:** Um-para-um. Um treinador pode ser somente um NPC.
- **Treinador - Itens Chave:** Um-para-muitos. Um treinador pode ter muitos itens chave.
- **Treinador - Itens Comuns:** Um-para-muitos. Um treinador pode ter muitos itens de posse.
- **Treinador - Pokebolas:** Um-para-muitos. Um treinador pode ter muitas Pokébolas.
- **Treinador - TMs:** Um-para-muitos. Um treinador pode ter muitos TMs.
- **Treinador - Frutas:** Um-para-muitos. Um treinador pode ter muitas Frutas.
- **Treinador - Treinador:** Um-para-um. Um treinador batalha apenas com um treinador.

# DER:

![image](https://github.com/SBD1/2023.2-Pokemon/blob/main/docs/imagens/derv5.jpg)

## Para melhor visualização do diagrama
Para visualizar o diagrama em melhor qualidade acesse: 


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
