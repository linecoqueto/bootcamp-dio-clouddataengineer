##-------------------------------------------------------------##
## FUNÇÃO LAMBDA :: função anônima
## São eficientes com funções que podemos resolver em apenas 1 linha
## coisas mais complexas não vamos fazer com o lambda, apenas coisas simples
##-------------------------------------------------------------##

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro','gato','efelefante']
contador_letras(lista_animais)
print(contador_letras(lista_animais))

###############

soma = lambda a, b: a + b
subtracao = lambda a,b : a - b

print(soma(5,10))
print(subtracao(10,5))

###############

calculadora = {
    'soma': lambda a, b: a+b,
    'subtracao': lambda a, b: a-b,
    'multiplicacao': lambda a, b: a*b,
    'divisao': lambda a, b: a/b
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicacao é: {}'.format(multiplicacao(10, 5)))
