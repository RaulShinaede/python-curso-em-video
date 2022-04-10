# Desafio: Crie um programa que leia um número Real
# qualquer pelo teclado e mostre na tela a sua porção
# inteira.

from math import trunc

numero = float(input('Número: '))

print('A porção inteira de {0} é {1}'.format(numero, trunc(numero)))
