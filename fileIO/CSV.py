import csv

students=[]



with open("names.csv","a") as file:
    writer=csv.writer(file)  
    writer.writerow(["bibek","jhapa"])

with open("names.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
         students.append({"name":row["name"], "house":row["house"]})

# using lambda funtion which doesn't need an external function for accessing key
for student in sorted(students,key=lambda student: student["name"],reverse=True):
    print(f"{student['name']} is in {student['house']}") 