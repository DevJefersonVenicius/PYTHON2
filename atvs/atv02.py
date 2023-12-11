# Escreva um programa que verifica se um número é positivo, negativo ou zero.
# Use um loop for para imprimir os números pares de 1 a 10.
numero = int(input('Digite um número: '))

if numero == 0:
    print(f'O número digitado foi: {numero}')
elif numero < 0:
    print(f'O número digitado é negativo: {numero}')
else:
    print(f'O número digitado é positivo: {numero}')

for i in range(1, 11): 
    if i % 2 == 0:
        print(i)