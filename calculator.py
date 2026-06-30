class Calc:
    def getDivide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

    def getSumSum(self, a, b, c):
        return a + b + c
    def getMinus(self, a, b):
        return a - b
