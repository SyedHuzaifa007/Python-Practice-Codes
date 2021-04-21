class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use The Person Class To Create An Object, And Then Execute The PrintName Method:

x = Person("Leonardo", "Di Vinci")
x.printname()