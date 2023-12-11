
# Dicionário de Dados:

> "Um dicionário de dados é uma coleção de nomes, atributos e definições sobre elementos de dados que estão sendo usados ​​em seu estudo. [...] O objetivo de um dicionário de dados é explicar o que todos os nomes e valores de variáveis ​​em sua planilha realmente significam. Em um dicionário de dados podem ser encontrados dados sobre os nomes das variáveis ​​exatamente como aparecem na planilha, nomes de variáveis ​​curtos (mas legíveis por humanos), o intervalo de valores ou valores aceitos para a variável, descrição da variável e outras informções pertinentes."(Dados Científicos: como construir metadados, descrição, readme, dicionário-de-dados e mais; Agência de Bibliotecas e Coleções Digitais da Universidade de São Paulo)

## Entidade: Localidade

#### Descrição
Representa uma localização no jogo, com informações detalhadas e um mapa associado.

#### Observação
A coluna `NOME` possui uma restrição de chave única `sk_nome_local`.

| Nome Variável | Tipo         | Descrição                    | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|------------------------------|--------------------|------------------------|----------|-------------------|
| LOCALIZACAO   | serial       | Identificador único da localidade. | Autoincrementado | Não | PK |                   |
| NOME          | VARCHAR(50)  | Nome da localidade.          | ASCII              | Não |    | UNIQUE            |
| INFO          | VARCHAR(255) | Informações sobre a localidade. | ASCII           | Não |    |                   |
| MAPA          | VARCHAR(255) | Mapa da localidade.          | ASCII              | Não |    |                   |

## Entidade: Caminho

#### Descrição
Descreve o autorrelacionamento entre localidades, mostrando a sala a seguir e a sala anterior.

#### Observação
A entidade possui a PK composta entre os dois caminhos `SALA_ATUAL` e `PROXIMA_SALA`, assim como as mesmas colunas são FK de `Localidade` referenciando a coluna `LOCALIZACAO`.

| Nome Variável | Tipo | Descrição | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|------|-----------|--------------------|------------------------|----------|-------------------|
| SALA_ATUAL    | int  | Id da sala atual. | 1-25000 | Não | PK, FK |                   |
| PROXIMA_SALA  | int  | Id da próxima sala. | 1-25000 | Não | PK, FK |                   |

## Entidade: Treinador

#### Descrição
Descreve um personagem do jogo que possui pokémons, seja PC ou NPC. A tabela descreve atributos gerais de treinador como nome, sexo, localização, etc.

#### Observação
A entidade é FK para algumas outras tabelas e possui uma FK de `Localidade` referenciando a coluna `LOCALIZACAO` para demonstrar o local onde o Treinador se encontra. A coluna `TREINADOR_ID` possui o tipo _serial_ em que possui seus valores auto-incrementados sozinhos pelo banco.

| Nome Variável       | Tipo        | Descrição | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------------|-------------|-----------|--------------------|------------------------|----------|-------------------|
| TREINADOR_ID        | serial      | Identificador único do treinador. | Autoincrementado | Não | PK |                   |
| NOME_TREINADOR      | VARCHAR(50) | Nome do treinador. | ASCII | Não |    |                   |
| SEXO                | CHAR(1)     | Sexo do treinador. | 'F' ou 'M' | Não |    |                   |
| LOCALIZACAO         | int         | Localização atual do treinador. | 1-25000 | Não | FK |                   |
| QUANT_INSIGNIAS     | int         | Quantidade de insígnias conquistadas pelo treinador. | 0-10 | Não |    |                   |
| QUANT_PK_CAPTURADOS | int         | Quantidade de pokémons capturados pelo treinador. | 0-25000 | Não |    |                   |
| DINHEIRO            | int         | Quantidade de dinheiro que o treinador possui. | 0-25000 | Não |    |                   |

## Entidade: Tipo_Item

#### Descrição
Define os tipos de itens disponíveis no jogo.

#### Observação
A entidade `Tipo_Item` é utilizada como referência para outras tabelas de itens.

| Nome Variável | Tipo      | Descrição              | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|-----------|------------------------|--------------------|------------------------|----------|-------------------|
| NOME_ITEM     | VARCHAR(60) | Nome do tipo de item. | ASCII              | Não | PK |                   |
| TIPO_ITEM     | CHAR(1)   | Categoria do item.     | ASCII              | Não |    |                   |

## Entidade: Item_Comum

