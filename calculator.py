import math


class Calculator:
    def addition(self, x, y):
        return float(x) + float(y)

    def subtraction(self, x, y):
        return float(x) - float(y)

    def multiplication(self, x, y):
        return float(x) * float(y)

    def division(self, x, y):
        if int(y) is not 0:
            return float(x) / float(y)
        else:
            return 'error, divisor y can not be zero'

    def squareRoot(self, x):
        if int(x) > 0:
            return float(math.sqrt(x))
        else:
            return 'error, input will result in imaginary number'

    def squared(self, x):
        return float(x**2)
