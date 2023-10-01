# MER:
O MER é um modelo conceitual de alto nível de abstração que representa as entidades com os seus atributos, além dos seus respectivos relacionamentos.


**Entidades:**

- **Local:** Representa um local no mundo Pokémon.
- **Ginasio:** Representa um ginásio Pokémon.
- **TMs:** Representam as técnicas de movimentos especiais que um Pokémon pode aprender.
- **Itens Comuns:** Representam itens comuns que podem ser encontrados no mundo Pokémon.
- **Itens Chave:** Representam itens chave que são necessários para acessar um local.
- **Pokebolas:** Representam Pokébolas, itens usados para capturar Pokémon.
- **Ervas:** Representam ervas que podem ser encontradas no mundo Pokémon.
- **Shop:** Representa uma loja Pokémon.
- **Loot:** Representa um pacote de itens.
- **Habilidades:** Representa as habilidades que um Pokémon pode ter.
- **Efeitos:** Representa os efeitos que uma habilidade pode aferir.
- **Pokemon:** Representa um Pokémon.
- **Batalha:** Representa uma batalha entre dois Pokémon.
- **Treinador:** Representa um treinador Pokémon.
- **Pokedex:** Representa a Pokédex, um dispositivo que registra informações sobre Pokémon.
- **NPC:** Representam personagens não jogáveis que podem ser encontrados no mundo Pokémon.

**Relacionamentos:**

- **Local - Shop:** Um-para-um. Um local pode ter somete um shop.
- **Local - Ginasio:** Um-para-um. Uma cidade pode ter somente um ginásio.
- **Local - NPC:** Um-para-um. Um NPC ocupa somente um local.
- **Local - Loot:** Um-para-muitos. Um local pode ter muitos loots.
- **Local - Pokemon:** Um-para-muitos. Um local pode ter muitos pokemon.
- **Loot - TMs:** Um-para-muitos. Um loot pode ter muitos TMs.
- **Loot - Itens Comuns:** Um-para-muitos. Um loot pode ter muitos itens comuns.
- **Loot - Itens Chave:** Um-para-muitos. Um loot pode ter muitos itens chave.
- **Loot - Ervas:** Um-para-muitos. Um loot pode ter muitas ervas.
- **Loot - Pokebolas:** Um-para-muitos. Um loot pode ter muitas pokebolas.
- **Ginasio - NPC:** Um-para-muitos. Um ginásio pode ter muitos treinadores NPC.
- **Ginasio - NPC:** Um-para-um. Um ginásio pode somente um líder NPC.
- **Ginasio - Treinador:** Um-para-um. Um treinador pode enfrentar vários ginásios.
- **Ginasio - Loot:** Um-para-muitos. Um ginásio pode ter vários pacotes de loot.
- **Shop - Itens Chave:** Um-para-muitos. Uma loja pode ter muitos itens chave.
- **Shop - Ervas:** Um-para-muitos. Uma loja pode ter muitas ervas.
- **Shop - Itens Comuns:** Um-para-muitos. Uma loja pode ter muitos itens comuns.
- **Shop - Pokebolas:** Um-para-muitos. Uma loja pode ter muitas pokebolas.
- **Shop - TMs:** Um-para-muitos. Uma loja pode ter muitos TMs.
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
- **Treinador - Ervas:** Um-para-muitos. Um treinador pode ter muitas ervas.
- **Treinador - Treinador:** Um-para-um. Um treinador batalha apenas com um treinador.

# DER:

![image](https://github.com/SBD1/2023.2-Pokemon/assets/95441810/e27ed44b-c0cf-43a0-8206-ea4bf873614c)


## Histórico de versões

| Versão |    Data    | Descrição                                           | Autor                                          |
| :----: | :--------: | --------------------------                          | ---------------------------------------------- |
| `1.0`  | 25/09/2023 | Criação do DER                                      | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.1`  | 28/09/2023 | Criação do MER                                      | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.2`  | 01/10/2023 | Modularização do documento para um arquivo separado | [Felipe de Sousa](https://github.com/fsousac)  |