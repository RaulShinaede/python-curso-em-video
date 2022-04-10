# Desafio: Faça um programa que leia uma
# frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input("Entre com a frase: ")

print("Quantidade de letras A: {}".format(frase.upper().count("A")))
print("Primeira posição: {}".format(frase.upper().find('A')))
print("Última posição: {}".format(frase.upper().rfind('A')))