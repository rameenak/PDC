import asyncio
import random

# Your palindrome function
def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    return reversed_s, is_palindrome

# Strings to check
strings = ["madam", "apple", "racecar", "python", "level"]

# Async versions of tasks
async def task_A(end_time, loop):
    print("task_A called")
    await asyncio.sleep(random.randint(0, 5))  # non-blocking sleep

    # Run palindrome check as part of task_A
    results = [reverse_and_check_palindrome(s) for s in strings]
    print("\nPalindrome Check in task_A:")
    for s, (rev, is_pal) in zip(strings, results):
        print(f"{s} → {rev} | Palindrome: {is_pal}")

    if loop.time() + 1.0 < end_time:
        loop.call_later(1, lambda: asyncio.create_task(task_B(end_time, loop)))
    else:
        loop.stop()

async def task_B(end_time, loop):
    print("task_B called")
    await asyncio.sleep(random.randint(0, 5))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, lambda: asyncio.create_task(task_C(end_time, loop)))
    else:
        loop.stop()

async def task_C(end_time, loop):
    print("task_C called")
    await asyncio.sleep(random.randint(0, 5))
    if loop.time() + 1.0 < end_time:
        loop.call_later(1, lambda: asyncio.create_task(task_A(end_time, loop)))
    else:
        loop.stop()

# Run the loop
loop = asyncio.get_event_loop()
end_loop = loop.time() + 60
loop.call_soon(lambda: asyncio.create_task(task_A(end_loop, loop)))
loop.run_forever()
loop.close()
