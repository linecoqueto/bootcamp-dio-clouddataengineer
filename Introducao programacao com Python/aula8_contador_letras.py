##vou devolver uma lista com a quantidade de letras de cada posição
def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        qtd = len(x)
        contador.append(qtd)
    return contador

if __name__ == '__main__':
    lista = list['cachorro','gato']
    print(contador_letras(lista))