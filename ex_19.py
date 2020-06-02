# 19. Uma empresa de pesquisas precisa tabular
# os resultados da seguinte enquete feita a
# um grande quantidade de organizações:
#
# "Qual o melhor Sistema Operacional para uso
# em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
#
# Você foi contratado para desenvolver um
# programa que leia o resultado da enquete
# e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser
# informado o valor 0, que encerra a entrada
# dos dados. Não deverão ser aceitos valores
# além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções
# devem ser armazenados num vetor. Após os
# dados terem sido completamente informados,
# o programa deverá calcular a percentual de
# cada um dos concorrentes e informar o
# vencedor da enquete. O formato da saída
# foi dado pela empresa, e é o seguinte:
#
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
#
# O Sistema Operacional mais votado foi o Unix,
# com 3500 votos, correspondendo a 40% dos votos.


votos = [0] * 6
numero = -1
total_votos = 0
jogador = []
sistema = ["Windows Server", "Unix          ", "Linux         ", "Netware       ", "Mac OS        ", "Outro         "]

for i in range(1,7):
    jogador.append(i)
print()
print("Qual o melhor Sistema Operacional para uso em servidores?")
print()
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")
print()

while (numero != 0):
    numero = int(input("Digite sem voto (0=fim): "))
    if (numero < 0) or (numero > 6):
        print("Informe um valor entre 1 e 6 ou 0 para sair!")
        continue
    if (numero != 0):
        votos[numero - 1] += 1
        total_votos += 1

print()
print ("Sistema Operacional      Votos             %")


melhor_jogador  = 0
votos_jogador = 0
porcentagem_jogador = 0

for i in range(len(votos)):
    if(votos[i] > 0):
        print(("{}             {}               {}".format(sistema[i], votos[i], round(((100 * votos[i])/total_votos), 2))))

    if(votos[i] == max(votos)):
        melhor_jogador = jogador[i]
        votos_jogador = votos[i]
        so = sistema[i]
        porcentagem_jogador = round(((100 * votos[i])/total_votos), 2)
print("Total                      {}".format(total_votos))
print()
print('O Sistema Operacional mais votado foi o  {},  com  {}  votos, correspondendo a {} % do total de votos'.format(so, votos_jogador, porcentagem_jogador))
