# target_port = 5000

def identify_service(port):
    if port == 22:
        return "SSH"
    elif port == 80:
        return "HTTP"
    elif port == 443 :
        return "HTTPS"
    else:
        return "Unkown Service"
# print(identify_service(target_port))
print(identify_service(22))
print(identify_service(80))
print(identify_service(443))
print(identify_service(5000))