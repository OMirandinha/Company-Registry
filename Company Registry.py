import copy

print('Bem vindo a empresa do Vitor Hugo Miranda')

id_global = 4994878
lista_funcionarios = []

def cadastrar_funcionario(id):

    nome = input("Digite seu nome: ")
    setor = input("Entre com o setor respectivo: ")
    salario = float(input("Entre com seu sálario: "))

    #Método para copiar os inputs dentro da lista de funcionários
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

    lista_funcionarios.append(copy.deepcopy(funcionario))

def consultar_funcionarios():

    #Laço de repetição que permite o usuário a voltar para o menu
    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar Todos")
        print("2. Consultar por id")
        print("3. Consultor por setor")
        print("4. Retornar ao menu")

        opcao = input("Digite a opçao desejada: ")

        #Consulta geral
        if opcao == '1':
            for f in lista_funcionarios:
                print(f)

        #Consulta por ID
        elif opcao == '2':
            id = int(input("Digite o ID do funcionário"))
            encontrado = False
            for f in lista_funcionarios:
                if f['id'] == id:
                    print(f)
                    encontrado = True
                    break
                if not encontrado:
                    print("ID inválido")

        #Consulta por setor
        elif opcao == '3':

            setor = input("Digite o setor do funcionário: ")
            encontrados = [f for f in lista_funcionarios if f['setor'] == setor]
            if encontrados:
                for f in encontrados:
                    print(f)
            else:
                print('Nenhum funcionário encontrado neste setor')

        #Volta para o menu anterior
        elif opcao == '4':
            return

        else:
            print('Opção inválida')


def remover_funcionario():

    #Função que deleta o respectivo funcionário da lista
    id = int(input("Digite o ID do funcionário a ser removido: "))
    global lista_funcionarios
    lista_funcionarios = [f for f in lista_funcionarios if f['id'] != id]
    if len(lista_funcionarios) == len([f for f in lista_funcionarios if f['id'] != id]):
        print("ID inválido.")
    else:
        print("Funcionário removido com sucesso.")


while True:

    #Menu principal do programa com as opções disponíveis ao usuário
    print("\nMenu Principal:")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        id_global += 1
        cadastrar_funcionario(id_global)

    elif opcao == '2':
        consultar_funcionarios()

    elif opcao == '3':
        remover_funcionario()

    elif opcao == '4':
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida")