# 13. Faça um programa que receba a temperatura média de
# cada mês do ano e armazene-as em uma lista. Após isto,
# calcule a média anual das temperaturas e mostre todas
# as temperaturas acima da média anual, e em que mês
# elas ocorreram (mostrar o mês por extenso:
# 1 – Janeiro, 2 – Fevereiro, . . . ).


temperatura = []
mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range(len(mes)):
    print(mes[i])
    temperatura.append(float(input("Digite a temperatura: ")))
    print()

media = sum(temperatura) / len(temperatura)
print()

for i in range (len(temperatura)):
    if (temperatura[i] > media):
        print("{} - {}".format(mes[i],temperatura[i]))