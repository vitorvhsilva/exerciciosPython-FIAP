import random

# cpf = '' 
# calculo = 0
# j = ''
# k = ''

# while len(cpf) <= 9:
#     cpf += str(random.randint(0, 9))

# for i in cpf:
#     mult = 10
#     calculo += int(i) * mult
#     mult -= 1

# if calculo % 11 == 0 or calculo % 11 == 1: 
#     j = 0
# elif calculo % 11 >= 2:
#     j = (11 - (calculo % 11))

# cpf += str(j)

# calculo = 0

# for k in cpf:
#     mult = 11
#     calculo += int(k) * mult
#     mult -= 1

# if calculo % 11 == 0 or calculo % 11 == 1: 
#     k = 0
# elif calculo % 11 >= 2:
#     k = (11 - (calculo % 11))

# cpf += str(k)

# print(cpf)

def validaCPF(cpf):
    calculo = 0

    j = 0

    mult = 10

    for i in cpf[:9]:
        calculo += int(i) * mult
        mult -= 1

    print(calculo)

    # if calculo % 11 == 0 or calculo % 11 == 1: 
    #     j = 0
    # elif calculo % 11 >= 2:
    #     j = (11 - (calculo % 11))

    # print(j)

    # if cpf[9] == str(j):
    #     print('boa')

validaCPF('52439200883')
