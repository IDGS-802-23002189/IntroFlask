from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms import validators

class CinepolisForm(FlaskForm):

    nombre = StringField("Nombre", [
        validators.DataRequired(message="Campo requerido"),
        validators.Length(min=3, max=30)
    ])

    cantidad_compradores = IntegerField("Cantidad de compradores", [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(min=1, message="Debe ser mayor a 0")
    ])

    tarjetaCineco = RadioField(
        "¿Tiene tarjeta Cineco?",
        choices=[("si", "Sí"), ("no", "No")],
        validators=[validators.DataRequired(message="Campo requerido")]
    )

    cantidad_boletos = IntegerField("Cantidad de boletos", [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(min=1, message="Debe ser mayor a 0")
    ])
