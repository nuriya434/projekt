from student_class import Subject, Grade, Student, Teacher
import os
math = Subject("матем")
physics = Subject("физика")

student1 = Student("Фируза", 20, "S12345")
student1.add_grade(math, 68)
student1.add_grade(physics, 90)
student2 = Student("Алибек", 22, "S67890")
student2.add_grade(math, 88)
student2.add_grade(physics, 60)
teacher = Teacher("Гульжан К.", 35, "T7890")

print(student1)
print(student2)
print(teacher)

#
os.mkdir("otschet")
#
with open(".\otschet\grades", "a") as file:
    file.write(f"{student1.get_name()} оц по матем: {student1.get_grade(math)}\n")
    file.write(f"{student1.get_name()} оц по матем: {student1.get_grade(physics)}\n")
    file.write(f"{student2.get_name()} оц по матем: {student2.get_grade(math)}\n")
    file.write(f"{student2.get_name()} оц по матем: {student2.get_grade(physics)}")
    
#
with open(".\otschet\grades", "r") as file:
    print(file.read())
