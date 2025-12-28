import concurrent.futures
import time


string_list = ["madam", "apple", "racecar", "python", "level"]

def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = (s == reversed_s)
    return reversed_s, is_palindrome


def evaluate_string(s):
    rev, is_pal = reverse_and_check_palindrome(s)
    print(f"String: {s}, Reversed: {rev}, Palindrome: {is_pal}")


if __name__ == '__main__':


    start_time = time.perf_counter()
    for s in string_list:
        evaluate_string(s)
    print('Sequential Execution time = %.4f seconds\n'
          % (time.perf_counter() - start_time))


    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for s in string_list:
            executor.submit(evaluate_string, s)
    print('Thread Pool Execution time = %.4f seconds\n'
          % (time.perf_counter() - start_time))

    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for s in string_list:
            executor.submit(evaluate_string, s)
    print('Process Pool Execution time = %.4f seconds\n'
          % (time.perf_counter() - start_time))
