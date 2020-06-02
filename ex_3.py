# 3. Faça um Programa que leia 4 notas, mostre as notas e a
# média na tela.


notas = []
for i in range(4):
    notas.append(float(input("Digite a {}ª nota: ".format(i+1))))

media = sum(notas) / len(notas)

print("Notas: {}".format(notas))
print("Média: {}".format(round(media,2)))

