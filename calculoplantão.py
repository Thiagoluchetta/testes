#irei fazer uma função que irá pegar todos os inputs primeiro e depois fazer o calculo, assim fica mais fácil de entender e de manter o código.
ResultadosPos1 = {

}
ResultadosPos2 = {

}
def capturar_resultadosPos1():
    try:
        ResultadosPos1['Vendas'] = float(input("Digite o valor total das vendas da Pos1: ").replace('.', '').replace(',', '.'))
        ResultadosPos1['Clientes'] = int(input("Digite o número de clientes da Pos1: "))    
        ResultadosPos1['Agregados'] = float(input("Digite o valor total dos agregados da Pos1: ").replace('.', '').replace(',', '.'))
        foodatached = []
        for i in range(1,4):
            entrada = input(f'Digite o {i} valor de food da Pos1: (Ou aperte enter para sair)')
            if entrada.strip() == '':
                break
            foodatached.append(int(entrada))
        ResultadosPos1['foodatached'] = foodatached
        print(f'Valores de foodatached armazenados: {foodatached}')

        IPTC = []
        for i in range(1,3):
            entrada = input(f'Digite a {i} entrada de IPTC da Pos1:')
            IPTC.append(int(entrada))
        ResultadosPos1['IPTC'] = IPTC
        print(f'Valores de IPTC armazenados: {IPTC}')
        ResultadosPos1['PC'] = int(input('A Pos1 Vendeu quantos pacotes de café?'))
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def capturar_resultadosPos2():  
    try:
        ResultadosPos2['Vendas'] = float(input("Digite o valor total das vendas da Pos2: ").replace('.', '').replace(',', '.'))
        ResultadosPos2['Clientes'] = int(input("Digite o número de clientes da Pos2: "))    
        ResultadosPos2['Agregados'] = float(input("Digite o valor total dos agregados da Pos2: ").replace('.', '').replace(',', '.'))
        foodatached = []
        for i in range(1,4):
            entrada = input(f'Digite o {i} valor de food da Pos2: (Ou aperte enter para sair)')
            if entrada.strip() == '':
                break
            foodatached.append(int(entrada))
        ResultadosPos2['foodatached'] = foodatached
        print(f'Valores de foodatached armazenados: {foodatached}')

        IPTC = []
        for i in range(1,3):
            entrada = input(f'Digite a {i} entrada de IPTC da Pos2:')
            IPTC.append(int(entrada))
        ResultadosPos2['IPTC'] = IPTC
        print(f'Valores de IPTC armazenados: {IPTC}')
        ResultadosPos2['PC'] = int(input('A Pos2 Vendeu quantos pacotes de café?'))
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")          

def calcular_TM():
    try:
        Vendas = ResultadosPos1['Vendas'] + ResultadosPos2['Vendas']
        Clientes = ResultadosPos1['Clientes'] + ResultadosPos2['Clientes']
        Agregados = ResultadosPos1['Agregados'] + ResultadosPos2['Agregados']
        foodatached = sum(ResultadosPos1['foodatached']) + sum(ResultadosPos2['foodatached'])
        IPTCpos1 = ResultadosPos1['IPTC'][0] - ResultadosPos1['IPTC'][1]
        IPTCpos2 = ResultadosPos2['IPTC'][0] - ResultadosPos2['IPTC'][1]

    # Cálculo dos resultados
        TM = Vendas / Clientes
        TC = Clientes
        Agregados = Agregados / Vendas * 100
        FA = foodatached / TC
        IPTC = TC / (IPTCpos1 + IPTCpos2)  

        print('-' * 30)
        print(f"\nResultados:"
          f"\nVendas: R$ {Vendas:.2f}"
          f"\nTC: {Clientes}"
          f"\nTM: {TM:.2f}"
          f"\nAgregados: {Agregados:.1f} %"
          f"\nFA: {FA} %"
          f"\nIPTC: {IPTC:.2f}")
        print("-" * 30)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

capturar_resultadosPos1()
capturar_resultadosPos2()
calcular_TM()