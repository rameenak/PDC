import socket
from reversedstring import reverse_and_check_palindrome

port = 60000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)
print('Server listening on port', port)

try:
    while True:
        conn, addr = s.accept()
        print('Got connection from', addr)

        data = conn.recv(1024).decode()
        if not data:
            conn.close()
            continue

        print('Server received:', data)

        reversed_s, is_palindrome = reverse_and_check_palindrome(data)
        response = f"Reversed: {reversed_s} | Palindrome: {is_palindrome}"
        conn.send(response.encode())
        conn.close()

except KeyboardInterrupt:
    print("\nServer shutting down gracefully...")
    s.close()
