import random

# Jogo de Jo kem Po

jokempo = ['papel', 'tesoura', 'pedra']
aleatorio = random.randint(0,2)
print("Jogo De Jo-kem-po")
print('''
        [ 1 ] Pedra
        [ 2 ] Papel
        [ 3 ] Tesoura''')
escolha = int(input("Digite o numero de sua escolha: "))

