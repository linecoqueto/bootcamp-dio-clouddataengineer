# Desafios
# Crie um programa que leia um número e mostre os números pares até esse número, inclusiveele mesmo.
#
# Entrada
# Você receberá 1 valor inteiro N, onde N > 0.
#
# Saída
# Exiba todos os números pares até o valor de entrada, sendo um em cada linha.

entrada = int(input())
div = entrada
for i in range(1, entrada+1):
    resto = i % 2
    #print('valor: {}'.format(i) + " resto: {}".format(resto))
    if resto == 0:
        print(i)