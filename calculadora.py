historico = []

def calculadora (n1,n2,operador):
    if operador == '+':
        resultado = n1 + n2
    elif operador == '-':
        resultado = n1 - n2
    elif operador == '*':
        resultado = n1 * n2
    elif operador == '/':
        if n2 != 0:
            resultado = n1/n2
        else:
            print('erro, divisão por zero')
        return None
    else:
        print('Operador inválido!')
        return None

    operacao = f"{n1} {operador} {n2} = {resultado}"
    historico.append(operacao)
    return resultado

while True:
        operador = input("Digite o tipo de calculo (+,-, *, /) ou sair para finalizar, limpar para remover histórico ")
        if operador.lower() == 'sair':
            print('Finalizando a calculadora, até mais!')
            break #Finaliza o loop
        if operador.lower() == 'limpar':
            historico.clear()
            print ('Histórico limpo')
            continue #Volta para o começo do loop

        while True:
            try:
                n1 = float(input('Digite o primeiro número.'))
                break
            except:
                print('Número invalido, tente novamente!')
        while True:
            try:
                n2 = float(input('Digite o segundo número.'))
                break
            except:
                print('Número invalido, tente novamente!')

        calculo = calculadora(n1, n2, operador) 
        print(f'{n1} {operador} {n2} = {calculo} ')

print('\nHistórico de Operações!')
for item in historico:
    print(item) 


