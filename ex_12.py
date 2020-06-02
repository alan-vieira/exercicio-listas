# 12. Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com
# mais de 13 anos possuem altura inferior à média de
# altura desses alunos.

idade = []
altura = []
altura13 = []
altura_media = []

for i in range(5):
    print("Aluno {}".format(i+1))
    idade.append(int(input("Idade: ")))
    altura.append(float(input("Altura: ")))
    if (idade[i] > 13):
        altura13.append(altura[i])
    print()
media = sum(altura13) / len(altura13)

for i in range(len(altura13)):
    if (altura13[i] < media):
        altura_media.append(altura13[i])
print("Alunos com altura inferior a média: {}".format(len(altura_media)))
