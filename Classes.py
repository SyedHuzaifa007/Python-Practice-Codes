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