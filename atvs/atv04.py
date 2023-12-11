# Crie uma função chamada soma que recebe dois parâmetros e retorna a soma deles.
# Chame a função com dois números e imprima o resultado.

def soma(num, num2):
    resultado = num + num2
    return resultado

num = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
print(f'O resultado da soma foi de: {soma(num, num2)}')