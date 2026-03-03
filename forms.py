from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    nombre=StringField('nombre', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.Length(min=4, max=50, message='Ingrese nombre valido')
    ])
    apellidos=StringField('apellidos', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.Length(min=2, max=50, message='Ingrese valor valido')
    ])
    numero=StringField('numero', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.Length(min=1, max=20, message='Ingrese un numero valido')
    ])
    email=EmailField('correo', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
