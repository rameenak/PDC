import socket

s = socket.socket()
host = socket.gethostname()
port = 60000

s.connect((host, port))

# Get input string from user
string_to_send = input("Enter a string to check: ")
s.send(string_to_send.encode())

# Receive response
data = s.recv(1024).decode()
print("Server response:", data)

s.close()