#### Descrição
Representa itens comuns que podem ser utilizados pelos treinadores no jogo.

#### Observação
A entidade `Item_Comum` é uma especialização da entidade `Tipo_Item`.

| Nome Variável | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_ITEM     | VARCHAR(60)  | Nome do item comum.  | ASCII              | Não | PK, FK |                   |
| EFEITO        | VARCHAR(150) | Efeito do item.      | ASCII              | Sim |    |                   |

## Entidade: Item_Chave

#### Descrição
Representa itens chave que são essenciais para o progresso no jogo.

#### Observação
A entidade `Item_Chave` é uma especialização da entidade `Tipo_Item`.

| Nome Variável | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_ITEM     | VARCHAR(60)  | Nome do item chave.  | ASCII              | Não | PK, FK |                   |
| UTILIDADE     | VARCHAR(150) | Utilidade do item.   | ASCII              | Sim |    |                   |

## Entidade: Fruta

#### Descrição
Representa frutas que podem ser utilizadas pelos treinadores para diversos efeitos no jogo.

#### Observação
A entidade `Fruta` é uma especialização da entidade `Tipo_Item`.

| Nome Variável | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_ITEM     | VARCHAR(60)  | Nome da fruta.       | ASCII              | Não | PK, FK |                   |
| EFEITO        | VARCHAR(150) | Efeito da fruta.     | ASCII              | Sim |    |                   |

## Entidade: Tipo

#### Descrição
Define os tipos de pokémons e habilidades no jogo.

#### Observação
A entidade `Tipo` é utilizada como referência para a entidade `Habilidade`.

| Nome Variável | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_TIPO     | VARCHAR(15)  | Nome do tipo.        | ASCII              | Não | PK |                   |

## Entidade: Efeito

#### Descrição
Define os efeitos que as habilidades podem ter no jogo.

#### Observação
A entidade `Efeito` é utilizada como referência para a entidade `Habilidade`.

| Nome Variável | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_EFEITO   | VARCHAR(15)  | Nome do efeito.      | ASCII              | Não | PK |                   |
| ACURACIA      | SMALLINT     | Acurácia do efeito.  | 0-100              | Não |    |                   |
| DANO          | SMALLINT     | Dano causado pelo efeito. | 0-100          | Sim |    |                   |
| INFO          | VARCHAR(150) | Informações sobre o efeito. | ASCII       | Não |    |                   |

## Entidade: Habilidade

#### Descrição
Define as habilidades que os pokémons podem aprender e utilizar no jogo.

#### Observação
A entidade `Habilidade` possui chaves estrangeiras referenciando as entidades `Tipo` e `Efeito`.

| Nome Variável   | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|-----------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| HABILIDADE_ID   | serial       | Identificador único da habilidade. | Autoincrementado | Não | PK |                   |
| NOME_HABILIDADE | VARCHAR(20)  | Nome da habilidade.  | ASCII              | Não |    | UNIQUE            |
| TIPO_DANO       | CHAR(1)      | Tipo de dano da habilidade. | ASCII       | Não |    |                   |
| DANO            | SMALLINT     | Dano causado pela habilidade. | Numérico  | Sim |    |                   |
| TIPO            | VARCHAR(15)  | Tipo da habilidade.  | ASCII              | Não | FK |                   |
| ACURACIA        | int          | Acurácia da habilidade. | Numérico       | Não |    |                   |
| EFEITO          | VARCHAR(15)  | Efeito da habilidade. | ASCII             | Sim | FK |                   |
| INFO            | VARCHAR(150) | Informações sobre a habilidade. | ASCII   | Não |    |                   |

## Entidade: TM

#### Descrição
Representa os TMs (Technical Machines) que ensinam habilidades aos pokémons.

#### Observação
A entidade `TM` possui uma chave estrangeira referenciando a entidade `Habilidade`.

| Nome Variável   | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|-----------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_ITEM       | VARCHAR(60)  | Nome do TM.          | ASCII              | Não | PK, FK |                   |
| HABILIDADE_ID   | int          | Identificador da habilidade associada ao TM. | Numérico | Não | FK | UNIQUE            |

## Entidade: Pokebola

#### Descrição
Define os diferentes tipos de pokébolas usadas para capturar pokémons.

#### Observação
A entidade `Pokebola` possui uma restrição de verificação para garantir que a força esteja dentro de um intervalo válido.

