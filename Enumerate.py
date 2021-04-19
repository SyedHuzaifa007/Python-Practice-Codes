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

# Using Enumerate Function In Loops

# Printing The Tuples In The Objects Directly
for ele in enumerate(l1):
    print(ele)

# Changing Index And Printing Searately
for count, ele in enumerate(l1, 100):
    print(count, ele)