from flask import Flask, request, redirect, render_template

from models.usuario import Usuario

app = Flask(__name__)


# www.uncisal.edu.br
#     - /users
#     - /login
#     - /cursos

# uncisal.edu.br
@app.route("/")
def hello_world():
    return "<p>Hello World!!</p>"


# uncisal.edu.br/saudacao/tonho
@app.route("/saudacao/<nome>")
def saudacao(nome):
    return f"<p>Seja Bem Vindo {nome}</p>"


@app.route("/soma/<int:a>/<int:b>", methods=['GET', 'POST'])
def soma(a, b):
    if request.method == "GET":
        return f"GET a + b = {a + b}"
    else:
        return f"POST a + b = {a + b}"


@app.route("/perfil/<int:id>")
def perfil(id):
    usuario = Usuario.find_by_id(id)

    # Passar esses dados para o template de Perfil
    return render_template(
        "perfil.html",
        nome=usuario.nome,
        email=usuario.email,
        numero=usuario.id,
        alunos=["Pablo", "Adonis", "Claudio", "Tayane", "Rebbecca"]
    )


@app.route("/usuarios", methods=['POST'])
def criar_usuario():
    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    senha = request.form["senha"]

    Usuario.create(nome, email, senha, telefone)

    return redirect("/perfil/1")


# [C]rud    -> POST /recursos
# [R]ead    -> GET  /recursos
# [U]pdate  -> POST /recursos/{id}
# [D]delete -> DELETE /recursos/{id}

# def change_password(id, senha):
#     usuario = find_user_by_id(id)

# METHODS - GET POST
# www.exemplo.com?usuario=fernando&senha=123mudar
# PostgreSQL - SGBD
