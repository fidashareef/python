
# Online Python - IDE, Editor, Compiler, Interpreter
class StudentMarks:
    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def computeTotal(self):
        return self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll No: {self.rollno}, Marks: {self.mark1}, {self.mark2}, Total: {self.computeTotal()}")

# Example usage
stud = StudentMarks()
stud.readData(123, 85, 90)
stud.printDetails()





