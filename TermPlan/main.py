# Bibliotecas
import os
os.system('cls')

import csv

from datetime import datetime

# Funções
# CADASTRO
def cadastro():
    print(f'{"Crie Sua Conta":^60}')

    usuario = input('Usuário: ').strip()

    with open('TermPlan/contas.csv', 'r') as contas:
        leitor = csv.reader(contas)

        for linha in leitor:
            if usuario == linha[0]:
                print('Esse usuário já existe!')
                return
            
    senha = input('Senha: ').strip()

    with open('TermPlan/contas.csv', 'a', newline='') as contas:
        escritor = csv.writer(contas)
        escritor.writerow([usuario, senha])

        print('Cadastro realizado com sucesso!')

# LOGIN
def login():
    print(f'{"Entrar":^60}')

    usuariologin = input('Usuário: ').strip()

    with open ('TermPlan/contas.csv', 'r') as contas:
        leitor = csv.reader(contas)

        for linha in leitor:
            if usuariologin == linha[0]:
                senhalogin = input('Senha: ').strip()
                if senhalogin == linha[1]:
                    print(f'{"Bem-vindo(a)" + usuariologin + "!":^60}')

                else:
                    print('Senha incorreta. Tente novamente.')
                    return
                
            else:
                print('Usuário não encontrado. Tente novamente.')

# Tittle

print('-=-' * 20)
print(f'{"TermPlan":^60}')
print('-=-' * 20)
print()

# Já tem uma conta? / 
print(f'{'Você já tem uma conta?':^60}')
print('[1] Sim\n[2] Não')

resposta = int(input('-----> 1 ou 2: '))
print('___' * 20)

# Cadastro e Login

if resposta == 2:
    cadastro()

elif resposta == 1:
    login()
    
# DashBoard
print('___' * 20)
agora = datetime.now()









