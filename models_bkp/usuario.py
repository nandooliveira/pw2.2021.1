from .database import Database


class Usuario():
    def __init__(self, id, nome, email, senha, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

    @classmethod
    def find_by_id(cls, user_id):
        row = Database.execute("SELECT * FROM usuarios WHERE id = %s", user_id).fetchone()

        return cls.__user_from_database_record(row)

    @classmethod
    def list_users(cls):
        rows = Database.execute("SELECT * FROM usuarios").fetchall()

        # usuarios = []
        #
        # for row in rows:
        #     usuarios.append(cls.__user_from_database_record(row))

        # usuarios = list(map(cls.__user_from_database_record, rows))

        usuarios = [cls.__user_from_database_record(row) for row in rows]

        return usuarios

    @classmethod
    def create(cls, nome, email, senha, telefone):
        Database.execute("INSERT INTO usuarios (nome, email, senha, telefone, criacao, atualizacao) VALUES (%s, %s, %s, %s, now(), now())",
                         nome, email, senha, telefone,
                         commit=True
                         )

    @classmethod
    def __user_from_database_record(cls, row):
        return Usuario(row[0], row[1], row[2], row[3], row[4])
