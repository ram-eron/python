import random

letras_utilizadas = ''
letras_corretas = ''
qtd = 0
x=0
underline = []

def gera_palavra():
    palavras = {1: [], 2: [], 3: []}

    with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if (len(linha) <= 5):
                palavras[1].append(linha)
            elif (len(linha) > 5 and len(linha) < 10):
                palavras[2].append(linha)
            else:
                palavras[3].append(linha)

    nivel = int(input('Escolha um nível: 1-Fácil, 2-Médio, 3-Difícil -> '))

    posicao = 0

    if (nivel == 1):
        posicao = random.randrange(0, len(palavras.get(1)))
        palavra_secreta = palavras.get(1)[posicao]
    elif (nivel == 2):
        posicao = random.randrange(0, len(palavras.get(2)))
        palavra_secreta = palavras.get(2)[posicao]
    else:
        posicao = random.randrange(0, len(palavras.get(3)))
        palavra_secreta = palavras.get(3)[posicao]

    return palavra_secreta.upper()

def utilizadas(chute):
    for letra in list(letras_utilizadas):
        if letra == chute:
            return bool(letra)
    return False

def monta_lista(chute, palavra_secreta):
    global x
    for letra in palavra_secreta:
        if letra == chute:
            underline[x] = letra
        x+=1
    x=0

def corretas(chute):
   for letra in list(letras_corretas):
        if letra == chute:
            return bool(letra)
   return False

def valida_letra(chute, palavra_secreta):
    '''funcao para validar letra e retornar a qtd de letras na string'''
    qtd = 0
    for letra in list(palavra_secreta):
        if letra==chute and not corretas(chute):
            qtd += 1
    return qtd

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = gera_palavra()

    for x in palavra_secreta:
        underline.append('_ ')

    global letras_corretas
    global letras_utilizadas
    jogando = True
    qtd_correta = 0
    erros = 0

    print('Palavra secreta contém ' + str(len(palavra_secreta)) + ' letras: ' + ' '.join(underline))

    while(jogando):
        chute = input('Informe uma letra: ').upper()

        if valida_letra(chute,palavra_secreta) > 0:
            qtd_correta += valida_letra(chute,palavra_secreta)
            letras_corretas += chute
            letras_utilizadas += chute
            monta_lista(chute,palavra_secreta)
        else:
            erros += 1

        print(' '.join(underline))

        if(erros >= len(palavra_secreta)+5):
            print('Você perdeu, a palavra era', palavra_secreta)
            break
        elif(len(palavra_secreta) == qtd_correta ):
            print('Acertou miserável, a palavra era', palavra_secreta)
            break

        print('Acertos = ', str(qtd_correta), ';Erros = ', str(erros))

if(__name__ == "__main__"):
    jogar()