#  Desafio: Faça um programa que leia um
# ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians, degrees

ang  = float(input('Ângulo: '))
sen  = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('Seno: {0:.2f}, Cosseno: {1:.2f}, Tangente: {2:.2f}'.format(sen, coss, tang))
