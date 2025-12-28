"""Asyncio: Run multiple STRING tasks in parallel(reverse string, palindrome check, letter count)"""

import asyncio


def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    return reversed_s, is_palindrome


def count_letters(s):
    return len(s)


async def reverse_string_task(strings):
    for s in strings:
        await asyncio.sleep(1)
        rev, is_pal = reverse_and_check_palindrome(s)
        print(f"[Reverse Task] {s} → {rev} | Palindrome: {is_pal}")


async def letter_count_task(strings):
    for s in strings:
        await asyncio.sleep(1)
        count = count_letters(s)
        print(f"[Count Task] '{s}' has {count} letters")


async def main():
    strings = ["madam", "apple", "racecar", "python", "level"]

    tasks = [
        asyncio.create_task(reverse_string_task(strings)),
        asyncio.create_task(letter_count_task(strings))
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
