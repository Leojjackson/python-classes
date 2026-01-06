# Crie um programa que calcule a velocidade de um carro na rodovia
# onde o permitido é 90km/h com multa de 9$ por km excedido.


print("Verificador de Velocidade")

print("Limite permitido = 90KM/H")

velocidade = int(input("Qual a velocidade do carro? "))

if velocidade < 90:
    print("Você não Ultrapassou o limite da via. Sem Multas!!!")
else:
    multa = (velocidade - 90) * 9
    print("Você Ultrapassou o limite da via. Multado!!!")
    print("O limite permitido é de \033[32m{}KM/H\033[m, Sua velocidade foi de \033[31m{}KM/H\033[m, Você Foi multado no valor de \033[31m{}\033[m.".format(90, velocidade, multa))