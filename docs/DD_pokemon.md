
# Dicionário de Dados:

> "Um dicionário de dados é uma coleção de nomes, atributos e definições sobre elementos de dados que estão sendo usados ​​em seu estudo. [...] O objetivo de um dicionário de dados é explicar o que todos os nomes e valores de variáveis ​​em sua planilha realmente significam. Em um dicionário de dados podem ser encontrados dados sobre os nomes das variáveis ​​exatamente como aparecem na planilha, nomes de variáveis ​​curtos (mas legíveis por humanos), o intervalo de valores ou valores aceitos para a variável, descrição da variável e outras informções pertinentes."(Dados Científicos: como construir metadados, descrição, readme, dicionário-de-dados e mais; Agência de Bibliotecas e Coleções Digitais da Universidade de São Paulo)

## Entidade: Local

#### Descrição: A entidade `Local` descreve a localização e informações sobre o local onde as entidades estão como: suas coordenadas, nome e particularidades.

#### Observação: Apesar de várias coordenadas (`Localização`, que é o conjunto de X e Y) poderem pertencer a uma única cidade, nenhuma entidade ocupa a mesma coordenada.

| Nome Variável |     Tipo     |         Descrição         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-----------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|  localização  | varchar[12]  | Localização das entidades |       ASCII        |          não           |    PK    |                   |
|     nome      | varchar[50]  |       Nome do local       |       ASCII        |          não           |          |                   |
|       x       |     int      |       Coordenada X        |      0-25000       |          não           |          |                   |
|       y       |     int      |       Coordenada Y        |      0-25000       |          não           |          |                   |
|     info      | varchar[255] | Informações sobre o Local |       ASCII        |          não           |          |                   |

## Entidade: Ginasio

#### Descrição: A entidade `Ginasio` descreve um local de desafio de cada cidade que concede uma **insígnia** para a continuidade na história do jogo.

#### Observação: O ginásio conta com líderes e treinadores, e e xiste apenas um líder para cada ginásio e apenas um ginásio para cada cidade. Possui uma chave estrangeira para a entidade `Local` do nome da cidade, outra para a entidade `Loot` para o id do loot recebido ao derrotar o ginásio e outra para a entidade `NPC` para o id do líder do ginásio.

| Nome Variável |    Tipo     |         Descrição          | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :------------------------: | :----------------: | :--------------------: | :------: | ----------------- |
| nome_ginasio  | varchar[50] |      Nome do ginásio       |       ASCII        |          não           |    PK    |                   |
|   lider_id    |     int     | Id do NPC lider do ginásio |      0-25000       |          não           |    FK    |                   |
|     tipo1     | varchar[10] |       Tipo primário        |       ASCII        |          não           |          |                   |
|     tipo2     | varchar[10] |      Tipo Secundário       |       ASCII        |          sim           |          |                   |
|    cidade     | varchar[50] | Cidade que sitia o ginásio |       ASCII        |          não           |    FK    |                   |
|     loot      |     int     |   Id do loot do ginásio    |      0-25000       |          não           |    FK    |                   |

## Entidade: TMs

#### Descrição: A entidade `TMs` descreve um item que pode ser usado para ensinar uma das tuplas de `Habilidades` a um Pokémon.

#### Observação: A entidade `TMs` possui uma chave estrangeira para a entidade `Habilidades` para o id da habilidade que o TM ensina.

| Nome Variável |    Tipo     |              Descrição               | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :----------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|   nome_item   | varchar[60] |              Nome do TM              |       ASCII        |          não           |    PK    |                   |
|     dono      |     int     |          Id do Dono ou NULL          |      1-25000       |          sim           |  PK FK   |                   |
|  quantidade   |     int     | Quantidade do item associada ao dono |      1-25000       |          sim           |          |                   |
| habilidade_id |     int     |   Id da habilidade que ele ensina    |      0-25000       |          não           |  SK FK   |                   |

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

## Entidade: PokeMart

#### Descrição: A entidade `PokeMart` descreve uma loja que pode ser encontrada no mundo Pokémon, onde o treinador pode comprar e vender itens.

#### Observação: Esta entidade é chave estrangeira para `Vendedor`, onde mostra quais NPC vendedores trabalham na loja.

