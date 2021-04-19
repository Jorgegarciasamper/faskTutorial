from flask import Flask
from flask import render_template

import forms

app = Flask(__name__)

@app.route('/')
def index():
    titulo='Tutorial en flask'
    comment_form = forms.CommentFrom()
    name = 'Eduardo'
    return render_template('index.html',name=name, title=titulo, form = comment_form)

if __name__ == '__main__':
    app.run(port=8080,debug=True)