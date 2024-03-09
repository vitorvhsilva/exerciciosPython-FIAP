"""
Nome
Idade
Peso
Altura
Usuário Python
Endereço
PCD (Pessoa com Deficiencia)
Data de Nascimento
"""

import math

nome = str('Vitor Hugo da Silva')  # string
idade = int(17)  # integer
altura = float(1.70)  # float/double
peso = float(68.5)  # float/double
usuarioPython = bool(True)  # boolean
endereco = str("Rua Lugar Nenhum, n100")  # string
pcd = bool(False)  # boolean
dataNasc = str("28/03/2006")  # string
dia = int(28)  # integer
mes = int(3)  # integer
ano = int(2006)  # integer

'''

print(f'Variável nome, valor = {nome}, tipo = {type(nome)}')
print(f'Variável idade, valor = {idade}, tipo = {type(idade)}')
print(f'Variável altura, valor = {altura}, tipo = {type(altura)}')
print(f'Variável peso, valor = {peso}, tipo = {type(peso)}')
print(f'Variável usuarioPython, valor = {usuarioPython}, tipo = {type(usuarioPython)}')
print(f'Variável endereco, valor = {endereco}, tipo = {type(endereco)}')
print(f'Variável pcd, valor = {pcd}, tipo = {type(pcd)}')
print(f'Variável dia, mes e ano, valor respectivo = {dia}/{mes}/{ano}, tipo = {type(nome)}')

'''

print(endereco[-3:])

print(endereco.split(','))

print(100 / 7)
print(100 // 7)

print(10 ** 2) #exponencial

print(math.sqrt(4))

print(((2 + 3) * 5) - (2 ** 2))

print('5' * 10)

print('5' + '2')
