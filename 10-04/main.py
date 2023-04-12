import json
import sys
import os
import time


with open('banco.json', 'r', encoding='utf-8') as funcionariosJson:
    n = json.load(funcionariosJson)


def nomeDepartamento(valor):
    for i in range(len(n["Departamento"])):
        if valor == (n["Departamento"][i]["ID_Departamento"]):
            return (n["Departamento"][i]["Nome_Departamento"])

def printLento(texto, velocidadetexto=0.08):
    for x in texto:
        print(x, end='', flush=True)
        time.sleep(velocidadetexto)


def listaFuncionarios():
    for i in range(len(n["Funcionario"])):
        print(n["Funcionario"][i]["Nome_Funcionario"])


def listaDepartamentos():
    for i in range(len(n["Departamento"])):
        print(n["Departamento"][i]["Nome_Departamento"])


def infoFuncionario():
    for i in range(len(n["Funcionario"])):
        print(f'{n["Funcionario"][i]["ID_Funcionario"]} - {n["Funcionario"][i]["Nome_Funcionario"]}')
    
    print('Digite o ID do funcionario que deseja ver as informações!')
    a = input('> ')
    os.system('cls')
    
    for funcionario in n["Funcionario"]:
        if funcionario['ID_Funcionario'] == int(a):
            printLento(f'''
Não pisque!
Carregando informações referente ao funcionario {funcionario["Nome_Funcionario"]}  .  .  .  .''')
            os.system('cls')
            print(f'\nInformações de cadastro do funcionario {funcionario["Nome_Funcionario"]}')
            print(f'''
ID - {funcionario["ID_Funcionario"]}
Nome - {funcionario["Nome_Funcionario"]}
CPF - {funcionario["CPF_Funcionario"]}
Departamento - {funcionario["ID_Departamento"]}''')


def infoDepartamento():
    for i in range(len(n["Departamento"])):
        print(f'{n["Departamento"][i]["ID_Departamento"]} - {n["Departamento"][i]["Nome_Departamento"]}')

    print('Digite o ID do departamento que deseja ver as informações!')
    a = int(input('> '))

    os.system('cls')

    for departamento in n["Departamento"]:
        if departamento['ID_Departamento'] == int(a):
            printLento(f'''
Não pisque!
Carregando informações referente ao departamento {departamento["Nome_Departamento"]}  .  .  .  .\n\n''')
            
    print('   Funcionarios   ')

    for i in range(len(n["Funcionario"])):
        if n["Funcionario"][i]["ID_Departamento"] == a:
            print(f'{n["Funcionario"][i]["Nome_Funcionario"]}')

# with open('banco.json', 'w') as funcionariosJson:
#     json.dump(n,funcionariosJson, indent=2)


def menu():
    os.system('cls')
    

    while True:
        try:
            print('''
        Menu
    
1 - Funcionarios.
2 - Departamentos.

0 - SAIR.''')
            
            escolha = int(input('> '))
            match escolha:
                
                case 1:
                    os.system('cls')
                    print('''
1 - Lista de Funcionarios.
2 - Informações Funcionarios.

3 - Voltar ao menu anterior.

0 - SAIR.''')
                    a = int(input('> '))
                    match a:
                        case 1:
                            os.system('cls')
                            listaFuncionarios()
                            input('')
                        case 2:
                            os.system('cls')
                            infoFuncionario()
                            input('')
                        case 3:
                            os.system('cls')
                            menu()
                        case 0:
                            os.system('cls')
                            exit()

                case 2:
                    os.system('cls')
                    print('''
1 - Lista de Departamentos.
2- Informações Departamentos.

3 - Voltar ao menu anterior.

0 - SAIR.''')
                    b = int(input('> '))
                    match b:
                        case 1:
                            os.system('cls')
                            listaDepartamentos()
                            input('')
                        case 2:
                            os.system('cls')
                            infoDepartamento()
                            input('')
                        case 3:
                            os.system('cls')
                            menu()
                        case 0:
                            os.system('cls')
                            exit()

                case 0:
                    os.system('cls')
                    printLento('Saindo do sistema ....')
                    os.system('cls')
                    #break
                    #sys.exit()
                    exit()
        except(ValueError):
            os.system('cls')
            print("Valor invalido!")


menu()