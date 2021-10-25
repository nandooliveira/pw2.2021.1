from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    telefone = db.Column(db.String)

    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
