# Banco de Dados

## Criação do Banco

```sql
CREATE DATABASE pweb;
```

## Criação da Tabela de Usuários

```sql
CREATE TABLE usuarios (
    id serial primary key,
    nome varchar(100) not null,
    email varchar(100) not null,
    senha varchar not null,
    telefone varchar,
    criacao timestamp,
    atualizacao timestamp
);
```