# 6. Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima
# o número de alunos com média maior ou igual a 7.0.

aluno = []
nota = 0
media = 0
soma = 0

for i in range(10):
    print("Aluno {}".format(i+1))
    for j in range(4):
        nota = float(input("Nota {}: ".format(j+1)))
        soma += nota
    print()
    media = soma / 4
    soma = 0

    if (media >= 7.0):
        aluno.append(round(media,1))

print("Alunos aprovados = {}".format(len(aluno)))