| Nome Variável |     Tipo     |                         Descrição                         | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-------------------------------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|    pokemart_id    |     int      |                        Id da loja                         |      0-25000       |          não           |    PK    |                   |
|     nome      | varchar[60]  |                       Nome da loja                        |       ASCII        |          não           |          |                   |
|     local     | varchar[12]  |            Local em que a cidade está sitiada             |       ASCII        |          não           |  SK FK   |                   |
|     info      | varchar[150] | Informações sobre o que a loja vende e como ela se parece |       ASCII        |          não           |          |                   |

## Entidade: Loot

#### Descrição: A entidade `Loot` descreve itens que são encontrados em locais específicos do mundo Pokémon - como cavernas, matagais - ou dados a partir de vitórias de ginásios.

#### Observação: Neste banco de dados não estamos considerando que batalhas pokemon não associadas à um ginásio podem dar loot.

| Nome Variável |    Tipo     |           Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :----------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|    loot_id    |     int     |           Id do loot           |      0-25000       |          não           |    PK    |                   |
|   nome_item   | varchar[60] |       Nome do item dado        |       ASCII        |          não           |  PK FK   |                   |
|  quantidade   |     int     |    Quantidade do item dado     |      1-25000       |          não           |    FK    |                   |
|     local     | varchar[12] | Local onde o loot é encontrado |       ASCII        |          não           |    FK    |                   |

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
|  pokemon_id   |     int     |              Id do pokemon               |      0-25000       |          não           |    PK    |                   |
|   treinador   |     int     |        Id do treinador do pokemon        |      0-25000       |          não           |  PK FK   |                   |
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

## Entidade: Batalha

#### Descrição: A entidade `Batalha` descreve uma batalha entre dois pokemons.

#### Observação: Nesta bese de dados não estamos considerando que há batalhas entre mais de dois pokemons. A entidade possui duas chaves estrageiras de `Pokemon`, onde mostra quais pokemons estão batalhando.

| Nome Variável | Tipo |       Descrição       | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :--: | :-------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|  batalha_id   | int  |     Id da batalha     |      1-25000       |          não           |    PK    |                   |
|   pokemon1    | int  | 1º pokemon da batalha |      1-25000       |          não           |    FK    |                   |
|   pokemon2    | int  | 2º pokemon da batalha |      1-25000       |          não           |    FK    |                   |

## Entidade: Treinador

#### Descrição: A entidade `Treinador` descreve um treinador Pokemon.

#### Observação: `Treinador` é chave estrangeira para todos os tipos de item e para a entidade `NPC`. O atributo sexo recebe apenas um char, sendo ele: 'F' para feminino e 'M' para masculino.

|  Nome Variável  |    Tipo     |               Descrição                | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-------------: | :---------: | :------------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|  treinador_id   |     int     |            Id do treinador             |      0-25000       |          não           |    PK    |                   |
|      nome       | varchar[60] |           Nome do treinador            |       ASCII        |          não           |          |                   |
| ultima_insignia | varchar[60] | Última insignia que o treinador ganhou |       ASCII        |          não           |          |                   |
|  tamanho_time   |   tinyint   |            Tamanho do time             |        0-6         |          não           |          |                   |
|      sexo       | varchar[1]  |           Sexo do treinador            |       ASCII        |          não           |          |                   |
|    dinheiro     |     int     |         Dinheiro do treinador          |     0-1000000      |          não           |          |                   |

## Entidade: Pokedex

#### Descrição: A entidade `Pokedex` descreve um catálogo de todos os pokemons vistos e capiturados pelo treinador.

#### Observação: `Pokedex` recebe uma chave estrangeira de `Pokemon` para consultar seus atributos.

| Nome Variável |     Tipo     |             Descrição             | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :-------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
| treinador_id  |     int      |          Id do treinador          |      0-25000       |          não           |    PK    |                   |
|    pokemon    |     int      |           Id do pokemon           |      0-25000       |          não           |    PK    |                   |
|  localidade   | varchar[60]  | Local onde o pokemon é encontrado |       ASCII        |          sim           |          |                   |
|     info      | varchar[255] |    Informações sobre o pokemon    |       ASCII        |          não           |          |      UNIQUE       |

## Entidade: NPC

#### Descrição: A entidade `NPC` descreve um personagem não jogável do jogo.

#### Observação: A entidade `NPC` recebe uma chave estrangeira de `Treinador` para consultar seus atributos, porém nem todo NPC é treinador. `NPC` recebe uma chave estrangeira de `Ginasio` pois há NPCs que participam dos ginásios mesmo não sendo líderes. Quanto ao atributo sexo, ele recebe apenas um char, sendo ele: 'F' para feminino e 'M' para masculino.

