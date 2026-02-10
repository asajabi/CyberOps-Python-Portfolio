def identify_service(port):
        if port == 22:
            return "SSH"
        elif port == 80:
            return "HTTP"
        elif port == 443 :
            return "HTTPS"
        elif port == 21 :
            return "FTP"
        elif port == 8080 :
            return "TCP"
        else:
            return "Unkown Service"
open_ports = [80,22,5000,21,8080,443]
for port in open_ports:
    service = identify_service(port)
        
    print("Port " + str(port) + " is running " + service)

