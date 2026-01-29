from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=100, max=1000, message='Ingrese un valor valido')
    ])
    nombre= StringField("Nombre", [
        validators.DataRequired(message='Campo requerido'),
        validators.length(min=3, max=10, message=" El campo es requerido")
        ])
    apaterno=StringField("Apaterno", [
        validators.DataRequired(message='Campo requerido'),
        validators.length(min=3, max=10, message=" El campo es requerido")
                                     ])
    amaterno=StringField("Amaterno",
                         [validators.DataRequired(message='Campo requerido'),
                          validators.length(min=3, max=10, message=" El campo es requerido")
                          ])
    correo=EmailField("Correo",[validators.DataRequired(message='Campo requerido'),
                                validators.email( message="email no valido")
                                ])