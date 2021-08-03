# Example-1

condition = input("What is the condition of the donut? ")
filling = input("What is the filling of the donut? ")

donut_price = 0

if condition == "fresh":
    if filling == "chocolate":
        donut_price = 10
    elif filling == "jam":
        donut_price = 5
    elif filling == "plain":
        donut_price = 3
    else:
        print("Sorry, we don't have this kind of filling")
elif condition == "day old":
    if filling == "chocolate":
        donut_price = 8 
    elif filling == "jam":
        donut_price = 4
    elif filling == "plain":
        donut_price = 2
    else:
        print("Sorry, we don't have this kind of filling")
else:   
    print("Sorry, we don't have this kind of condition")    


print("The price of the donut is $" + str(donut_price)) 

# Example-2

SAT = input("What is the SAT score? ")
GPA = input("What is the GPA? ")
alumni = input("Are your parents an alumni? ")

avg = 10
score = 2
if SAT >= avg and GPA >= score:
    if alumni == "yes":
        print("You are eligible for the full-time program")
else:
    print("You are not eligible for the full-time program")
