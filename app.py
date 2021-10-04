from flask import Flask, request, render_template
import psycopg2

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
    connection = psycopg2.connect(
        host = 'localhost',
        database = 'pweb',
        user = 'postgres',
        password = 'postgres'
    )

    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM usuarios WHERE id = {id}")
    usuario = cursor.fetchall()[0]

    # Passar esses dados para o template de Perfil
    return render_template(
        "perfil.html",
        nome = usuario[1],
        email = usuario[2],
        numero = usuario[0],
        alunos = ["Pablo", "Adonis", "Claudio", "Tayane", "Rebbecca"]
    )

# METHODS - GET POST
# www.exemplo.com?usuario=fernando&senha=123mudar
# PostgreSQL - SGBD