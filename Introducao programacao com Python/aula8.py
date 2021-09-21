##-------------------------------------------------------------##
## Lidando com módulos, importação de classes, métodos e construção
## de funções anônimas (lambda)
##-------------------------------------------------------------##

## MÓDULO : São os arquivos .py, e os módulos podem interagir entre eles

## executar no terminal ::
# >>> import aula_7_televisao
# >>> televisao = aula7_televisao.Televisao()
# >>> televisao.ligada
# False
# >>> televisao.power()
# >>> televisao.ligada
# True

## if __name__ == '__main__' :: está referenciando ao proprio arquivo

from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5,10)
    print(calculadora.soma())
    lista = ['cachorro','gato','elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {}'.format(total_letras))