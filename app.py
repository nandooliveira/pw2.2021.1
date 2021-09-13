from flask import Flask, request, render_template

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


@app.route("/soma/<int:a>/<int:b>", methods=["GET", "POST"])
def soma(a, b):
    if request.method == "GET":
        return f"GET a + b = {a + b}"
    else:
        return f"POST a + b = {a + b}"

@app.route("/perfil")
def perfil():
    # Verificar qual o usuário está autenticado
    # Buscar os dados do usuário no banco de dados
    usuario = {
        "nome": "Zé de Nanan",
        "email": "tonho@da.lua"
    }
    # Passar esses dados para o template de Perfil
    return render_template(
        "perfil.html",
        nome = "Fernando",
        email = "fernando.oliveira@hey.com",
        numero = 1,
        alunos = ["Pablo", "Adonis", "Claudio", "Tayane", "Rebbecca"]
    )

# METHODS - GET POST
# www.exemplo.com?usuario=fernando&senha=123mudar
