#Construção de algoritmo para estudo de lógica de programação e python
#Servirá como um app de organização financeira
#irei adicionar novas funções conformo aprendo, evoluindo o código e trazendo novidades!

#menu inicial
import json

gastos = []
receitas = []

def salvar_dados():
    dados = {
        'receitas': receitas,
        'gastos': gastos
    }
    with open('dados_financeiros.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados():
    global receitas, gastos
    try:
        with open('dados_financeiros.json', 'r') as arquivo:
            dados = json.load(arquivo)
            receitas = dados.get('receitas', [])
            gastos = dados.get('gastos', [])
    except FileNotFoundError:
        receitas = []
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

def adicionar_receita():
    print('----adicionar receitas----')
    try:
        valorR = float(input('Qual o valor da receita?'))
        categoriaR = input('Qual a descrição da receita?')

        receita = {
            'valor' : valorR,
            'categoria' : categoriaR,
        }

        receitas.append(receita)
        salvar_dados()
        print('Receita adicionada com sucesso!')
        print( '-' * 30)
        print(f'Categoria: {receita['categoria']}')
        print(f'Valor : R$ {receita["valor"]:.2f}')
        print('-'*30)

    except ValueError:
        print('Digite um número válido!')

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
        salvar_dados()
        print('\nGasto Adicionado com Sucesso!')
        print("-" * 30)
        print(f'Descrição : {gasto["descrição"]}')
        print(f'Categoria : {gasto["categoria"]}')
        print(f'Valor : R$ {gasto["valor"]:.2f}')
        print('-'*30)
        
    except ValueError:
        print("Digite um número válido")

def limpar_operações():
    print('tem certeza que deseja apagar as informações?')
    confirmar = input('Digite S para apagar ou N para cancelar!').strip().upper()

    if confirmar == 'S':
        gastos.clear()
        receitas.clear()
    else:
        print('Nenhum dado foi apagado!')

def soma():
    total_receita = sum(receita['valor'] for receita in receitas)
    total_gastos = sum(gasto['valor'] for gasto in gastos)

    soma_financeira = total_receita - total_gastos
    print(f'Saldo em conta {soma_financeira:.2f}!')

def mostrar_menu():
    print('\n=====Organizador financeiro=====')
    print('1.Adicionar despesa.')
    print('2.Adicionar receita.')
    print('3.listar gastos.')
    print('4.Limpar operações')
    print('5. Soma financeira.')
    print('6.Sair')

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
            adicionar_receita()
        elif opcao == 3:
            listar_gastos()
        elif opcao == 4:
            limpar_operações()
        elif opcao == 5:
            soma()
        elif opcao == 6:
            print('saindo')
            break
        else:
            print('opção inválida')

carregar_dados()
executando_menu()


