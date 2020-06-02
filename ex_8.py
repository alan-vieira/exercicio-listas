# 8. Faça um Programa que peça a idade e a altura de
# 5 pessoas, armazene cada informação no seu respectivo
# vetor. Imprima a idade e a altura na ordem inversa a
# ordem lida.

idade = []
altura = []

for i in range(5):
    idade.append(int(input("Digite a idade: ")))
    altura.append(int(input("Digite a altura: ")))
    print()

print("Idade = {}".format(idade[::-1]))
print("Altura = {}".format(altura[::-1]))
