def sentencas_dancantes(palavra):
    maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minuscula = 'abcdefghijklmnopqrstauvwxyz'
    retorno = ''

    retorno = palavra[0]

    for numero in range(1, len(palavra)):
        if retorno[numero - 1] in maiuscula:
            retorno += palavra[numero].lower()
        if retorno[numero - 1] in minuscula:
            retorno += palavra[numero].upper()
    return retorno

print(sentencas_dancantes("ABcd"))

