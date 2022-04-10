# Desafio: Escreva um programa que pergunte o salário
# de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um
# aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Entre com o salário: '))

if salario > 1.250:
    print('O salário com o aumento é R${:.2f}'.format(salario + (salario * 0.10)))
else:
    print('O salário com o aumento é R${:.2f}'.format(salario + (salario * 0.15)))