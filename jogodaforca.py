import random

# vetores
palavras = random.choice(['GATO', 'CACHORRO', 'ELEFANTE', 'LEAO', 'TIGRE', 'GIRAFA', 'MACACO', 'LOBO', 'ZEBRA', 'RINOCERONTE', 'HIPOPOTAMO', 'CAMALEAO', 'CANGURU', 'PANDA', 'CROCODILO'])
palavra_secreta = [i for i in palavras]

tentativas = len(palavra_secreta) * 2
forca = ['_'] * len(palavra_secreta)

# jogo
while forca != palavra_secreta and tentativas != 0:

    print(f'Tentativas restantes: {tentativas}')
    print('Palavra: ', *forca, sep='')

    entrada = input('Digite uma letra: ')

    for i in range(len(palavra_secreta)):
        if entrada == palavra_secreta[i]:
            forca[i] = palavra_secreta[i]
    if entrada not in palavra_secreta:
        print('A letra digitada não existe!')

    tentativas -= 1


# fim de jogo
if tentativas != 0:
    print('Palavra: ', *forca, sep='')
    print('Parabéns! Você encontrou a palavra secreta')
else:
    print('GAME OVER: Suas tentativas acabaram!')