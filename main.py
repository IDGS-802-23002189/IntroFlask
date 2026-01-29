import math
from flask import Flask, render_template, request, redirect
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)
app.secret_key='Clave secreta'
csrf=CSRFProtect()

@app.route("/")
def index():
    titulo="IDGS-802-FLASK"
    lista=['Juan','karla']
    return render_template("index.html",titulo=titulo,lista=lista)


@app.route("/usuarios", methods =["GET","POST"])
def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    usuarios_class=forms.UserForm(request.form)
    if request.method=='POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data

        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
        
    
    return render_template("usuarios.html",
                           form=usuarios_class, 
                           mat = mat,
                           nom=nom,
                           apa=apa,
                           ama=ama,
                           email=email
                           )

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

    
@app.route("/operasBas", methods=["GET", "POST"])
def opera1():
    n1 = 0
    n2 = 0
    res = 0

    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
    return render_template(
        "operasBas.html",
        n1=n1,
        n2=n2,
        res=res
    )


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


@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")


@app.route("/cinepolis", methods=["GET", "POST"])
def cine():

    total = 0
    mensaje = ""
    costo_boleto = 12

    nombre = ""
    cantidad_boletos = ""
    cantidad_compradores = ""
    tarjetaCineco = "no"

    if request.method == "POST":

        accion = request.form.get("accion")

        if accion == "salir":
            return redirect("/cinepolis")

        if accion == "procesar":

            nombre = request.form.get("nombre")
            cantidad_boletos = int(request.form.get("cantidad_boletos", 0))
            cantidad_compradores = int(request.form.get("cantidad_compradores", 0))
            tarjetaCineco = request.form.get("tarjetaCineco")

            max_boletos = cantidad_compradores * 7

            if cantidad_boletos > max_boletos:
                mensaje = f"Solo se permiten {max_boletos} boletos para {cantidad_compradores} personas"
            else:
                subtotal = cantidad_boletos * costo_boleto
                descuento = 0

                if cantidad_boletos > 5:
                    descuento = subtotal * 0.15
                elif cantidad_boletos >= 3:
                    descuento = subtotal * 0.10

                total = subtotal - descuento

                if tarjetaCineco == "si":
                    total -= total * 0.10

                mensaje = "Compra realizada correctamente."

    return render_template(
        "cinepolisFlask.html",
        total=total,
        mensaje=mensaje,
        nombre=nombre,
        cantidad_boletos=cantidad_boletos,
        cantidad_compradores=cantidad_compradores,
        tarjetaCineco=tarjetaCineco
    )


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)
