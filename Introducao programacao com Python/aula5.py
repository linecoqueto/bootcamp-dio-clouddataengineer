##---------------------------##
## LISTA :: é mutável (consigo mudar os valores da lista)
##---------------------------##

lista = [11, 53, 5, 7]
lista_animal = ['cachorro', 'gato', 'efelante', 'lobo', 'arara']

#exibir lista
print(lista)

#exibir lista em determinada posição
print(lista_animal[1])

#percorrer toda a lista com o for
for x in lista_animal:
    print(x)

#realizar a soma dos valores da lista
soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

#outra forma para somar uma lista
print(sum(lista))

#buscar maior valor da lista
print(max(lista))

#buscar menor valor da lista
print(min(lista))

#buscar menor valor da lista de string (considera o alfabeto
print(min(lista_animal))

#buscar maior valor da lista de string (considera o alfabeto
print(max(lista_animal))

#buscar se já existe um  valor na lista
if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('não existe um gato na lista')

#multiplar uma lista
nova_lista = lista_animal * 3
print(nova_lista)

#incluir um valor na lista
if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista. Será incluído')
    lista_animal.append('lobo')
    print(lista_animal)

#excluir um valor - é retirado o ultimo valor da lista
lista_animal.pop()
print(lista_animal)

#excluir um valor de determinada posição
lista_animal.pop(1)
print(lista_animal)

#excluir um valor por nome
lista_animal.remove('efelante')
print(lista_animal)

#ordenar uma lista
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

#reverter uma lista
lista_animal.reverse()
print(lista_animal)

##---------------------------##
## TUPLAS :: é imutável
##---------------------------##

tupla = (1, 10, 12, 14)
print(tupla)

#consultar quantos registros tempos
tupla = (1, 10, 12, 14)
print(len(tupla))

##converter uma lista para tupla
tupla_animal = tuple(lista_animal)
print(type(lista_animal))
print(tupla_animal)

##converter uma tupla para lista
tupla = (1, 10, 12, 14)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)