class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 4))
print(calc.add(5, 4, 5))
