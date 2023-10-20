# Normalização 

A normalização de bancos de dados é um processo de organização de dados em tabelas de forma a evitar anomalias de dados, como redundância de dados, inconsistência de dados e anomalias de inserção, atualização e exclusão.

Existem cinco formas normais de normalização, cada uma com seus próprios requisitos e benefícios.

## **Primeira forma normal (1NF)**

A primeira forma normal (1NF) é o nível mais básico de normalização. Uma tabela está na 1NF se atender aos seguintes requisitos:

* Não deve conter grupos repetidos.
* Deve ter todas as colunas atômicas.

Uma coluna atômica é uma coluna que não pode ser dividida em partes menores. Por exemplo, a coluna "Nome" não é atômica, pois pode ser dividida em primeiro nome, sobrenome e outros nomes.

Para o nosso projeto aplicamos em:

## **Segunda forma normal (2NF)**

Uma tabela está na segunda forma normal (2NF) se atender aos seguintes requisitos:

* Está na 1NF.
* Todas as colunas não chave são completamente dependentes da chave primária.

Uma coluna não chave é uma coluna que não é parte da chave primária.

Para o nosso projeto aplicamos em:

A dependência total ocorre quando o valor de uma coluna não chave não pode ser determinado sem o valor da chave primária.

## **Terceira forma normal (3NF)**

Uma tabela está na terceira forma normal (3NF) se atender aos seguintes requisitos:

* Está na 2NF.
* Não tem dependências transitivas.

Uma dependência transitiva ocorre quando o valor de uma coluna não chave depende do valor de outra coluna não chave.

Para o nosso projeto aplicamos em:

## **Forma normal de Boyce-Codd (BCNF)**

A forma normal de Boyce-Codd (BCNF) é uma extensão da 3NF. Uma tabela está na BCNF se atender aos seguintes requisitos:

* Está na 3NF.
* Não tem dependências funcionais multivaloradas.

Uma dependência funcional multivalorada ocorre quando o valor de uma coluna não chave depende do valor de outra coluna não chave, mas pode ter vários valores possíveis.

Para o nosso projeto aplicamos em:

## **Quarta forma normal (4NF)**

A quarta forma normal (4NF) é uma forma de normalização avançada que não é frequentemente usada. Uma tabela está na 4NF se atender aos seguintes requisitos:

* Está na 3NF.
* Não tem dependências funcionais desnecessárias.

Uma dependência funcional desnecessária ocorre quando o valor de uma coluna não chave pode ser determinado sem o valor de outra coluna não chave.

Para o nosso projeto aplicamos em:

## Histórico de versões

| Versão |    Data    | Descrição                             | Autor                                          |
| :----: | :--------: | ------------------------------------- | ---------------------------------------------- |
| `1.0`  | 20/10/2023 | Criação do Documento                  | [Felipe de Sousa](https://github.com/fsousac)  |

