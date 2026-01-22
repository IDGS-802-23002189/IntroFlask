from flask import Flask, render_template, request


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

    
@app.route("/operasBas")
def opera1():
    return render_template("operasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    operacion = request.form.get("operacion")

    if operacion == "sumar":
        resultado = n1 + n2
        texto = "La suma es"
    elif operacion == "restar":
        resultado = n1 - n2
        texto = "La resta es"
    elif operacion == "multiplicar":
        resultado = n1 * n2
        texto = "La multiplicación es"
    elif operacion == "dividir":
        if n2 == 0:
            return "Error: no se puede dividir entre cero"
        resultado = n1 / n2
        texto = "La división es"
    else:
        return "Operación no válida"

    return f"{texto}: {resultado}"



if __name__ == "__main__":
    app.run(debug=True)
