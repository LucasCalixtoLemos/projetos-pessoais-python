import csv

# CADASTRO
def cadastro():
    print(f'{"Criar Conta":^60}')

    usuario = input('Usuário: ')

    with open('data/contas.csv', 'r') as contas:
        leitor = csv.reader(contas)

        for linha in leitor:
            if usuario == linha[0]:
                print('Usuário já existe!')
                return 
               
    with open ('TermPlan/data/contas.csv', 'a', newline='') as contas:
        escritor = csv.writer(contas)
        escritor.writerow(linha)

    senha = input('Senha: ')

    print('-----> Cadastro realizado com sucesso!')
    print('___' * 20)

# LOGIN
def login():
    print(f'{"Entrar":^60}')

    usuariologin = input('Usuário: ')
    senhalogin = input('Senha: ')

    with open ('TermPlan/data/contas.csv', 'r') as contas:
        leitor = csv.reader(contas)

        for linha in leitor:
            if usuariologin == linha[0] and senhalogin == [1]:
                print(f'Bem-vindo {linha[0]}!')

    with open ('TermPlan/data/contas.csv', 'r') as contas:
        leitor = csv.reader(contas)

        for linha in leitor:
            if usuariologin != linha[0] or senhalogin != linha[1]:
                print('Usuário não encontrado, tente novamente.')
                return

