# 24. Faça um programa que simule um lançamento
# de dados. Lance o dado 100 vezes e armazene
# os resultados em um vetor . Depois, mostre
# quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e
# uma função para gerar numeros aleatórios,
# simulando os lançamentos dos dados.


import random

jogada = [0] * 100

for i in range(100):
    dado = random.randrange(1, 7)
    jogada[i] = dado

print("\nEm 100 jogadas:\n")
for i in range(6):
    print("O número {} saiu {} vezes.".format(i+1,jogada.count(i+1)))
