# Desafio: Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa.

from math import hypot

cop = float(input('Qual é o valor do cateto oposto? '))
caj = float(input('Qual é o valor do cateto adjacente? '))

print('O Valor da hipotenusa é {}'.format(hypot(cop, caj)))
