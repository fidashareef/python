
# Online Python - IDE, Editor, Compiler, Interpreter


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage
rect = Rectangle(10, 5)
print("Area of Rectangle:", rect.area())

