import csv

name=input("Enter student's name: ")
house=input("enter student's house: ")
age=int(input("Enter student's age: "))

with open("students.csv","a") as file: 
    writer=csv.DictWriter(file,fieldnames=["name", "house","age"])
    