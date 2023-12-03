class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"Name: {self._name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = {}

    def __str__(self):
        return f"Student ID: {self.student_id}, {Person.__str__(self)}"

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_grade(self, subject):
        return self.grades.get(subject, None)

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, {Person.__str__(self)}"

class Subject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Subject: {self.name}"

class Grade:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Grade: {self.value}"