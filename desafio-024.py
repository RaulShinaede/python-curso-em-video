# Desafio: Crie um programa que leia
# o nome de uma cidade e diga se ela
# começa ou não com o nome "SANTO".

cidade = input("Nome da cidade: ")

print("Começa com SANTO? {}".format(cidade.upper().find('SANTO') == 0))