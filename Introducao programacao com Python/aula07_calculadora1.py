##-------------------------------------------------------------##
## CONSTRUINDO MÉTODOS, FUNÇÕES E CLASSES EM PYTHON
##-------------------------------------------------------------##

#MÉTODO: É tudo que NÃO retorna valor -> chama-se "def" no python
#MÉTODO: util para reaproveitar código
#FUNÇÃO: É tudo que retorna valor

def soma(a, b):
    return a + b
print(soma(1,2))

def sub(a,b):
    return a - b
print(sub(3,2))

#CLASSE:
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def soma(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2

    def divis(self):
        return self.num1 / self.num2

if __name__ == '__main__':
    calculadora = Calculadora(10,2)
    print(calculadora.num1)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.multi())
    print(calculadora.divis())
