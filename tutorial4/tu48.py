
# Online Python - IDE, Editor, Compiler, Interpreter
class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: {self.cost}")

# Example usage
book = Book()
book.get_details("Python Basics", "John Doe", 350)
book.print_details()






