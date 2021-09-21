
class Calculadora:

    def soma(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def divis(self, num1, num2):
        return num1 / num2

calculadora = Calculadora()
print(calculadora.soma(10,2))
print(calculadora.sub(10,2))
print(calculadora.multi(10,2))
print(calculadora.divis(10,2))
