# 15. Faça um programa que leia um número indeterminado
# de valores, correspondentes a notas, encerrando a
# entrada de dados quando for informado um valor igual
# a -1 (que não deve ser armazenado). Após esta entrada
# de dados, faça:
#
# a. Mostre a quantidade de valores que foram lidos;
#
# b. Exiba todos os valores na ordem em que foram
# informados, um ao lado do outro;
#
# c. Exiba todos os valores na ordem inversa à que
# foram informados, um abaixo do outro;
#
# d. Calcule e mostre a soma dos valores;
#
# e. Calcule e mostre a média dos valores;
#
# f. Calcule e mostre a quantidade de valores acima
# da média calculada;
#
# g, Calcule e mostre a quantidade de valores abaixo
# de sete;
#
# h. Encerre o programa com uma mensagem;


numero = 0
valores = []
valores_alto = []
valores_abaixo7 = []

while(True):
    numero = int(input("Digite um número: "))
    if (numero != -1):
        valores.append(numero)
    else:
        break

soma = sum(valores)
media = soma / len(valores)

for i in range(len(valores)):
    if (valores[i] > media):
        valores_alto.append(valores[i])

for i in range(len(valores)):
    if (valores[i] < 7):
        valores_abaixo7.append(valores[i])

print("Quantidade de valores: {}".format(len(valores)))
print("Valores = {}".format(valores))
print("Valores Invertidos = {}".format(valores[::-1]))
print("Soma: {}".format(soma))
print("Média: {}".format(round(media,2)))
print("Valores assima da média = {}".format(valores_alto))
print("Valores abaixo de 7 = {}".format(valores_abaixo7))
print("Fim do programa...")
