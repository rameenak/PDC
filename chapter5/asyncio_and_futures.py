import asyncio
import sys

# Palindrome function
def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    return reversed_s, is_palindrome

# Async coroutines
async def first_coroutine(num):
    count = sum(range(1, num + 1))
    await asyncio.sleep(4)
    return f'First coroutine (sum of N ints) result = {count}'

async def second_coroutine(num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    return f'Second coroutine (factorial) result = {count}'

async def palindrome_coroutine(strings):
    results = [reverse_and_check_palindrome(s) for s in strings]
    await asyncio.sleep(2)
    output = "\n".join(f"{s} → {rev} | Palindrome: {is_pal}" for s, (rev, is_pal) in zip(strings, results))
    return output

# Main async function
async def main(num1, num2, strings):
    # Run all coroutines concurrently
    results = await asyncio.gather(
        first_coroutine(num1),
        second_coroutine(num2),
        palindrome_coroutine(strings)
    )

    # Print results
    for result in results:
        print(result)

if __name__ == '__main__':
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    strings = ["madam", "apple", "racecar", "python", "level"]

    asyncio.run(main(num1, num2, strings))
