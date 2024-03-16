lista = [1, 2 ,3]

lista_2 = [1, 'a', 3.14]

## Pode se mudar um valor de uma lista assim
lista_2[-1] = 3

## adiciona item na lista
lista_2.append(True)

## remove um item da lista

lista_2.pop(0)

print(lista_2, len(lista_2))

## verifica se a lista esta vazia ou nao
bool([])
## bool([]) mesma coisa que lista

print('\n')

##tupla

tupla = (1, 'a', 3.14)

copo_1 = 'cafe'
copo_2 = 'agua'

copo_1, copo_2 = copo_2, copo_1

print(copo_1, copo_2)

print('\n')

##conjuntos

conjuntos = {112, 22, 344, 442, 54, 54}
conjuntos_2 = {112, 1, 3, 22}

print(conjuntos.intersection(conjuntos_2))
print(conjuntos.difference(conjuntos_2))

print('\n')

dicionario = {'a': 100, 'b': 200, 'c': 300, 'd': 400 }



len(dicionario)

print(dicionario.items())
print(dicionario.keys())
print(dicionario.values())

if 'a' in dicionario:
    print('OK')

print(dicionario.get('z', 0))
print(dicionario.get('a', 0))

base_1 = {
    'nome': ['João', 'José', 'Maria'],
    'idade': [30, 24, 34],
    'estado_civil': ['casado', 'casado', 'solteiro']
}

base_2 = [
    {'nome': 'João', 'idade':30, 'estado_civil': 'casado'},
    {'nome': 'José', 'idade':24, 'estado_civil': 'casado'},
    {'nome': 'Maria', 'idade':34, 'estado_civil': 'solteiro'}
]

print(base_1['idade'])
