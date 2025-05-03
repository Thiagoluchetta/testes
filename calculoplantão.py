def calcular_TM():
    try: 
        VendasPos1 = float(input("Digite o valor total das vendas da Pos1: "))
        VendasPos2 = float(input("Digite o valor total das vendas da Pos2: "))

        ClientePos1 = int(input("Digite o número de clientes da Pos1: "))
        ClientePos2 = int(input("Digite o número de clientes da Pos2: "))

        VendasTotal = VendasPos1 + VendasPos2
        ClientesTotal = ClientePos1 + ClientePos2

        TM = VendasTotal / ClientesTotal
        print(f'\nO Valor final das vendas é {VendasTotal:.2f}')
        print(f'\nO número total de clientes é {ClientesTotal}')
        print(f"\nO Ticket Médio é: R$ {TM:.2f}")
    except ValueError:
        print("Digite um número válido")
    except ZeroDivisionError:
        print("O número de clientes não pode ser zero.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
calcular_TM