from __future__ import print_function
import Pyro4

# Connect to first node in the chain
obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")

# Test chain message passing
print("Chain message test:")
result = obj.process(["hello"])
print("Result =", result)

# Test reversed string and palindrome
s = input("Enter a string to reverse and check palindrome: ").strip()
reversed_s, is_palindrome = obj.reverse_and_check_palindrome(s)
print(f"Original string: {s}")
print(f"Reversed string: {reversed_s}")
print(f"Palindrome: {is_palindrome}")
