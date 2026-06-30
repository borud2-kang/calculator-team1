class Calc:

    def __init__(self):
        pass

    def getGop(self, a : int ,b : int) -> int:
        return a * b
    def getDivide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

    def getSumSum(self, a, b, c):
        return a + b + c
    def __init__(self):
        pass

    def getSum(self, a, b):
        return a + b

    def getZegop(self, a):
        return a * a
      
    def getMinus(self, a, b):
        return a - b
