'''Multiplicar duas Matrizes'''

def multiplicar_matriz(matriz1, matriz2):
    linha = len(matriz1)
    coluna = len(matriz1[0])
    matriz3 = []

    for n in range(linha):
        matriz3.append([])
        for j in range(coluna):
            matriz3[n].append(0)

    for x in range(linha):
        for y in range(coluna):
            matriz3[x][y] = (matriz1[x][y] * matriz2[y][x]) + (matriz1[x][y] * matriz2[y][x])
    return matriz3

print(multiplicar_matriz([[2, 3], [4,6]], [[1,3,0],[2,1, 1]]))
