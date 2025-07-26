# class Student: 
#     ...
# def main():
#     student =get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student=Student()
#     student.name=input("enter name: ")
#     student.house=input("enter house: ")
#     return student

# if __name__=="__main__":
#     main()


class Student: 
    def __init__(self, name, house):
        self.name=name
        self.house=house


def main():
    student =get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    
    name=input("enter name: ")
    house=input("enter house: ")
    return Student(name,house)

if __name__=="__main__":
    main()

