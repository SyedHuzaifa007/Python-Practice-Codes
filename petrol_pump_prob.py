import datetime
# User Information
user_name = input("Enter Your Name: ")
car_name = input("Enter Your Car Name: ")
car_model = input("Enter Your Car Model: ")
car_number = input("Enter Your Car Number: ")
biometric = input("Are You Sure To Scan Your Fingerprint For Biometric (Y/N): ")
if biometric == "Y" or "y":
    print("Place Your Finger On Fingerprint Scanner")
    print("Scannig.....")
    print("Your ID Is Confirmed, Go Ahead And Refule Your Car")
elif biometric != "Y" or "y":
    print("Sorry! We Can't Refule Your Car")
print("Hello")
