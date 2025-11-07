import multiprocessing
import time
from reversed_string import reverse_and_check_palindrome  # ✅ import your function

def foo():
    name = multiprocessing.current_process().name
    print(f"\nStarting {name}\n")

    if name == 'background_process':
        # Background process uses first set of strings
        strings = ["madam", "apple", "racecar", "python", "level"]
    else:
        strings = ["noon", "banana", "rotor", "civic", "deed"]

    results = [reverse_and_check_palindrome(s) for s in strings]

    for s, (rev, is_pal) in zip(strings, results):
        print(f"{name}: {s} → {rev} | Palindrome: {is_pal}")

    time.sleep(1)
    print(f"Exiting {name}\n")

if __name__ == '__main__':
    multiprocessing.freeze_support()  # ✅ for Windows compatibility

    # Create background process
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = False  # ✅ explicitly not daemon

    # Create non-background process
    no_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    no_background_process.daemon = False

    # Start both processes
    background_process.start()
    no_background_process.start()

    # Wait for them to finish
    background_process.join()
    no_background_process.join()
