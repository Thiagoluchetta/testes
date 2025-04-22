#Construção de algoritmo para estudo de lógica de programação e python
#Servirá como um app de organização financeira
#irei adicionar novas funções conformo aprendo, evoluindo o código e trazendo novidades!

#menu inicial
gastos = []
def listar_gastos():
    if not gastos:
        print("\nNenhuma despesa registrada ainda.")
        return

    print("\n=== Lista de Despesas ===")
    for i, gasto in enumerate(gastos, start=1):
        print(f"\nDespesa {i}")
        print("-" * 30)
        print(f'Descrição : {gasto["descrição"]}')
        print(f'Categoria : {gasto["categoria"]}')
        print(f'Valor     : R$ {gasto["valor"]:.2f}')
    print("-" * 30)


def adicionar_gastos():
    print("=== Adicionar Gastos ===")
    try:
        valor = float(input("Qual o valor do gasto?"))
        descricao = input('Qual a descrição do gasto?')
        categoria = input('Qual a categoria do gasto?')

        gasto = {
            "valor" : valor,
            "descrição" : descricao,
            "categoria" : categoria,
        }

        gastos.append(gasto)
        print('\nGasto Adicionado com Sucesso!')
        print("-" * 30)
        print(f'Descrição : {gasto["descrição"]}')
        print(f'Categoria : {gasto["categoria"]}')
        print(f'Valor : R$ {gasto["valor"]:.2f}')
        print('-'*30)
        
    except ValueError:
        print("Digite um número válido")


def mostrar_menu():
    print('\n=====Organizador financeiro=====')
    print('1.Adicionar despesa.')
    print('2.Adicionar receita.')
    print('3.Mostrar gastos.')
    print('4.Limpar operações')
    print('5.Sair')

def executando_menu():
    while True:
        mostrar_menu()
        try:
            opcao = int(input('Qual operação deseja realizar?'))
        except ValueError:
            print('Digite um número válido!')
            continue

        if opcao == 1:
            adicionar_gastos()
        elif opcao == 2:
            print('2')
        elif opcao == 3:
            listar_gastos()
        elif opcao == 4:
            print('4')
        elif opcao == 5:
            print('saindo')
            break
        else:
            print('opção inválida')

executando_menu()
