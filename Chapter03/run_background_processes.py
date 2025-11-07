import multiprocessing
import time
from reversed_string import reverse_and_check_palindrome  # ✅ import your function


def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    strings = ["madam", "apple", "racecar", "python", "level"]

    # Background process checks first half
    # Non-background process checks the second half
    if name == 'background_process':
        for s in strings[:3]:
            rev, is_pal = reverse_and_check_palindrome(s)
            print(f"{name}: {s} → {rev} | Palindrome: {is_pal}")
            time.sleep(0.5)
    else:
        for s in strings[3:]:
            rev, is_pal = reverse_and_check_palindrome(s)
            print(f"{name}: {s} → {rev} | Palindrome: {is_pal}")
            time.sleep(0.5)

    print(f"Exiting {name}\n")


if __name__ == '__main__':
    start_time = time.time()  # Start timer

    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True  # Daemon process

    no_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    no_background_process.daemon = False  # Regular process

    background_process.start()
    no_background_process.start()

    # Wait for the non-daemon process to finish
    no_background_process.join()

    # End timing
    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Main process finished. ⏱️ Ended at {elapsed:.2f}s\n")