| Nome Variável |     Tipo     |              Descrição              | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :----------: | :---------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|    npc_id     |     int      |              Id do NPC              |      0-25000       |          não           |    PK    |                   |
|   treinador   |     int      |           Id do treinador           |      0-25000       |          sim           |    FK    |                   |
|  localidade   | varchar[12]  |        Local onde o NPC fica        |       ASCII        |          não           |    FK    |                   |
|     sexo      |  varchar[1]  |             Sexo do NPC             |       ASCII        |          não           |          |                   |
|    ginasio    | varchar[50]  | Nome do ginásio que o NPC participa |       ASCII        |          sim           |    FK    |                   |
|     info      | varchar[150] |       Informações sobre o NPC       |       ASCII        |          não           |          |                   |

## Entidade: Itens-vendidos

#### Descrição: A entidade `Itens-vendidos` descreve os itens vendidos por uma loja.

#### Observação: A entidade `Itens-vendidos` recebe uma chave estrangeira de `PokeMart` para identificá-la e outra de alguma entidate-item. A quantidade nula significa infinitos itens a venda.

| Nome Variável |    Tipo     |                Descrição                | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :---------: | :-------------------------------------: | :----------------: | :--------------------: | :------: | :---------------: |
|    pokemart_id    |     int     |               Id da loja                |      0-25000       |          não           |  PK FK   |                   |
|   nome_item   | varchar[60] |          Nome do item vendido           |       ASCII        |          não           |  PK FK   |                   |
|  quantidade   |     int     | Quantidade de itens disponíveis a venda |      1-25000       |          sim           |          |                   |
|     preco     |     int     |              Preço do item              |      0-25000       |          não           |          |                   |

## Entidade: Vendedor

#### Descrição: A entidade `Vendedor` identifica a loja e o NPC que trabalha nela.

#### Observação: A entidade `Vendedor` recebe uma chave estrangeira de `PokeMart` para identificá-la e outra de `NPC` para identificar o NPC que trabalha na loja.

| Nome Variável | Tipo | Descrição  | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :--: | :--------: | :----------------: | :--------------------: | :------: | :---------------: |
|    pokemart_id    | int  | Id da loja |      0-25000       |          não           |  PK FK   |                   |
|    npc_id     | int  | Id do NPC  |      0-25000       |          não           |  PK FK   |                   |

## Entidade: PokeCenter

#### Descrição: A entidade `PokeCenter` descreve um "hospital" que pode ser encontrada no mundo Pokémon, onde o treinador pode curar seus Pokémons.


#### Observação: A entidade `PokeCenter` recebe uma chave estrangeira de `Local` para identificá-la.

| Nome Variável | Tipo | Descrição  | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :--: | :--------: | :----------------: | :--------------------: | :------: | :---------------: |
|    pokecenter_id    | int  | Id do PokeCenter |      0-25000       |          não           |  PK   |                   |
|    cura_disponivel     | int  | Quantidade de cura disponível  |      0-25000       |          não           |     |      |
|  localidade   | varchar[12]  |        Local onde o PokeCenter fica        |       ASCII        |          não           |   SK FK    |                   |
|     info      | varchar[150] |       Informações sobre o NPC       |       ASCII        |          não           |          |                   |


## Entidade: Mochila

#### Descrição: A entidade `Mochila` descreve um meio de armazenar itens do universo Pokemon.


#### Observação: A entidade `Mochila` recebe uma chave estrangeira de `Treinador` para identificá-la.

| Nome Variável | Tipo | Descrição  | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
| :-----------: | :--: | :--------: | :----------------: | :--------------------: | :------: | :---------------: |
|    classificação_item    | int  | Classificação do item |      0-25000       |          não           |  PK   |                   |
| dono  |     int      |          Id do treinador          |      0-25000       |          não           |    PK    |                   |
|    slot    | int  | Slot disponível para item |      0-25000       |          não           |     |                   |                  |



## Histórico de versões

| Versão |    Data    | Descrição                                           | Autor                                          |
| :----: | :--------: | --------------------------                          | ---------------------------------------------- |
| `1.0`  | 01/10/2023 | Criação do DD                                       | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.1`  | 01/10/2023 | Modularização do documento para um arquivo separado | [Felipe de Sousa](https://github.com/fsousac) |
| `1.2`  | 02/10/2023 | Adição de dados | [Murilo Perazzo](https://github.com/murilopbs) |
