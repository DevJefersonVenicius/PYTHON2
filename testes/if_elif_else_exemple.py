# Utilizando if, elif e else
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
nota4 = float(input('Digite sua nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media == 10:
    print('Você tirou nota maxima! Parabens!!!')
elif media >= 6:
    print('Você passou.')
else:
     print('Você reprovou.')
print('Sua media foi: ',media)