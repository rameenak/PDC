## Code 2: Reverse string and check palindrome 
import multiprocessing
import time

def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    return (s, reversed_s, is_palindrome)

if __name__ == "__main__":
    base_words = ["madam", "apple", "racecar", "python", "level"]
    sizes = [5, 10, 15, 50]

    for size in sizes:
        # Repeat words to reach required size
        strings = (base_words * ((size // len(base_words)) + 1))[:size]

        print(f"\n===== Size: {size} =====")

        start_time = time.time()  # Start timing

        with multiprocessing.Pool() as pool:
            results = pool.map(reverse_and_check_palindrome, strings)

        end_time = time.time()  # End timing
        elapsed_time = end_time - start_time

        # Display results in requested format
        for s, rev, is_pal in results:
            print(f"{s} : {rev} : Palindrome {is_pal}")

        print(f"⏱️ Time taken for size {size}: {elapsed_time:.6f} seconds")

