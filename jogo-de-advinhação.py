import random
print("Tente acertar um numero que estou pensando entre 1 e 10! ;)")
numero = int(input("Digite um numero de 1 a 10: "))
n_aleatorio = random.randint(0,10)+1

if numero == n_aleatorio:
    print("Parábens você acertou o numero! você é bom!!!")
else:
    print("O Numero Que eu escolhi foi o {}".format(n_aleatorio))
    print("Hum... Tente novamente!!!")


