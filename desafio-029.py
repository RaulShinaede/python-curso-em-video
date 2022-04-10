# Desafio: Escreva um programa que leia a
# velocidade de um carro.
# Se ela ultrapassar  80Km/h, mostre uma
# mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite

vel = int(input('Qual é a velocidade do carro? '))

if vel > 80:
    print('Você foi multado em R${}'.format((vel-80) * 7))