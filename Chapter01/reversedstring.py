

def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    return reversed_s, is_palindrome

if __name__ == "__main__":
    strings = ["madam", "apple", "racecar", "python", "level"]
    print("Original strings:", strings)

    results = [reverse_and_check_palindrome(s) for s in strings]

    print("\nResults:")
    for s, (rev, is_pal) in zip(strings, results):
        print(f"{s} → {rev} | Palindrome: {is_pal}")
