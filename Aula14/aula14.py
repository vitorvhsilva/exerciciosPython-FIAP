import json

with open('posicional.txt', encoding='utf-8') as file:
    lista = file.readlines()

lista.pop(0)
lista.pop(0)

def limpar_dado(dado: str):
    return dado.strip()

def fazer_dic(lista):
    lista_dic = []

    for linha in lista:
        nome = limpar_dado(linha[:31]) # nome
        sobrenome = limpar_dado(linha[31:62]) # sobrenome
        idade = limpar_dado(linha[62:69]) # idade
        cidade = limpar_dado(linha[69:89]) # cidade
        estado = limpar_dado(linha[89:96]) # estado
        cep = linha[96:104] # cep
        dic = {
                'nome': nome,
                'sobrenome': sobrenome,
                'idade': idade,
                'cidade': cidade,
                'estado': estado,
                'cep': cep 
            }
        lista_dic.append(dic)
    
    return lista_dic



lista_dic = fazer_dic(lista)

with open('teste.json', mode='w') as file:
    json.dump(lista_dic, file, indent=4, ensure_ascii=False)

# print(lista[2][:31]) # nome
# print(lista[2][31:62]) # sobrenome
# print(lista[2][62:69]) # idade
# print(lista[2][69:89]) # cidade
# print(lista[2][89:96]) # estado
# print(lista[2][96:104]) # cep
