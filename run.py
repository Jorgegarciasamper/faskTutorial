from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def helloWold():
    return '<h1>Hola Mundo!!</h1>'


@app.route('/params1')
def param1():
    param = request.args.get('param1', 'no contiene')
    param1 = request.args.get('param2', 'no contiene')
    return 'El parametro es :{}, {}'.format(param,param1)

@app.route('/params')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def param(name = 'Valor defecto', num='ninguno'):
    return 'El parametro es :{} {}'.format(name,num)


if __name__ == '__main__':
    app.run(port=8080,debug=True)




