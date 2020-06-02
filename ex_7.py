# 7. Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.


vetor = []
soma = 0
produto = 1

for i in range(5):
    vetor.append(int(input("Digite o {}º número: ".format(i+1))))
    soma += vetor[i]
    produto *= vetor[i]

print()
print("Soma: {}".format(soma))
print("Produto: {}".format(produto))
print("Números = {}".format(vetor))
