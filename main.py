
jáSouProgramador = "Ainda não"

def fazerperguntas():
    print("Você já é um programador?")

    estudos = input("Já estudou por 6 meses focados? (sim/não) ")
    treino = input("Já resolveu problemas de lógica? (sim/não) ")
    decisão = input("Já decidiu a área que quer seguir? (sim/não) ")
    portffolio = input("Já montou projetos? (sim/não) ")

    if estudos == 'sim' and treino == 'sim' and decisão == 'sim' and portffolio == 'sim':
        print("Sim, você é um programador")
    elif (estudos == 'sim' and treino == 'sim') or (decisão == 'não' or portffolio == 'não'):
        print("Já sabe das coisas, agora corra atrás!")
    else:
        print("Você AINDA não é um programador, vai com foco!")

continuar = "sim"
while continuar.lower() == "sim":
    fazerperguntas()
    continuar = input("Você quer continuar? (sim/não) ")


