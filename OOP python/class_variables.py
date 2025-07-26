class Student:

    class_year=2024
    num_students=0

    def __init__(self, name, age):
        self.name=name
        self.age=age
        Student.num_students+=1


student1=Student("Bibek", 20)
student2=Student("patric",25)

print(f"{student1.name}, {student1.age},{Student.class_year}")
print(f"{student2.name}, {student2.age}, {Student.class_year}")

print(f"my graduating class of {Student.class_year} has {Student.num_students} students ")
print(student1.name)
print(student2.name)


