# Um programa que Mostra o maior e o menor valor de uma lista de numeros ilimitados.

lista = []

maior = menor = 0

print("[ DIGITE UMA LETRA PARA ENCERRAR O PROGRAMA!!! ]!")
while True:
    try:
        numero = int(input('Digite um numero: '))

        if lista == []:
            maior = menor = numero
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

        lista.append(numero)

    except ValueError:
        break

print('-='*30)
print(f"Os Valores digitados foram: {lista}")
print(f'O Maior valor digitado foi: {maior}')
print(f'O Menor valor digitado foi: {menor}')