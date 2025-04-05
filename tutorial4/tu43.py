
# Online Python - IDE, Editor, Compiler, Interpreter


class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"Model: {self.model}, Year: {self.year}, Price: {self.price}")

# Example usage
car1 = Car("Toyota", 2022, 20000)
car2 = Car("Honda", 2023, 25000)
car1.cost()
car2.cost()


