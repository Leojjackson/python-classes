let array = []

let menor = 0
let maior = 0

let contador = 0

do{
    let numero = prompt("Digite um valor: ")
    numero = Number(numero)

    if (array.length == 0){
        menor = numero
        maior = numero
    }
    if (numero > maior){
        maior = numero
    }
    else if(numero < menor){
        menor = numero
    }
    
    
    array.push(numero)
    contador ++

}while(contador < 5);
console.log(array)
console.log(`Os Valores Digitados no array foram: ${array.length}`)
console.log(`O Maior Valor Digitado foi: ${maior}`)
console.log(`O Menor Valor Digitado foi: ${menor}`)