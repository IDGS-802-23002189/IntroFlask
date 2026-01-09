from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    titulo="IDGS-802-FLASK"
    lista=['Juan','karla']
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/formularios")
def formularios():
    return render_template("formularios.html")

@app.route("/reportes")
def reportes():
    return render_template("reportes.html")

@app.route("/hola")
def hola():
    return "Hola hola"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"Numero: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"ID: {id} nombre: {username}"

@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1, n2):
    return f"suma: {n1 + n2}"

@app.route("/default")
@app.route("/default/<string:param>")
def func2(param="Juan"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas")
def operas():
    return '''
    <form>
        <label for="name">Nombre:</label>
        <input type="text" id="name" required>

        <label for="apaterno">Apellido paterno:</label>
        <input type="text" id="apaterno" required>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
