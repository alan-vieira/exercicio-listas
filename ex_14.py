# 14. Utilizando listas faça um programa que faça 5
# perguntas para uma pessoa sobre um crime. As perguntas
# são:
#
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
#
# O programa deve no final emitir uma classificação
# sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser
# classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário,
# ele será classificado como "Inocente".


pergunta = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
resposta = ""
cont = 0

for i in range(len(pergunta)):
    resposta = input("{} ".format(pergunta[i]))
    if (resposta == "sim"):
        cont += 1
print()

if (cont == 2):
    print("Suspeito(a)")
if (cont >= 3 and cont <= 4):
    print("Cúmplice")
if(cont >= 5):
    print("Assassino")
if(cont < 2):
    print("Inocente")
