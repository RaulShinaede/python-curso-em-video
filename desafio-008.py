# Desafio: Escreva um programa que leia um valor em metros
# e o exiba convertido em centimetros e milimetros

valor = int(input('Digite o valor em metro para conversão: '))

print('Centimetro: {0}, Milimetro: {1}'.format(valor * 100, valor * 1000))