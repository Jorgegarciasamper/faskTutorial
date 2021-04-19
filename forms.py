from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

class CommentFrom(Form):
    username = StringField('username')
    email = EmailField('Correo electronico')
    comment = TextField('Comentario')