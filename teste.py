def acharMinimoDeDias(duracoes):
    dias = 0
    duracoes.sort(reverse=True)
    while len(duracoes) > 0:
        soma = 0
        lista_remocao = []
        for duracao in duracoes:
            if duracao + soma <= 3:
                soma += duracao
                lista_remocao.append(duracao)
        for i in lista_remocao:
            duracoes.remove(i)
        dias += 1
    return dias


if __name__ == '__main__':

    f = open("input002.txt", "r")
    lines = f.readlines()
    #duracoes_count = int(input().strip())
    duracoes_count = lines[0].strip()

    duracoes = []

    for i in lines[1:]:
        duracoes_item = float(i.strip())
        duracoes.append(duracoes_item)

    result = acharMinimoDeDias(duracoes)

    print(str(result) + '\n')



