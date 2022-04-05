# Desafio: Escreva um programa que pergunte a quantidade de Km
# percorrido por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
# carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Dias de uso: '))
km = float(input('Km rodado: '))

vpd = dias * 60;
vpkm = km * 0.15;

print('Preço a pagar: R${:.2f}'.format(vpd+vpkm))