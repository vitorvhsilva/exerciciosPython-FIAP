lista = [0,1,2,3,4,5,6,7,8,9,10]
lista_2 = ['a','b','c','d','e','f','g']

#percorrer itens
'''
for item in lista[2:]:
  print(item)

print('\nFim 1\n')
'''
#pegar indice
'''
for i in range(7):
  print(f'{i + 1}: {lista_2[i]}')

print('\nFim 2\n')
'''
'''
print(list(range(5, 100, 5)))

x = 0 

while x < 10:
  print(x)
  x += 1

'''
'''
lista_while = [1,2,3,4,5]

while len(lista_while):
  valor = lista_while.pop(0)
  print(f'{valor} : {len(lista_while)}')

print('O valor da variavel e {a}, {b}'.format(a=50,b=100))

import random
'''
'''

temperatura = 0

while True:
  print(temperatura)
  if temperatura > 0: #
    break
  else:
    temperatura = random.randint(-10,10)

'''

lista_for = [1,2,3,4,5,6,7]

for item in lista_for:

  print(f'Numero: {item}')

  if item % 3 == 0: #se for verdadeiro (par), executa o continue (ignora oq ta dentro do for) 
    break

  print(item ** 2 + 3 * item / 255)
  print('======================================')

'''

print([item ** 2 for item in lista_for]) #mudando os valores da lista

lista_strings = ['pre_abc', 'pre_def', 'pre_ghi', 'pre_jkl', 'pre_mno']

print([palavra[4:] for palavra in lista_strings])

'''