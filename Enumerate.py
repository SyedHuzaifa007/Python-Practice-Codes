# Simple Python Program To Practice Enumerate Function

l1 = ['eat', 'sleep', 'repeat']
s1 = 'geek'

# Creating Enumerate Objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type: ",type(obj1))
print(list(enumerate(l1)))

# Changing Start Index To 2 From 0
print(list(enumerate(s1,2)))