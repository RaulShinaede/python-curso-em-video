# Desafio: Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor

num1 = int(input('Entre com o primeiro número: '))
num2 = int(input('Entre com o segundo número: '))

if num1 > num2:
    print('O maior número é {} e o menor é {}'.format(num1, num2))
else:
    print('O maior número é {} e o menor é {}'.format(num2, num1))
