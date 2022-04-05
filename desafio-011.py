# Desafio: Faça um programa que leia a largura
# e a altura de uma parede em metros, calcule a
# sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m²

larg = int(input('Largura da parede em metros: '))
alt = int(input('Altura da parede em metros: '))
area = larg * alt

print('Para pintar uma parede de área: {0}, é necessário {1} de tinta'.format(area, area / 2))

