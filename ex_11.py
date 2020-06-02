# 11. Altere o programa anterior, intercalando 3 vetores
# de 10 elementos cada.


a = []
b = []
c = []
abc = []
indice = 1
ind = 2

for i in range(10):
    a.append(int(input("Digite o {}º número do vetor a: ".format(i + 1))))
    abc.insert(i,a[i])
print()
for i in range(10):
    b.append(int(input("Digite o {}º número do vetor b: ".format(i + 1))))
    abc.insert(indice,b[i])
    indice += 2
print()
for i in range(10):
    c.append(int(input("Digite o {}º número do vetor c: ".format(i + 1))))
    abc.insert(ind,c[i])
    ind += 3

print("a = {}".format(a))
print("b = {}".format(b))
print("c = {}".format(c))
print("abc = {}".format(abc))