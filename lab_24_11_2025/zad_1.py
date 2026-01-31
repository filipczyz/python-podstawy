
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def is_passed(self):
        if len(self.marks) == 0:
            return False
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50

student_zdal = Student("Ania", [60, 70, 80])
wynik1 = student_zdal.is_passed()
print(f"Czy {student_zdal.name} zdała? {wynik1}")

student_oblal = Student("Tomek", [30, 40, 50])
wynik2 = student_oblal.is_passed()
print(f"Czy {student_oblal.name} zdał? {wynik2}")
