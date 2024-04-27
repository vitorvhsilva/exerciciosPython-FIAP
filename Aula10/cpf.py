import random

def validaCPF(cpf):
    calculo = 0

    j = 0
    k = 0

    mult = 10

    for i in cpf[:9]:
        calculo += int(i) * mult
        mult -= 1

    if calculo % 11 >= 2:
        j = (11 - (calculo % 11))
    else:
        j = 0
        
    mult = 11
    calculo = 0

    for i in cpf[:10]:
        calculo += int(i) * mult
        mult -= 1

    if calculo % 11 >= 2:
        k = (11 - (calculo % 11))
    else:
        k = 0

    if cpf[9] == str(j) and cpf[10] == str(k):
        return True
    else: 
        return False


def criaCPF():
    cpf = ''

    while len(cpf) < 9:
        cpf += str(random.randint(0,9))

    calculo = 0

    j = 0
    k = 0

    mult = 10

    for i in cpf[:9]:
        calculo += int(i) * mult
        mult -= 1

    if calculo % 11 >= 2:
        j = (11 - (calculo % 11))
    else:
        j = 0

    cpf += str(j)

    mult = 11
    calculo = 0

    for i in cpf[:10]:
        calculo += int(i) * mult
        mult -= 1

    if calculo % 11 >= 2:
        k = (11 - (calculo % 11))
    else:
        k = 0

    cpf += str(k)

    return cpf

def identificar_estado(cpf):
    estado = cpf[8]
    estado = int(estado)

    if estado == 1:
        return 'DF, GO, MS, MT ou TO'
    elif estado == 2:
        return 'AC, AM, AP, PA, RO ou RR'
    elif estado == 3:
        return 'CE, MA, ou PI'
    elif estado == 4:
        return 'AL, PB, PE, RN'
    elif estado == 5:
        return 'BA e SE'
    elif estado == 6:
        return 'MG'
    elif estado == 7:
        return 'ES e RJ'
    elif estado == 8:
        return 'SP'
    elif estado == 9:
        return 'PR e SC'
    elif estado == 0:
        return 'RS'
    
print(identificar_estado(criaCPF()))
