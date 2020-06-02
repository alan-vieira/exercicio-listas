# 5. Faça um Programa que leia 20 números inteiros e
# armazene-os num vetor. Armazene os números pares no
# vetor PAR e os números IMPARES no vetor impar. Imprima
# os três vetores.


numero = []
par = []
impar = []

for i in range(20):
    numero.append(int(input("Digite o {}º número: ".format(i+1))))
    if ((numero[i] % 2) == 0):
        par.append(numero[i])
    else:
        impar.append(numero[i])
print()
print("Números = {}".format(numero))
print("Pares = {}".format(par))
print("Ímpares = {}".format(impar))
