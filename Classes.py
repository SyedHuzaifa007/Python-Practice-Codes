# Classes Example-1

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
        # Print Name Function
    def printname(self):
        print(self.firstname, self.lastname)
        # Title Case Function
    def camelcase(self):
        print(self.firstname.title(), self.lastname.title())

# Use The Person Class To Create An Object, And Then Execute The PrintName Method:

x = Person("leonardo", "di vinci")
x.printname()
x.camelcase()
y = Person("adolf", "hitler")
y.printname()
y.camelcase()
z = Person("kevin", "mitnick")
z.printname()
z.camelcase()
a = Person("elon", "musk")
a.printname()
a.camelcase()

# Example-2

class Patient():
    def __init__(self, lname):
        self.lname = lname  

p_1 = Patient("Doe")
print(p_1.lname)

class Student():
    def __init__(self, fname, lname):
        self.fname = fname