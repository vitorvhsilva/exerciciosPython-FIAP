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
        
    mult = 11
    calculo = 0

    for i in cpf[:10]:
        calculo += int(i) * mult
        mult -= 1

    if calculo % 11 >= 2:
        k = (11 - (calculo % 11))

    if cpf[9] == str(j) and cpf[10] == str(k):
        print('CPF Válido! ')
    else: 
        print('CPF inválido! ')
        

validaCPF('52439200882')
