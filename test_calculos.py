import pytest
from resultados import calcular_TM_com_dados

def test_calculo_TM():
    dados1 = {
        'Vendas': 1000.0,
        'Clientes': 50,
        'Agregados': 200.0,
        'foodatached': [1, 2],
        'IPTC': [30, 10]
    }
    dados2 = {
        'Vendas': 2000.0,
        'Clientes': 100,
        'Agregados': 400.0,
        'foodatached': [2, 2],
        'IPTC': [40, 20]
    }

    resultado = calcular_TM_com_dados(dados1, dados2)

    # Verificações (asserções)
    assert resultado['Vendas'] == 3000.0
    assert round(resultado['TM'], 2) == 20.00
    assert resultado['TC'] == 150
    assert round(resultado['Agregados'], 1) == 20.0
    assert round(resultado['FA'], 2) == 0.05  # Aqui você arredonda para 2 casas decimais
    assert round(resultado['IPTC'], 2) == 3.75
