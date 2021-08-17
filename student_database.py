# Taking Student Information 

serail_no = input("Enter Serial Number: ")
name = input("Enter Student Name: ")
age = input("Enter Student Age: ")
roll_no = input("Enter Student Roll Number: ")
branch = input("Enter Student Branch: ")
year = input("Enter Student Year: ")

# Writing Student Information In A Text File

with open(f"{name}.txt", "a") as f:
    f.write(f"Serial Number: {serail_no}")
    f.write(f"\nStudent Name: {name}")
    f.write(f"\nStudent Age: {age}")
    f.write(f"\nStudent Roll Number: {roll_no}")
    f.write(f"\nStudent Branch: {branch}")
    f.write(f"\nStudent Year: {year}")
    f.write(f"\n\n")
    