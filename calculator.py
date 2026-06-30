class Calc:
    def getDivide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b
