# 10. Faça um Programa que leia dois vetores com 10
# elementos cada. Gere um terceiro vetor de 20 elementos
# , cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.


a = []
b = []
ab = []
indice = 1

for i in range(10):
    a.append(int(input("Digite o {}º número do vetor a: ".format(i + 1))))
    ab.insert(i,a[i])

print()
for i in range(10):
    b.append(int(input("Digite o {}º número do vetor b: ".format(i + 1))))
    ab.insert(indice,b[i])
    indice += 2
print("a = {}".format(a))
print("b = {}".format(b))
print("ab = {}".format(ab))