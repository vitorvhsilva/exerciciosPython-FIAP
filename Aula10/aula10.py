
def pegarMaior(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            return [a, b]
        else:
            return [a, c]

    if b >= a and b >= c:
        if a >= c:
            return [b, a]
        else:
            return [b, c]
        
    if c >= a and c >= b:
        if a >= b:
            return [c, a]
        else:
            return [c, b]

def notaFiap():
    cp1 = input('Digite a nota do CP1\n')

    while not cp1.isdigit or int(cp1) > 10 or int(cp1) < 0:
        cp1 = input('Formato inválido, digite a nota do CP1\n')

    cp2 = input('Digite a nota do CP2\n')

    while not cp2.isdigit or int(cp2) > 10 or int(cp2) < 0:
        cp2 = input('Formato inválido, digite a nota do CP2\n')


    cp3 = input('Digite a nota do CP3\n')

    while not cp3.isdigit or int(cp3) > 10 or int(cp3) < 0:
        cp3 = input('Formato inválido, digite a nota do CP3\n')

    listaCpPrimeiroSemestre = pegarMaior(int(cp1), int(cp2), int(cp3))

    ch1 = input('Digite a nota do Challenge 1\n')

    while not ch1.isdigit or int(ch1) > 10 or int(ch1) < 0:
        ch1 = input('Formato inválido, digite a nota do Challenge 1\n')

    ch2 = input('Digite a nota do Challenge 2\n')

    while not ch2.isdigit or int(ch2) > 10 or int(ch2) < 0:
        ch2 = input('Formato inválido, digite a nota do Challenge 2\n')

    gs1 = input('Digite a nota da Global Solution 1\n')

    while not gs1.isdigit or int(gs1) > 10 or int(gs1) < 0:
        gs1 = input('Formato inválido, digite a nota da Global Solution 1\n ')

    notaPrimeiroSemestre = ((int(listaCpPrimeiroSemestre[0]) * 0.10) + (int(listaCpPrimeiroSemestre[1]) * 0.10) +
                            (int(ch1) * 0.10) + (int(ch2) * 0.10) + (int(gs1) * 0.60)) 

    notaPrimeiroSemestre = int(notaPrimeiroSemestre)



    cp4 = input('Digite a nota do CP4\n')

    while not cp4.isdigit or int(cp4) > 10 or int(cp4) < 0:
        cp4 = input('Formato inválido, digite a nota do CP4\n')

    cp5 = input('Digite a nota do CP5\n')

    while not cp5.isdigit or int(cp5) > 10 or int(cp5) < 0:
        cp5 = input('Formato inválido, digite a nota do CP5\n')


    cp6 = input('Digite a nota do CP6\n')

    while not cp6.isdigit or int(cp6) > 10 or int(cp6) < 0:
        cp6 = input('Formato inválido, digite a nota do CP6\n')

    listaCpSegundoSemestre = pegarMaior(int(cp4), int(cp5), int(cp6))

    ch3 = input('Digite a nota do Challenge 3\n')

    while not ch3.isdigit or int(ch3) > 10 or int(ch3) < 0:
        ch3 = input('Formato inválido, digite a nota do Challenge 3\n')

    ch4 = input('Digite a nota do Challenge 4\n')

    while not ch4.isdigit or int(ch4) > 10 or int(ch4) < 0:
        ch4 = input('Formato inválido, digite a nota do Challenge 4\n')

    gs2 = input('Digite a nota da Global Solution 2\n')

    while not gs2.isdigit or int(gs2) > 10 or int(gs2) < 0:
        gs2 = input('Formato inválido, digite a nota da Global Solution 2\n ')

    notaSegundoSemestre = ((int(listaCpSegundoSemestre[0]) * 0.10) + (int(listaCpSegundoSemestre[1]) * 0.10) +
                            (int(ch3) * 0.10) + (int(ch4) * 0.10) + (int(gs2) * 0.60)) 

    notaSegundoSemestre = int(notaSegundoSemestre)

    notaFinal = (notaPrimeiroSemestre * 0.4) + (notaSegundoSemestre * 0.6)

    print(f'Sua nota final foi {notaFinal:.2f}')

notaFiap()