import socket

hostnm = socket.gethostname()
my_ip = socket.gethostbyname(hostnm)

print("Ip Adress =  "+my_ip)