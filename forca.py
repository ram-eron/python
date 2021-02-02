
letras_utilizadas = ''
letras_corretas = ''
qtd = 0
x=0
underline = []

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

    palavra_secreta = 'Python'.upper()

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

        if(erros >= 5):
            print('Você perdeu, a palavra era', palavra_secreta)
            break
        elif(len(palavra_secreta) == qtd_correta ):
            print('Acertou miserável, a palavra era', palavra_secreta)
            break

        print('Acertos = ', str(qtd_correta), ';Erros = ', str(erros))

if(__name__ == "__main__"):
    jogar()