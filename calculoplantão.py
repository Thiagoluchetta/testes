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
        for i in range(1,2):
            entrada = input(f'Digite a {i} entrada de IPTC da Pos2:')
            IPTC.append(int(entrada))
        ResultadosPos2['IPTC'] = IPTC
        print(f'Valores de IPTC armazenados: {IPTC}')
        ResultadosPos2['PC'] = int(input('A Pos2 Vendeu quantos pacotes de café?'))
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")          

def calcular_TM():
    try:
        # Soma de foodatached
        diferenca_foodatachedPos1 = sum(ResultadosPos1['foodatached'])
        diferenca_foodatachedPos2 = sum(ResultadosPos2['foodatached'])
        ResultadosPos1['foodatachedsomado'] = diferenca_foodatachedPos1
        ResultadosPos2['foodatachedsomado'] = diferenca_foodatachedPos2

        # Soma de IPTC
        iptcpos1 = sum(ResultadosPos1['IPTC'])
        iptcpos2 = sum(ResultadosPos2['IPTC'])
        ResultadosPos1['IPTCsomado'] = iptcpos1
        ResultadosPos2['IPTCsomado'] = iptcpos2

        # Loop para calcular resultados
        for pos, resultados in zip(['Pos1', 'Pos2'], [ResultadosPos1, ResultadosPos2]):
            Vendas = resultados['Vendas']
            Clientes = resultados['Clientes']
            Agregados = resultados['Agregados']
            PC = ResultadosPos1['PC'] + ResultadosPos2['PC']
            foodatached = ResultadosPos1['foodatachedsomado'] + ResultadosPos2['foodatachedsomado']

            # Verificar divisão por zero
            if Clientes == 0:
                print(f"Erro: O número de clientes na {pos} não pode ser zero.")
                return

            # Cálculo do TM
            TM = Vendas / Clientes
            TC = Clientes
            Agregados = Agregados / Vendas * 100
            FA = foodatached / TC
            IPTC = iptcpos1 - iptcpos2

            # Exibição dos resultados
            print('-' * 30)
            print(f"\nResultados da {pos}:"
                  f"\nVendas: R$ {Vendas:.2f}"
                  f"\nTC: {Clientes}"
                  f"\nTM: {TM:.2f}"
                  f"\nAgregados: {Agregados:.1f} %"
                  f"\nFA: {FA:.2f} %"
                  f"\nIPTC: {IPTC:.2f}"
                  f"\nPC: {PC}")
            print("-" * 30)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

capturar_resultadosPos1()
capturar_resultadosPos2()
calcular_TM()