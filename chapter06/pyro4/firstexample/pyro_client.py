import Pyro4

# Connect to the server
server = Pyro4.Proxy("PYRONAME:server")    

# Ask for user name
name = input("What is your name? ").strip()
print(server.welcomeMessage(name))

# Ask user for a string to reverse and check palindrome
s = input("Enter a string to reverse and check palindrome: ").strip()
reversed_s, is_palindrome = server.reverse_and_check_palindrome(s)

print(f"Original string: {s}")
print(f"Reversed string: {reversed_s}")
print(f"Palindrome: {is_palindrome}")
