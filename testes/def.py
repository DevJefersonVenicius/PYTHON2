# codigo que soma dois numeros e diz se é verdadeiro ou falso
num1 = 20
num2 = 35

def resultado(num1, num2):
    numero = int(num1)
    numero2 = int(num2)
    if num1 + num2 == 55:
        print('Verdadeiro')
    else:
        print('A soma está incorreta')   
    resultado = num1 + num2
    return resultado
num1 = int(input('Digite o numero: '))
num2 = int(input('Digite o numero: '))
print(resultado(num1, num2))