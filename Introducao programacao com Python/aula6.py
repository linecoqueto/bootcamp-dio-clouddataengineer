##-------------------------------------------------------------##
## CONJUNTOS { } :: não permite duplicidade
##-------------------------------------------------------------##

#criando um conjunto
conjunto = {1, 2, 3, 4}
print(type(conjunto))

#adicionar um elemento ao conjunto
conjunto = {1, 2, 3, 4}
conjunto.add(5)
print(conjunto)

#adicionar um elemento do conjunto
conjunto = {1, 2, 3, 4}
conjunto.discard(2)
print(conjunto)

#criando conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

##união de dois conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

##intersecção dos conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

##diferenca dos conjuntos
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

##diferenca simetrica
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

##pertinencia
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b) #todos os elementos de A encontra-se no B
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a) #todos os elementos de B encontra-se no A
print('B é superconjunto de A: {}'.format(conjunto_superset))

##converter uma lista para um conjunto
lista = ['cachorro', 'gato', 'gato', 'elefante', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)