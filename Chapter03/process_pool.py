# Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing
from reversed_string import reverse_and_check_palindrome  # ✅ import your function

def process_word(word):
    """Wrapper function for pool workers"""
    reversed_s, is_palindrome = reverse_and_check_palindrome(word)
    return f"{word} → {reversed_s} | Palindrome: {is_palindrome}"

if __name__ == '__main__':
    multiprocessing.freeze_support()  

   
    strings = ["madam", "apple", "racecar", "python", "level", "noon"]

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=4)
    
    # Distribute work among processes
    results = pool.map(process_word, strings)

    # Close and join the pool
    pool.close()
    pool.join()

    print("\n=== Process Pool Palindrome Results ===")
    for r in results:
        print(r)
