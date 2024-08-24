loop = True

class NomeInvalido(Exception):
    pass

class CpfInvalido(Exception):
    pass

class CepInvalido(Exception):
    pass

class MelhorLinguagemInvalida(Exception):
    pass

class PythonPiorQueJava(Exception):
    pass

def validarNome(nome: str):
    if len(nome) < 3 or not nome.isalpha():
        raise NomeInvalido()
    
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

    if cpf[9] != str(j) or cpf[10] != str(k) or len(cpf) != 11:
        raise CpfInvalido()

def validaCEP(cep):
    if len(cep) != 8 or cep[0] != "0":
        raise CepInvalido()

def validarLinguagem(linguagem: str):
    if linguagem.lower() == "python" or linguagem.lower() == "py":
        raise PythonPiorQueJava()
    if linguagem.lower() != "java":
        raise MelhorLinguagemInvalida()

while loop:
    try:
        nome = input('Olá, qual é seu nome? ')
        validarNome(nome)
        loop = False
    except NomeInvalido as e:
        print('Nome inválido! Insira seu nome novamente')

loop = True

while loop: 
    try: 
        idade = input('Qual sua idade? ')
        int(idade)
        loop = False
    except ValueError as e:
        print('Idade inválida! Insira sua idade novamente')

loop = True

while loop: 
    try: 
        cpf = input('Qual seu CPF? ')
        validaCPF(cpf)
        loop = False
    except CpfInvalido as e:
        print('CPF inválido! Insira seu CPF novamente')
    except IndexError as e:
        print('CPF inválido! Insira seu CPF novamente')

loop = True

while loop: 
    try: 
        cep = input('Qual seu CEP? ')
        validaCEP(cep)
        loop = False
    except CepInvalido as e:
        print('CEP inválido! Insira seu CEP novamente')

loop = True

while loop: 
    try: 
        linguagem = input('Qual a melhor linguagem de programação? ')
        validarLinguagem(linguagem)
        loop = False
    except MelhorLinguagemInvalida as e:
        print('Professor, professor. . . Você sabe a resposta')
    except PythonPiorQueJava as e:
        print('Vou deixar passar dessa vez 😡')
        loop = False
