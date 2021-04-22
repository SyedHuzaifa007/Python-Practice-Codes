class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
    def camelcase(self):
        print(self.firstname.title(), self.lastname.title())

# Use The Person Class To Create An Object, And Then Execute The PrintName Method:

x = Person("Leonardo", "Di Vinci")
x.printname()
y = Person("Adolf", "Hitler")
y.printname()
z = Person("Kevin", "Mitnick")
z.printname()