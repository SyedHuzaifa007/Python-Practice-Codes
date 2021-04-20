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