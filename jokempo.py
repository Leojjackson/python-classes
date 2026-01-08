import random
from time import sleep

# Jogo de Jo kem Po

jokempo = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0,2)
print("Jogo De Jo-kem-po")
print(''' Suas Opções:
        [ 1 ] Pedra
        [ 2 ] Papel
        [ 3 ] Tesoura
        ''')
jogador = int(input("Qual é a sua jogada? :"))
print("Jo")
sleep(1)
print("KEM")
sleep(1)
print("PO")
print('-='*15)
print("Computador Jogou: {}".format(jokempo[computador]))
print("Jogador jogou: {}".format(jokempo[jogador]))
print('-='*20)

if computador == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("JOGADOR VENCE")
    if jokempo == 2:
        print("COMPUTADOR VENCE")
    else:
        print('Jogada Invalida')
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print('EMPATE')
    if jokempo == 2:
        print("JOGADOR VENCE")
    else:
        print('Jogada Invalida')
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    if jokempo == 2:
        print("EMPATE")
    else:
        print('Jogada Invalida')



