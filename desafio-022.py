# Desafio: Crie um programa que leia o nome completo
# de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeito nome

nome = input('Digite o nome completo: ')

print("Nome em maiúsculo: {}".format(nome.upper()))
print("Nome em minúsculo: {}".format(nome.lower()))
print("Quantidade de letras (sem espaços): {}".format(len(nome.replace(" ", ""))))

primeiroNome = nome.split()[0]

print("Quantidade de letras no primeiro nome: {}".format(len(primeiroNome)))

