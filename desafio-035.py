# Desafio: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não
# formar um trângulo.

comp1 = float(input('Comprimento da reta 1: '))
comp2 = float(input('Comprimento da reta 2: '))
comp3 = float(input('Comprimento da reta 3: '))

v1 = (comp2 - comp3) < comp1 < comp2 + comp3
v2 = (comp1 - comp3) < comp2 < comp1 + comp3
v3 = (comp1 - comp2) < comp3 < comp1 + comp2

if v1 and v2 and v3:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')