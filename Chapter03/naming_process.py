import multiprocessing
import time
from reversed_string import reverse_and_check_palindrome

def myFunc():
    name = multiprocessing.current_process().name
    print(f"Starting process name = {name}\n")

    strings = ["madam", "apple", "racecar", "python", "level"]
    print("Original strings:", strings)

    results = [reverse_and_check_palindrome(s) for s in strings]

    print("\nResults:")
    for s, (rev, is_pal) in zip(strings, results):
        print(f"{s} → {rev} | Palindrome: {is_pal}")

    time.sleep(2)
    print(f"Exiting process name = {name}\n")

def start_processes():
    process_with_name = multiprocessing.Process(
        name="Palindrome Process 1",
        target=myFunc
    )
    process_with_default_name = multiprocessing.Process(
        target=myFunc
    )

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()

if __name__ == "__main__":
    multiprocessing.freeze_support()  
    start_processes()
