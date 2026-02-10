correct_password = "secret123"

pswd_list =["password","123456","admin","secret123","football"]

for password in pswd_list:
    print("Testing password: " + password)
    
    if password == correct_password:
        print("MATCH FOUND! Password is: " + password)
        break
    else: 
        print("Wrong password")