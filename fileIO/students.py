# with open("names.csv") as file:
#     for line in file:
#        row= line.rstrip().split(",")
#        print(f"{row[0]} is in {row[1]}")


students=[]

with open("names.csv") as file:
    for line in file:
       name, house= line.rstrip().split(",")
       student={"name":name,"house":house}
       students.append(student)

def getName(student):
    return student["name"]
       
# for student in sorted(students,key=getName):
#     print(f"{student['name']} is in {student['house']}") 


# using lambda funtion which doesn't need an external function for accessing key
for student in sorted(students,key=lambda student: student["name"],reverse=True):
    print(f"{student['name']} is in {student['house']}")  
       