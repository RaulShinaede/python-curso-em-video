# Desafio: Um professor quer sortear um dos
# seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

from random import choice

alunos = [input('Nome do primeiro aluno: '),
          input('Nome do segundo aluno: '),
          input('Nome do terceiro aluno: '),
          input('Nome do quarto aluno: ')]

print('Aluno escolhido: {}'.format(choice(alunos)))
