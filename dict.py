# Example -1

user_info = {
     "name":"Alex",
     "age":50,
     "phone":12345678910,
     "address":"somewhere on the Earth"
}

# Accessing The Values From The Keys 
print(user_info["name"])
print(user_info["phone"])

# Updating The Values of Existing Keys
user_info["name"] = "John Wick"
print(user_info["name"])
print(user_info)
user_info["phone"] = 67786867856
print(user_info)

# Deleting The Value Pair From A Dictionary
del user_info["address"]
print(user_info)

# Adding A Key Value Pair In The Exsisting Dictionary
user_info["DOB"] = "01-01-1000"
print(user_info)








