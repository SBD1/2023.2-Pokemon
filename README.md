# 2023.2-Pokemon

Repositório da matéria de Sistemas de Bancos de Dados 1 sobre a modelagem do banco de dados de um jogo do Pokémon
<br><br><br>
<img src="https://scontent.fbsb23-1.fna.fbcdn.net/v/t1.18169-9/13925422_152568501845177_8127161986761319001_n.png?_nc_cat=101&ccb=1-7&_nc_sid=9267fe&_nc_ohc=gR9IEySLzm8AX9Zwghp&_nc_ht=scontent.fbsb23-1.fna&oh=00_AfD8ohdWs32Tiv659Re250BSZ2I5vVGJGTajQCItFcXj9g&oe=65381071"/>

## Alunos

| Nome                         | Matrícula   | Github                                     |
| ---------------------------- | ----------- | ------------------------------------------ |
| Felipe de Sousa Coelho       | 211061707   | [@fsousac](https://github.com/fsousac)     |
| XXXALUNOXXX                  | XXXALUNOXXX | XXXALUNOXXX                                |
| XXXALUNOXXX                  | XXXALUNOXXX | XXXALUNOXXX                                |
| Murilo Perazzo Barbosa Souto | 190129221   | [@murilopbs](https://github.com/murilopbs) |

## Sobre

O objetivo deste projeto é desenvolver um sistema de banco de dados ao criar um jogo envolvendo o universo Pokémon. Neste projeto, aplicaremos os princípios fundamentais de gerenciamento de banco de dados na prática. O desafio consiste em desenvolver um sistema de banco de dados sólido que representará o mundo Pokémon, incluindo treinadores, Pokémon, batalhas.

## Considerações feitas na modelagem de entidades e relacionamentos e na criação do modelo relacional

- Não hã batalhas em duplas.

## Entregas

### [Módulo 1](https://miro.com/app/board/uXjVMhnb5go=/?share_link_id=944002834733)

Foi realizada para a entrega do módulo 1 a modelagem do banco de dados do jogo, incluindo o Modelo Entidade-Relacionamento e Diagrama Entidade-Relacionamento (MER e DER), o Modelo Relacional (MREL) e o Dicionário de Dados (DD).

# MER:

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
- **Captura:** Representa um relacionamento um-para-um entre um Pokémon e uma pokebola, indicando que a pokebola capturou aquele Pokémon.
- **NPCs:** Representam personagens não jogáveis que podem ser encontrados no mundo Pokémon.

**Relacionamentos:**

- **Local - Shop:** Um-para-um. Um local pode ter somete um shop.
- **Local - Ginasio:** Um-para-um. Uma cidade pode ter somente um ginásio.
- **Local - NPCs:** Um-para-um. Um NPC ocupa somente um local.
- **Local - Loot:** Um-para-muitos. Um local pode ter muitos loots.
- **Local - Pokemon:** Um-para-muitos. Um local pode ter muitos pokemon.
- **Loot - TMs:** Um-para-muitos. Um loot pode ter muitos TMs.
- **Loot - Itens Comuns:** Um-para-muitos. Um loot pode ter muitos itens comuns.
- **Loot - Itens Chave:** Um-para-muitos. Um loot pode ter muitos itens chave.
- **Loot - Ervas:** Um-para-muitos. Um loot pode ter muitas ervas.
- **Loot - Pokebolas:** Um-para-muitos. Um loot pode ter muitas pokebolas.
- **Ginasio - NPCs:** Um-para-muitos. Um ginásio pode ter muitos treinadores NPCs.
- **Ginasio - NPCs:** Um-para-um. Um ginásio pode somente um líder NPC.
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
- **Treinador - NPCs:** Um-para-um. Um treinador pode ser somente um NPC.
- **Treinador - Itens Chave:** Um-para-muitos. Um treinador pode ter muitos itens chave.
- **Treinador - Itens Comuns:** Um-para-muitos. Um treinador pode ter muitos itens de posse.
- **Treinador - Pokebolas:** Um-para-muitos. Um treinador pode ter muitas Pokébolas.
- **Treinador - TMs:** Um-para-muitos. Um treinador pode ter muitos TMs.
- **Treinador - Ervas:** Um-para-muitos. Um treinador pode ter muitas ervas.
- **Treinador - Treinador:** Um-para-um. Um treinador batalha apenas com um treinador.

# DER:

![image](https://github.com/SBD1/2023.2-Pokemon/assets/95441810/2706085f-5923-4aa6-853c-fddd7e590d93)

# MREL:

![image](https://github.com/SBD1/2023.2-Pokemon/assets/95441810/399687aa-1326-4270-91ef-e7a5ce844dba)

# Dicionário de Dados:

> "Um dicionário de dados é uma coleção de nomes, atributos e definições sobre elementos de dados que estão sendo usados ​​em seu estudo. [...] O objetivo de um dicionário de dados é explicar o que todos os nomes e valores de variáveis ​​em sua planilha realmente significam. Em um dicionário de dados podem ser encontrados dados sobre os nomes das variáveis ​​exatamente como aparecem na planilha, nomes de variáveis ​​curtos (mas legíveis por humanos), o intervalo de valores ou valores aceitos para a variável, descrição da variável e outras informções pertinentes."(Dados Científicos: como construir metadados, descrição, readme, dicionário-de-dados e mais; Agência de Bibliotecas e Coleções Digitais da Universidade de São Paulo)

## Entidade: Local

#### Descrição: A entidade `Local` descreve a localização e informações sobre o local onde as entidades estão como: suas coordenadas, nome e particularidades.

#### Observação: Apesar de várias coordenadas (`Localização`, que é o conjunto de X e Y) poderem pertencer a uma única cidade, nenhuma entidade ocupa a mesma coordenada.

| Nome Variável |     Tipo     |         Descrição         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-----------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|  localização  | varchar[50]  | Localização das entidades |       ASCII        |          não           |    PK    |                   |
|     nome      | varchar[50]  |       Nome do local       |       ASCII        |          não           |          |                   |
|       x       |     int      |       Coordenada X        |      1-25000       |          não           |    PK    |                   |
|       y       |     int      |       Coordenada Y        |      1-25000       |          não           |    PK    |                   |
|     info      | varchar[255] | Informações sobre o Local |       ASCII        |          não           |          |                   |

## Entidade: Ginasio

#### Descrição: A entidade `Ginasio` descreve um local de desafio de cada cidade que concede uma **insígnia** para a continuidade na história do jogo.

#### Observação: O ginásio conta com líderes e treinadores, e e xiste apenas um líder para cada ginásio e apenas um ginásio para cada cidade. Possui uma chave estrangeira para a entidade `Local` do nome da cidade, outra para a entidade `Loot` para o id do loot recebido ao derrotar o ginásio e outra para a entidade `NPC` para o id do líder do ginásio.

| Nome Variável |    Tipo     |         Descrição          | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
| nome_ginasio  | varchar[50] |      Nome do ginásio       |       ASCII        |          não           |    PK    |                   |
|   lider_id    |     int     | Id do NPC lider do ginásio |      1-25000       |          não           |    FK    |                   |
|     tipo1     | varchar[10] |       Tipo primário        |       ASCII        |          não           |          |                   |
|     tipo2     | varchar[10] |      Tipo Secundário       |       ASCII        |          sim           |          |                   |
|    cidade     | varchar[50] | Cidade que sitia o ginásio |       ASCII        |          não           |    FK    |                   |
|     loot      |     int     |   Id do loot do ginásio    |      1-25000       |          não           |    FK    |                   |

## Entidade: TMs

#### Descrição: A entidade `TMs` descreve um item que pode ser usado para ensinar uma das tuplas de `Habilidades` a um Pokémon.

#### Observação: A entidade `TMs` possui uma chave estrangeira para a entidade `Habilidades` para o id da habilidade que o TM ensina.

| Nome Variável |    Tipo     |              Descrição               | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :----------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|   nome_item   | varchar[60] |              Nome do TM              |       ASCII        |          não           |    PK    |                   |
|     dono      |     int     |          Id do Dono ou NULL          |      1-25000       |          sim           |  PK FK   |                   |
|  quantidade   |     int     | Quantidade do item associada ao dono |      1-25000       |          sim           |          |                   |
| habilidade_id |     int     |   Id da habilidade que ele ensina    |      1-25000       |          não           |    FK    |      UNIQUE       |

## Entidade: Itens-Comuns

#### Descrição: A entidade `Itens-Comuns` descreve itens comuns que podem ser encontrados no mundo Pokémon, como potions, repels, etc.

#### Observação: Tem o mesmo princípio de quantidade que a entidade `TMs`.

| Nome Variável |     Tipo     |              Descrição               | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :----------------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   nome_item   | varchar[60]  |             Nome do item             |       ASCII        |          não           |    PK    |                   |
|     dono      |     int      |          Id do Dono ou NULL          |      1-25000       |          sim           |  PK FK   |                   |
|  quantidade   |     int      | Quantidade do item associada ao dono |      1-25000       |          sim           |          |                   |
|    efeito     | varchar[150] |        Efeito ao usar o item         |       ASCII        |          não           |          |                   |

## Entidade: Itens-Chave

#### Descrição: A entidade `Itens-Chave` descreve itens chave que podem ser encontrados no mundo Pokémon, como insígnias, bikes, gliders, etc.

#### Observação: Tem o mesmo princípio de quantidade que a entidade `TMs`.

| Nome Variável |     Tipo     |              Descrição               | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :----------------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   nome_item   | varchar[60]  |             Nome do item             |       ASCII        |          não           |    PK    |                   |
|     dono      |     int      |          Id do Dono ou NULL          |      1-25000       |          sim           |  PK FK   |                   |
|  quantidade   |     int      | Quantidade do item associada ao dono |      1-25000       |          sim           |          |                   |
|   utilidade   | varchar[150] |          Utilidade do item           |       ASCII        |          não           |          |                   |

## Entidade: Pokebolas

#### Descrição: A entidade `Pokebolas` descreve pokebolas que servem para o treinador capturar pokemons e adicioná-los ao seu time, são exemplos a UltraBall, GreatBall, MasterBall, etc.

#### Observação: Tem o mesmo princípio de quantidade que a entidade `TMs` e tem seu nome vinculado ao atributo `Pokebola` da entidade `Pokemon`.

| Nome Variável |    Tipo     |                  Descrição                   | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :------------------------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   nome_item   | varchar[60] |                 Nome do item                 |       ASCII        |          não           |    PK    |                   |
|     dono      |     int     |              Id do Dono ou NULL              |      1-25000       |          sim           |  PK FK   |                   |
|  quantidade   |     int     |     Quantidade do item associada ao dono     |      1-25000       |          sim           |          |                   |
|     Força     |     int     | Quantidade de "força de captura" da pokebola |      1-25000       |          não           |          |                   |

## Entidade: Ervas

#### Descrição: A entidade `Ervas` descreve Ervas medicinais que servem para o treinador curar ou dar algum efeito aos seus pokemons, são exemplos a Energy Powder, Energy Root, Fresh Water, etc.

#### Observação: Tem o mesmo princípio de quantidade que a entidade `TMs`.

| Nome Variável |     Tipo     |              Descrição               | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :----------------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
|   nome_item   | varchar[60]  |             Nome da erva             |       ASCII        |          não           |    PK    |                   |
|     dono      |     int      |          Id do Dono ou NULL          |      1-25000       |          sim           |  PK FK   |                   |
|  quantidade   |     int      | Quantidade do item associada ao dono |      1-25000       |          sim           |          |                   |
|    efeito     | varchar[150] |        Efeito ao usar a erva         |       ASCII        |          não           |          |                   |

## Entidade: Shop

#### Descrição: A entidade `Shop` descreve uma loja que pode ser encontrada no mundo Pokémon, onde o treinador pode comprar e vender itens.

#### Observação: Esta entidade é chave estrangeira para `Vendedor`, onde mostra quais NPCs vendedores trabalham na loja.

| Nome Variável |     Tipo     |                         Descrição                         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-------------------------------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|    shop_id    |     int      |                        Id da loja                         |      1-25000       |          não           |    PK    |                   |
|     nome      | varchar[60]  |                       Nome da loja                        |       ASCII        |          não           |          |                   |
|    cidade     |     int      |            Local em que a cidade está sitiada             |      1-25000       |          não           |    FK    |      UNIQUE       |
|     info      | varchar[150] | Informações sobre o que a loja vende e como ela se parece |       ASCII        |          não           |          |                   |

## Entidade: Loot

#### Descrição: A entidade `Loot` descreve itens que são encontrados em locais específicos do mundo Pokémon - como cavernas, matagais - ou dados a partir de vitórias de ginásios.

#### Observação: Neste banco de dados não estamos considerando que batalhas pokemon não associadas à um ginásio podem dar loot.

| Nome Variável | Tipo |           Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :--: | :----------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|    loot_id    | int  |           Id do loot           |      1-25000       |          não           |    PK    |                   |
|    item_id    | int  |        Id do item dado         |      1-25000       |          não           |  PK FK   |                   |
|  quantidade   | int  |    Quantidade do item dado     |      1-25000       |          não           |    FK    |                   |
|     local     | int  | Local onde o loot é encontrado |      1-25000       |          não           |    FK    |                   |

## Entidade: Habilidades

#### Descrição: A entidade `Habilidades` descreve as habilidades que um Pokémon pode ter.

#### Observação: Esta entidade é chave estrangeira para `Pokemon`, onde mostra quais habilidades o pokemon associado possui. O atributo alcance somente admite um char de tamanho 1, que pode ser: 'f' de físico, 'd' de à distância. O atributo alvo somente admite um char de tamanho 1, que pode ser: 's' para si próprio, 'e' para um inimigo, 't' para o próprio time, 'i' para o time inimigo e 'a' para todos no campo.

|  Nome Variável  |     Tipo     |                Descrição                | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-------------: | :----------: | :-------------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
| nome_habilidade | varchar[60]  |           Nome da habilidade            |       ASCII        |          não           |    PK    |                   |
|      tipo       | varchar[10]  |       Tipo primário da habilidade       |       ASCII        |          não           |          |                   |
|     alcance     |  varchar[1]  |          Alcance da habilidade          |       ASCII        |          não           |          |                   |
|      alvo       |  varchar[1]  |          Alvo(s) da habilidade          |       ASCII        |          não           |          |                   |
|      dano       |     int      |           Dano da habilidadde           |      1-25000       |          sim           |          |                   |
|    acuracia     |     int      |         Acurácia da habilidade          |       1-100        |          não           |          |                   |
|     efeito      |     int      | Id do efeito que habilidade pode causar |      1-25000       |          sim           |    FK    |                   |
|      info       | varchar[150] |     Informações sobre a habilidade      |       ASCII        |          não           |          |      UNIQUE       |

## Entidade: Efeitos

#### Descrição: A entidade `Efeitos` descreve os efeitos que uma habilidade pode inferir.

#### Observação: Esta entidade é chave estrangeira para `Habilidades`, onde mostra qual efeito a habilidade associada possui.

| Nome Variável |     Tipo     |         Descrição          | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|  efeito_nome  | varchar[30]  |       Nome do efeito       |       ASCII        |          não           |    PK    |                   |
|   acuracia    |     int      |     Acurácia do efeito     |       1-100        |          não           |          |                   |
|     dano      |     int      |       Dano do efeito       |      1-25000       |          sim           |          |                   |
|     info      | varchar[150] | Informações sobre o efeito |       ASCII        |          não           |          |                   |

## Entidade: Pokemon

#### Descrição: A entidade `Pokemon` descreve um Pokémon.

#### Observação: Esta entidade é chave estrangeira para `Batalha`, onde identifica os pokemons que estão batalhando, além de ser registrada também na entidade `Pokedex`.

| Nome Variável |    Tipo     |                Descrição                 | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :--------------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|  pokemon_id   |     int     |              Id do pokemon               |      1-25000       |          não           |    PK    |                   |
|   treinador   |     int     |       Nome do treinador do pokemon       |      1-25000       |          não           |  PK FK   |                   |
| nome_pokemon  | varchar[60] |             Nome do pokemon              |       ASCII        |          não           |          |                   |
|     tipo1     | varchar[10] |         Tipo primário do pokemon         |       ASCII        |          não           |          |                   |
|     tipo2     | varchar[10] |        Tipo secundário do pokemon        |       ASCII        |          sim           |          |                   |
|  habilidade1  | varchar[60] |              1ª habilidade               |       ASCII        |          não           |    FK    |                   |
|  habilidade2  | varchar[60] |              2ª habilidade               |       ASCII        |          sim           |    FK    |                   |
|  habilidade3  | varchar[60] |              3ª habilidade               |       ASCII        |          sim           |    FK    |                   |
|  habilidade4  | varchar[60] |              4ª habilidade               |       ASCII        |          sim           |    FK    |                   |
|    nature     | varchar[10] |            Nature do pokemon             |       ASCII        |          não           |          |                   |
|     nivel     |  small int  |             Nível do pokemon             |        1-80        |          não           |          |                   |
|      hp       |  small int  |      Quantidade de vida do pokemon       |       1-2000       |          não           |          |                   |
|    defesa     |  small int  |     Quantidade de defesa do pokemon      |       1-2000       |          não           |          |                   |
|    ataque     |  small int  |     Quantidade de ataque do pokemon      |       1-2000       |          não           |          |                   |
|   sp_defesa   |  small int  | Quantidade de defesa especial do pokemon |       1-2000       |          não           |          |                   |
|   sp_ataque   |  small int  | Quantidade de ataque especial do pokemon |       1-2000       |          não           |          |                   |
|  velocidade   |  small int  |   Quantidade de velocidade do pokemon    |       1-2000       |          não           |          |                   |
|   acuracia    |  small int  |           Acurácia do pokemon            |       1-2000       |          não           |          |                   |
|     sexo      | varchar[1]  |             Sexo do pokemon              |       ASCII        |          não           |          |                   |
|    status     | varchar[10] |            Status do pokemon             |       ASCII        |          sim           |          |                   |
|   pokebola    | varchar[60] |     Pokebola que capturou o pokemon      |       ASCII        |          não           |    FK    |                   |

## Histórico de versões

| Versão |    Data    | Descrição                  | Autor                                          |
| :----: | :--------: | -------------------------- | ---------------------------------------------- |
| `1.0`  | 24/09/2023 | Criação do README          | [Murilo Perazzo](https://github.com/murilopbs) |
| `1.1`  | 27/09/2023 | Inserção do MER,DER e MREL | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.2`  | 30/09/2023 | Inserção do DD             | [Felipe de Sousa](https://github.com/fsousac)  |
