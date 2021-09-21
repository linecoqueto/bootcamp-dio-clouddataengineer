#interacao com usuário, convertendo a variável de entrada para inteiro
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

#operações matemáticas
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#print simples das operações realizadas
print('\n print simples das operacoes realizadas')
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)

#Função type para saber o tipo de uma variável
print('\n print dos tipos das variáveis')
print(type(soma))
print(type(divisao))

#converter uma variável com str, então conseguimos concatenar
print('\n converter variavel e concatenar')
print('soma: ' + str(divisao))

#arredondar uma variável
print('\n arredondar variavel')
print(int(divisao))

#converter uma string para inteiro
print('\n converter uma string para inteiro')
x = '1'
soma2 = int(x) + 1
print(soma2)

#uma outra forma de concatenar é usando o format
print('\n converter uma string para inteiro')
print('subtracao: {}. '.format(subtracao))

#exibindo mais de 1 na mesma linha
print('\n trabalhando com format para converter ')
print('subtracao: {}. Multiplicação: {} '.format(subtracao,
                                           multiplicacao))

#podemos dar um apelido/alias e com quebra de linha "\n"
print('Divisão: {div}. \nRestoDiv: {rest} '.format(div=divisao,
                                                 rest=resto))


