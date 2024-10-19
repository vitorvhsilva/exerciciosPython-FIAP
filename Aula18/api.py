from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['POST'])
def soma():
    num1 = request.form['num1']
    num2 = request.form['num2']
    oper = request.form['oper']

    num1 = int(num1)
    num2 = int(num2)

    resultado = 0

    if oper == 'soma':
        resultado = soma(num1, num2)
    if oper == 'sub':
        resultado = sub(num1, num2)
    if oper == 'mult':
        resultado = mult(num1, num2)
    if oper == 'div':
        resultado = div(num1, num2)

    return str(resultado)

@app.route('/', methods=['GET'])
def cards():
    qtd = request.args.get('qtd')
    response_shuffle = requests.get(f'https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count={qtd}')
    dict_deck = response_shuffle.json()
    return dict_deck

def soma(num1:int, num2: int):
    return num1 + num2

def sub(num1:int, num2: int):
    return num1 - num2

def mult(num1:int, num2: int):
    return num1 * num2

def div(num1:int, num2: int):
    return num1 / num2

if __name__ == '__main__':
    app.run(debug=True)