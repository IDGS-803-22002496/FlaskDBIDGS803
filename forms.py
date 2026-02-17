from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    matricula=IntegerField('id', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.NumberRange(min=2, max=100, message='Ingrese valor valido')
    ])
    nombre=StringField('nombre', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.NumberRange(min=4, max=10, message='Ingrese nombre valido')
    ])
    apaterno=StringField('apaterno', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.NumberRange(min=2, max=100, message='Ingrese valor valido')
    ])
    email=EmailField('correo', [
        validators.DataRequired(message= 'El campo es requerido'),
        validators.NumberRange(min=2, max=100, message='Ingrese valor valido')
    ])