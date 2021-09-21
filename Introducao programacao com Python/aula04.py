### TRABALHANDO COM REPETIÇÃO

##repetição simples até o 100 : FOR/RANGE
for x in range(100):
    print(x)

##repetição simples de 20 a 100
for x in range(20,100):
    print(x)

##verificar os numeros primos
a = int(input('Entre com o número: '))
div = 0
for x in range(1, a+1):
     resto = a % x #fazendo a divisão e pegando o resto
     print(a, resto) #vai imprimir os dois valores das variáveis
     if resto == 0: #se for igual a zero ele é primo
        div += 1

if div == 2: #se ele foi dividido por 0 e por ele mesmo ele é um num primo
    print('Número {} é primo'.format(a))
else:
    print('Número {} não é primo'.format(a))


##verificar os numeros primos de 0 a 100
a = int(input('Entre com um valor: '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1):
         resto = num % x #fazendo a divisão e pegando o resto
         if resto == 0: #se for igual a zero ele é primo
            div += 1
    if div == 2: #se ele foi dividido por 0 e por ele mesmo ele é um num primo
        print('Número {} é primo'.format(num))


##Forçar uma repetição até que ela seja verdadeira :: WHILE
a = 0
while a <= 10:
    print(a)
    a += 1


##Solicitar notas, fazer média e verificar se nota foi digitada corretamente
nota1 = int(input('Primeiro Bimestre: '))
while nota1 > 10:
    nota1 = int(input('Nota inválida. \nEntre com a nota correta Primeiro Bimestre: '))
nota2 = int(input('Segundo Bimestre: '))
while nota2 > 10:
    nota2 = int(input('Nota inválida. \nEntre com a nota correta Segundo Bimestre: '))
nota3 = int(input('Terceiro Bimestre: '))
while nota3 > 10:
    nota3 = int(input('Nota inválida. \nEntre com a nota correta Terceiro Bimestre: '))
nota4 = int(input('Quarto Bimestre: '))
while nota4 > 10:
    nota4 = int(input('Nota inválida. \nEntre com a nota correta Quarto Bimestre: '))

media = (nota1+nota2+nota3+nota4) / 4
print('media: {}'.format(media))
