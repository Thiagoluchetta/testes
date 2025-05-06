def calcular_TM_com_dados(dados1, dados2):
    try:
        Vendas = dados1['Vendas'] + dados2['Vendas']
        Clientes = dados1['Clientes'] + dados2['Clientes']
        Agregados = dados1['Agregados'] + dados2['Agregados']
        foodatached = sum(dados1['foodatached']) + sum(dados2['foodatached'])
        IPTCpos1 = dados1['IPTC'][0] - dados1['IPTC'][1]
        IPTCpos2 = dados2['IPTC'][0] - dados2['IPTC'][1]

        # Cálculo dos resultados
        TM = Vendas / Clientes
        TC = Clientes
        Agregados = Agregados / Vendas * 100
        FA = foodatached / TC
        IPTC = TC / (IPTCpos1 + IPTCpos2)

        # Retorna os resultados como um dicionário
        return {
            'Vendas': Vendas,
            'TM': TM,
            'TC': TC,
            'Agregados': Agregados,
            'FA': FA,
            'IPTC': IPTC
        }

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None
