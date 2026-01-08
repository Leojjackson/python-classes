import random

# Jogo de Jo kem Po

jokempo = ['Pedra', 'Papel', 'Tesoura']
aleatorio = random.randint(0,2)
jokempo = jokempo[aleatorio]
print("Jogo De Jo-kem-po")
print(jokempo)
print('''
        [ 1 ] Pedra
        [ 2 ] Papel
        [ 3 ] Tesoura''')
escolha = int(input("Digite o numero de sua escolha: "))



