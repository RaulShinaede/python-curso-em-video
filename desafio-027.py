# Desafio: Faça um programa que leia o nome
# completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente

nome = input("Entre com o nome: ")

nomeDividido = nome.split()

print("Nome completo: {}".format(nome))
print("Primeiro Nome: {}".format(nomeDividido[0]))
print("Segundo Nome: {}".format(nomeDividido[len(nomeDividido)-1]))