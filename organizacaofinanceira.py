#Construção de algoritmo para estudo de lógica de programação e python
#Servirá como um app de organização financeira
#irei adicionar novas funções conformo aprendo, evoluindo o código e trazendo novidades!

gastos = []

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


adicionar_gastos()
    