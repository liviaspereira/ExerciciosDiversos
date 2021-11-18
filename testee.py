def palavra_aumentada(palavra):

    retorno = ''
    for letra in palavra:
        retorno += letra.upper()
    return retorno 

print(palavra_aumentada("palavra"))
