from flask import Flask, render_template, request

app = Flask(__name__)


def calculator(num1:int, num2:int, op:str):
    if op == '+':
        return str(num1 + num2)
    elif op == '-':
        return str(num1 - num2)
    elif op == '*':
        return str(num1 * num2)
    elif op == '/':
        if num2 == 0:
            return 'Divisão por zero!'
        else:
            return str(num1/num2)
    else:
        return 'Operação Inviável de ser realizada!'
# Página Principal
@app.route('/')
def index():
    return render_template('home.html')

@app.post('/result')
def equal():
    number1 = int(request.form['FN'])
    number2 = int(request.form['SN'])
    operador = request.form['OP']

    resultado = calculator(number1, number2, operador)
    print(resultado)
    return render_template('result.html', resultado = resultado)



app.run(host='0.0.0.0', port=81, debug=True)
