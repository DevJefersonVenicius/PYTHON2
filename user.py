dic_acessos = {'Jeferson': '12345', 'João': '121212'}

user = input('Informe seu USUARIO: ')
password = input('Informe sua SENHA: ')

user_password = {}
user_password[user] =  password

for chave in dic_acessos.keys():
    if chave == user and dic_acessos[chave] and dic_acessos[chave] == user_password[user]:
        print('Acesso liberado')
        if chave != user:
            print(f'O usuario {user} não foi encontrado')
            break
        else:
            print(f'Senha incorreta para o usuario {user}')
        break
    else:
        print(f'O usuario {user} não foi encontrado')
        break
    