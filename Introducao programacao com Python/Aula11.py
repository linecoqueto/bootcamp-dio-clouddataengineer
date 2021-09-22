##-------------------------------------------------------------##
## EXCEÇÕES CUSTOMIZADAS COM TRY, EXCEPT, ELSE E FINALLY
##-------------------------------------------------------------##

lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

    #x = a
except ZeroDivisionError:
    print('Não é possível realizar a divisão!')
except IndexError:
    print('Erro ao acessar um indice invalido da lista!')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção!!')
finally:
    print('sempre executa!')
    arquivo.close()
    print('Fecha arquivo!')