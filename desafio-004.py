# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

item = input('Digite algo: ')
print('Tipo da variável:', type(item))
print('É um número?', item.isnumeric())
print('É uma letra do alfabeto?', item.isalpha())
print('Só tem espaços?', item.isspace())
print('É alfanumérico?', item.isalnum())