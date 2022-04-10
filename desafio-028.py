# Desafio: Escreva um programa que faça
# o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi
# o número escolhido pelo computador.

# O programa deverá escrever na tela se o
# usuário venceu ou perdeu

from random import randint

numRand = randint(0,5)
numInput = int(input('Escolha um número de 1 a 5: '))

if numInput != numRand:
    print('Perdeu!! número era {}'.format(numRand))
else:
    print('Venceu!!')
