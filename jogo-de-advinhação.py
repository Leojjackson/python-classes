'''import random
print("Tente acertar um numero que estou pensando entre 1 e 10! ;)")
numero = int(input("Digite um numero de 1 a 10: "))
n_aleatorio = random.randint(0,10)+1

if numero == n_aleatorio:
    print("Parábens você acertou o numero! você é bom!!!")
else:
    print("O Numero Que eu escolhi foi o {}".format(n_aleatorio))
    print("Hum... Tente novamente!!!")'''


# Colocando em prática


# Programando um Jogo de advinhação melhorado 2.0...


from random import randint
import time


jogador = 0
computador = randint(1,10)
tentativas = 5


while True:

    print("-=" * 15)
    print("{:^40}".format("\033[1;33m Jogo de Advinhação\033[m"))
    print("-=" * 15)
    jogador = int(input("Digite um numero de  1 a 10: "))
    print("Analisando os numeros...")
    time.sleep(2)
    if jogador != computador:
        print("Você errou o numero, tente novamente")
        tentativas -= 1
        print(f'O computador jogou o numero {computador} e você jogou o numero {jogador}')
        print("O computador ganhou!!!")
        print(f'Tentativas restantes {tentativas}')
    if tentativas == 0:
        print("Suas tentativas acabaram! Tente novamente!")
        break
    if jogador == computador:
        print(f"O computador jogou {computador} e você jogou {jogador}, parabéns você Ganhou!!!")
        print(f'Ganhou com {tentativas} tentativas Restantes!')


