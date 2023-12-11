# Fazer 10 questões em um codigo e dizer se esta correto ou errado
q1 = 1
q2 = 2
q3 = 3
q4 = 4
q5 = 5
q6 = 6
q7 = 7
q8 = 8
q9 = 9
q10 = 10
questoes = q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
questao = questoes
for questao in range(1, 11):
    questoes = int(input(f'Digite a resposta da questão {questao}: '))
    if questoes == questao:
        print('Você acertou!')
    else:
        questoes != questao
        print('Você errou.')