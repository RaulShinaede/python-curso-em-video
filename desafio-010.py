# Desafio: Crie um programa que leia quanto dinheiro uma
# pessoa tem na carteira e mostre quantos dólares
# ela pode comprar
# Considere US$1,00 = R$3,27

valor = float(input('Dinheiro em reais: '))
cotacao = 3.27

print('Você pode comprar US${0:.2f} dólares'.format(valor / cotacao))