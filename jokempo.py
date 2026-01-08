import random
from time import sleep

# Jogo de Jo kem Po

jokempo = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0,2)
print("Jogo De Jo-kem-po")
print(''' Suas Opções:
        [ 0 ] Pedra
        [ 1 ] Papel
        [ 2 ] Tesoura
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
print('-='*15)

if computador == 0: #pedra
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("JOGADOR VENCE")
    if jogador == 2:
        print("COMPUTADOR VENCE")

elif computador == 1: #papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print("JOGADOR VENCE")

elif computador == 2: #tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    if jogador == 2:
        print("EMPATE")




