## Code 3: Reverse string and check palindrome (Threading version - formatted output)
import threading
import time

def reverse_and_check_palindrome(s, results, index):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    results[index] = (s, reversed_s, is_palindrome)

if __name__ == "__main__":
    base_words = ["madam", "apple", "racecar", "python", "level"]
    sizes = [5, 10, 15, 50]

    for size in sizes:
        # Repeat base words to reach required size
        strings = (base_words * ((size // len(base_words)) + 1))[:size]
        results = [None] * size
        threads = []

        print(f"\n===== Size: {size} =====")

        start_time = time.time()  # Start timing

        # Create and start threads
        for i in range(size):
            t = threading.Thread(target=reverse_and_check_palindrome, args=(strings[i], results, i))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        end_time = time.time()  # End timing
        elapsed_time = end_time - start_time

        # Display results in requested format
        for s, rev, is_pal in results:
            print(f"{s} : {rev} : Palindrome {is_pal}")

        print(f"Time taken for size  {size} by thread: {elapsed_time:.6f} seconds")
