# Taking Student Information 
import random

serail_no = random.randint(1,1000)
name = input("Enter Student Name: ")
age = input("Enter Student Age: ")
roll_no = input("Enter Student Roll Number: ")
branch = input("Enter Student Branch: ")
year = input("Enter Student Year: ")

with open("student_database.txt", "a") as f:
    f.write(f"Student Name: {name}")