# Bibliotecas
import os
os.system('cls')

# Título
print('-=-'*20)
print(f'{"CODLY".center(60)}')
print('-=-'*20)

# Seleção de Matérias

print('Selecione a matéria para treinar!\n'.center(60))
print('[1] Fundamentos da Programação')
print('[2] Matemática para Computação')
print('[3] Introdução à Computação')
print('[4] Sistemas Digitais')
print('[5] Gestão de Pessoas')

materia = int(input('➜ Matéria: '))

# Atividades Fundamentos da Programação

if materia == 1:
    print('---'*20)
    print('Selecione o assunto que você quer treinar!\n'.center(60))
    print('[1] Estruturas Condicionais')
    print('[2] Estruturas de Repetição')
    print('[1] Listas')

    assuntoFP = int(input('➜ Assunto: '))

    if assuntoFP == 1:
        

    