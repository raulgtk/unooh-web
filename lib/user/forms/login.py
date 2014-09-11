# coding: utf-8

from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms.validators import Required
from wtforms.validators import Email

class LoginForm(Form):

    email = StringField(u'Email', [
        Required(u"El email es obligatorio"),
        Email(u"El email no es correcto")])
    password = PasswordField(u'Contraseña', [
        Required(u"La contraseña es obligatoria"),])
    next = HiddenField()