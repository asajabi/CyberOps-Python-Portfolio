correct_username = "admin"

correct_password = "cyber2026"

user = str(input("Please type your username: "))

pswd = str(input("Please type your correct password: "))

if user == correct_username and pswd == correct_password:
    print ("Access Granted. Welcome to the System.")
else:
    print("Access Denied. Incorrect credentials.")