
# Online Python - IDE, Editor, Compiler, Interpreter
class RECTANGLE:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return (center_x, center_y)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Example usage
rect = RECTANGLE(10, 20, 0, 0)
print("Center:", rect.center())
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())







