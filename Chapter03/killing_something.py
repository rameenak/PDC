import multiprocessing
import time
from reversed_string import reverse_and_check_palindrome


def run_palindrome_task():
    print("Starting palindrome process")

    strings = ["madam", "apple", "racecar", "python", "level"]
    print("Original strings:", strings)

    results = [reverse_and_check_palindrome(s) for s in strings]

    print("\nResults:")
    for s, (rev, is_pal) in zip(strings, results):
        print(f"{s} → {rev} | Palindrome: {is_pal}")

    print("Finished palindrome process")

if __name__ == '__main__':
    p = multiprocessing.Process(target=run_palindrome_task)

    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    time.sleep(2)
    if p.is_alive():
        p.terminate()
        print('Process terminated:', p, p.is_alive())

    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)