| Nome Variável | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_ITEM     | VARCHAR(60)  | Nome da pokébola.    | ASCII              | Não | PK, FK |                   |
| FORCA         | SMALLINT     | Força da pokébola.   | 0-100              | Não |    | CHECK (FORCA >= 0 AND FORCA <= 100) |

## Entidade: Mochila

#### Descrição
Representa a mochila de um treinador, contendo itens.

#### Observação
A entidade `Mochila` possui chaves estrangeiras referenciando as entidades `Treinador` e `Tipo_Item`.

| Nome Variável | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NOME_ITEM     | VARCHAR(60)  | Nome do item na mochila. | ASCII          | Não | PK, FK |                   |
| DONO          | int          | Identificador do treinador dono da mochila. | Numérico | Não | FK |                   |
| QUANTIDADE    | SMALLINT     | Quantidade do item na mochila. | Numérico  | Não |    |                   |

## Entidade: Pokedex

#### Descrição
Representa a Pokedex, um dispositivo eletrônico que fornece informações sobre as espécies de pokémons.

#### Observação
A entidade `Pokedex` possui chaves estrangeiras referenciando a entidade `Tipo` e restrições de verificação para garantir que os valores estejam dentro de intervalos válidos.

| Nome Variável   | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|-----------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NUMERO_POKEDEX  | int          | Número único na Pokedex para o pokémon. | Numérico | Não | PK |                   |
| NOME_POKEMON    | VARCHAR(20)  | Nome do pokémon.     | ASCII              | Sim |    | UNIQUE            |
| TIPO1           | VARCHAR(15)  | Tipo primário do pokémon. | ASCII         | Não | FK |                   |
| TIPO2           | VARCHAR(15)  | Tipo secundário do pokémon. | ASCII       | Sim | FK |                   |
| NIVEL_EVOLUCAO  | SMALLINT     | Nível de evolução do pokémon. | Numérico  | Sim |    |                   |
| TAXA_CAPTURA    | smallint     | Taxa de captura do pokémon. | 0-100       | Não |    | CHECK (taxa_captura >= 0 AND taxa_captura <= 100) |
| SOM_EMITIDO     | int          | Identificador do som emitido pelo pokémon. | Numérico | Não |    |                   |
| REGIAO          | VARCHAR(20)  | Região onde o pokémon é encontrado. | ASCII | Não |    |                   |
| INFO            | VARCHAR(100) | Informações adicionais sobre o pokémon. | ASCII | Não |    |                   |

## Entidade: Evolucao

#### Descrição
Representa a relação de evolução entre diferentes espécies de pokémons.

#### Observação
A entidade `Evolucao` possui chaves estrangeiras referenciando a entidade `Pokedex`.

| Nome Variável | Tipo | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|---------------|------|----------------------|--------------------|------------------------|----------|-------------------|
| ANTERIOR      | int  | Número na Pokedex do pokémon anterior na cadeia evolutiva. | Numérico | Não | PK, FK |                   |
| SUCESSOR      | int  | Número na Pokedex do pokémon sucessor na cadeia evolutiva. | Numérico | Não | FK | UNIQUE            |

## Entidade: Registro_Pokedex

#### Descrição
Registra quais pokémons foram capturados por um treinador.

#### Observação
A entidade `Registro_Pokedex` possui chaves estrangeiras referenciando as entidades `Pokedex` e `Treinador`.

| Nome Variável   | Tipo         | Descrição            | Valores permitidos | Permite valores nulos? | É chave? | Outras Restrições |
|-----------------|--------------|----------------------|--------------------|------------------------|----------|-------------------|
| NUMERO_POKEMON  | int          | Número do pokémon na Pokedex. | Numérico | Não | PK, FK |                   |
| TREINADOR_ID    | int          | Identificador do treinador. | Numérico   | Não | PK, FK |                   |
| CAPTURADO       | VARCHAR(5)   | Indica se o pokémon foi capturado. | 'SIM' ou 'NAO' | Não |    |                   |



## Histórico de versões

| Versão |    Data    | Descrição                                           | Autor                                          |
| :----: | :--------: | --------------------------                          | ---------------------------------------------- |
| `1.0`  | 01/10/2023 | Criação do DD                                       | [Felipe de Sousa](https://github.com/fsousac)  |
| `1.1`  | 01/10/2023 | Modularização do documento para um arquivo separado | [Felipe de Sousa](https://github.com/fsousac) |
| `1.2`  | 02/10/2023 | Adição de dados | [Murilo Perazzo](https://github.com/murilopbs) |
