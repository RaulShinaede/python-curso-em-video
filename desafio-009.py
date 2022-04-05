# Desafio: Faça um programa que leia um número
# inteiro qualquer e mostre na tela sua tabuada

num = int(input('Digite um número: '))

for i in range(1, 11):
    print('{0} x {1} = {2}'.format(num, i, num * i))
