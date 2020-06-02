# 16. Utilize uma lista para resolver o problema a seguir.
# Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de
# suas vendas brutas daquela semana. Por exemplo, um
# vendedor que teve vendas brutas de $3000 em uma semana
# recebe $200 mais 9 por cento de $3000, ou seja, um
# total de $470. Escreva um programa (usando um array
# de contadores) que determine quantos vendedores
# receberam salários nos seguintes intervalos de valores:
#
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
#
# Desafio: Crie ma fórmula para chegar na posição da
# lista a partir do salário, sem fazer vários ifs
# aninhados.

salario = []
nivel = [200, 299, 300, 399, 400, 499, 500, 599, 600, 699, 700, 799, 800, 899, 900, 999, 1000, 1999]
faixa = [0] * 9

#composição do salário
while(True):
    venda = int(input("Valor da venda: R$ "))
    if (venda != -1):
        comissao = ((venda * 9) / 100)
        salario.append(200 + comissao)
    else:
        break

#loop do salário
for i in range(len(salario)):
    cont1 = 0
    cont2 = 1
#loop da faixa salarial
    for j in range(len(faixa)):
        if (salario[i] >= nivel[cont1] and salario[i] <= nivel[cont2]):
            faixa[j] += 1

        cont1 += 2
        cont2 += 2

#loop da resposta
contador = 2
print()
for i in range(len(faixa)):
    print("{} receberam entre R$ {}00 e R$ {}99".format(faixa[i], contador, contador))
    contador += 1
