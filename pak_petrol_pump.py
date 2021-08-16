import datetime
import time
import random 

# User Information

user_name = input("Enter Your Name: ")
car_name = input("Enter Your Car Name: ")
car_model = input("Enter Your Car Model: ")
car_number = input("Enter Your Car Number: ")
biometric = input("Are You Sure To Scan Your Fingerprint For Biometric Verification (Y/N): ")
if biometric == "Y" or "y":
    print("Place Your Finger On Fingerprint Scanner")
    print("Scanning.....")
    time.sleep(5)
    print("Your ID Is Confirmed, Go Ahead And Refule Your Car")
elif biometric != "Y" or "y":
    print("Sorry! We Can't Refule Your Car")
    quit

# Fuling Machine 

fuel_price = 100
print(f"Price of Perol is ${fuel_price}/L Today")
quantity = int(input("Enter The Quantity Of Petrol You Want To Refule (In Litres): "))
print("Please Wait While We Refule Your Car.....")
time.sleep(10)
print("Your Car Is Refule, Please Take This Ticket Number And Head To The Next Machine For Paying Your Amount")
ticket_number = random.randint(1, 100000)
print(f"Ticket Number: {ticket_number}")

# Cash And Reciept Machine

print("Welcome To Pak Petrol Pump, Hope You Enjoying The Day!")
ticket_number_verify = int(input("Enter Your Car Ticket Number Issued To You: "))
if ticket_number_verify == ticket_number:
    total_amount = quantity * fuel_price
    print(f"Your Ticket Number Is Confirmed, Please Pay The Total Amount of: ${total_amount}")
    biometric_1 = input("Are You Sure To Scan Your Fingerprint For Biometric Verification (Y/N): ")
    if biometric_1 == "Y" or "y":
        print("Place Your Finger On Fingerprint Scanner")
        print("Scanning.....")
        time.sleep(5)
        print(f"Your ID Is Confirmed, Making The Transaction Of.....${total_amount}")
    time.sleep(5)
    confirmed = input("Press 'P' On The Screen After You Pay: ")
    time.sleep(3)
    if confirmed == "P" or "p":
        print_reciept = (input("Your Amount Has Been Paid Successfully, Please Press '1' On The Screen To Print Reciept: "))
        if print_reciept == "1":
            print("Your Reciept Will Be Printed In 5 Seconds")
            time.sleep(5)
            print("Reciept Printed")
            reciept = print("_______________________PAYMENT RECIEPT______________________\n"
                            f"|Customer Name: {user_name}__________Car Name: {car_name}\n"
                            f"|Car Model: {car_model}__________Car Number: {car_number}\n"
                            f"|Ticket Number: {ticket_number}\n"
                            f"|Price Of Petrol: ${fuel_price}\L\n"
                            f"|Quantity Of Petrol: {quantity} Litres\n"
                            f"|Total Amount: ${total_amount}\n"
                            f"|Payment Method: Cash\n"
                            f"|Payment Date: {datetime.datetime.now()}\n"
                            "_____________________________________________________________\n"
                            "|Thanks For Visiting Pak Petrol Pump. Enjoy Your Day!")
            print(reciept)
elif ticket_number_verify != ticket_number:
    print("Sorry! Your Ticket Number Is Incorrect, We Couldn't Verify You")
    quit            
