students=[
    {"name":"hermoine", "house":"griffindor", "patronous":" Otter"},
    {"name":"harry", "house":"griffindor", "patronous":"stag"},
    {"name":"Draco", "house":"slytherin", "patronous":None}
]

for student in students:
    if  student["name"]=="harry":
        print(student["house"])
