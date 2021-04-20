fruits = ["apple", "mango", "cherry", "kiwi", "banana"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Now With The List Comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Syntax: variable = [expression for item in iterable if condition == True]

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Getting A Little Advance
name = "Name"
a = [x for x in name]
b = [y for y in name]
print(a + b)

word = "Word"
a = [x*2 for x in word]
print(a)