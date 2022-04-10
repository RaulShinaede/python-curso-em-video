# Desafio: O mesmo professor do desafio anterior
# quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos
# quatro alunos e mosrtre a ordem sorteada.

import random

alunos = [input('Nome do primeiro aluno: '),
          input('Nome do segundo aluno: '),
          input('Nome do terceiro aluno: '),
          input('Nome do quarto aluno: ')]

seq = random.sample(alunos, k=4)

print('Primeiro: {}, Segundo: {}, Terceiro: {}, Quarto: {}'.format(seq[0], seq[1], seq[2], seq[3]))
