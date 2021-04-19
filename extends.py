from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo='Tutorial en flask'
    name = 'Eduardo'
    return render_template('index.html',name=name, title=titulo)

@app.route('/client')
def client():
    list_name = ['Test1', 'Test2', 'Test3']
    return render_template('client.html', list=list_name)

if __name__ == '__main__':
    app.run(port=8080,debug=True)