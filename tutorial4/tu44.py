
# Online Python - IDE, Editor, Compiler, Interpreter
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def dataprint(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}")

# Example usage
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)
s1.dataprint()
s2.dataprint()


