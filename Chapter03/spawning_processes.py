# Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing
from reversed_string import reverse_and_check_palindrome  

def myFunc(i):
    print(f'\nProcess number: {i} started')

    # Prepare some strings based on process number
    strings = ["madam", "apple", "racecar", "python", "level"][:i] or ["madam"]

    # Apply palindrome checking
    results = [reverse_and_check_palindrome(s) for s in strings]

    # Display results
    for s, (rev, is_pal) in zip(strings, results):
        print(f'Process {i}: {s} → {rev} | Palindrome: {is_pal}')

    print(f'Process number: {i} finished\n')


if __name__ == '__main__':
    multiprocessing.freeze_support()  # ✅ for Windows safety

    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()  # waits for each process to finish before starting the next
