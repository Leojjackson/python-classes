# Simples Tratamento de Dados...

from datetime import date
Nome = str(input("Digite Seu Nome: ")).lstrip().title()
Idade = int(input("Digite sua Idade: "))
resultado = date.today().year
a = resultado - Idade
def imprimir_dados (n, i, a):
    print(f"Nome: {n}")
    print(f"Idade: {i} Anos De Idade")
    print(f"Ano de nascimento: {a}")

imprimir_dados (Nome, Idade, a)

array = []

array.append(Nome)
array.append(Idade)
array.append(a)

print(array)