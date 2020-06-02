# 22. Sua organização acaba de contratar um
# estagiário para trabalhar no Suporte de
# Informática, com a intenção de fazer um
# levantamento nas sucatas encontradas nesta
# área. A primeira tarefa dele é testar todos
# os cerca de 200 mouses que se encontram lá,
# testando e anotando o estado de cada um
# deles, para verificar o que se pode aproveitar
# deles.
#
# Foi requisitado que você desenvolva um
# programa para registrar este levantamento.
# O programa deverá receber um número
# indeterminado de entradas, cada uma
# contendo: um número de identificação
# do mouse o tipo de defeito:
#
# necessita da esfera;
# necessita de limpeza; a.necessita troca
# do cabo ou conector; a.quebrado ou
# inutilizado Uma identificação igual a
# zero encerra o programa. Ao final o
# programa deverá emitir o seguinte relatório:
#
# Quantidade de mouses: 100
#
# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%


situacao = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo ou conector", "quebrado ou inutilizado"]
problema = [0] * 4

cont = 0

print()
print("Registro de mouses com defeito:")
print()
print("1- necessita da esfera")
print("2- necessita de limpeza")
print("3- necessita troca do cabo ou conector")
print("4- quebrado ou inutilizado")
print()
while(True):
    prob = int(input("Problema: "))
    if (prob != 0):
        problema[prob - 1] += 1
        cont += 1
    else:
        break
print()
print("Quantidade de mouses: {}".format(cont))
print()
print("Situação                        Quantidade              Percentual")

for i in range(len(problema)):
    print("{}- {}                  {}                     {}%".format(i+1, situacao[i], problema[i], round(((100 * problema[i]) / cont),1)))

