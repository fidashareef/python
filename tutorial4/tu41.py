
# Online Python - IDE, Editor, Compiler, Interpreter

class Arith:
    def read(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b if self.b != 0 else 'Division by zero error'

# Example usage
arith = Arith()
arith.read(10, 5)
print("Sum:", arith.add())
