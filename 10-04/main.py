import json


with open('banco.json', 'r', encoding='utf-8') as funcionariosJson:
    n = json.load(funcionariosJson)

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
    
    for funcionario in n["Funcionario"]:
        if funcionario['ID_Funcionario'] == int(a):
            print(funcionario)

infoFuncionario()