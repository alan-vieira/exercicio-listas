# 9. Faça um Programa que leia um vetor A com 10 números
# inteiros, calcule e mostre a soma dos quadrados dos
# elementos do vetor.

a = []
soma = 0

for i in range(10):
    a.append(int(input("Digite o {}º número: ".format(i + 1))))
    soma += (a[i] ** 2)

print("Soma dos quadrados = {}".format(soma))
