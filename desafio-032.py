# Desafio: Faça um programa que leia um ano
# qualquer e mostre se ele é BISSEXTO

from calendar import isleap

ano = int(input('Qual é o ano? '))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')