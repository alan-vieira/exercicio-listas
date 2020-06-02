# 4. Faça um Programa que leia um vetor de 10 caracteres, e
# diga quantas consoantes foram lidas. Imprima as consoantes.


vetor = list("Inconstitucional")
vetor_consoante = []
consoante = 0

for i in range(len(vetor)):
    if not (vetor[i] == 'a' or vetor[i] == 'e' or vetor[i] == 'i'
            or vetor[i] == 'o' or vetor[i] == 'u'
            or vetor[i] == 'A' or vetor[i] == 'E' or vetor[i] == 'I'
            or vetor[i] == 'O' or vetor[i] == 'U'):
        consoante += 1
        vetor_consoante.append(vetor[i])

print()
print("Quantidade de consoantes: {}".format(consoante))
print(vetor_consoante)
