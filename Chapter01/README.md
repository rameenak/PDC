# Chapter 1 — Process and Threads  

This chapter introduces the basic concepts of string manipulation and parallelism using Python.  
It demonstrates reversing strings and checking for palindromes using **sequential**, **multiprocessing**, and **threading** approaches.  
It also compares execution methods to show performance differences.

Files included:

- **reversedstring.py** → Sequential execution (single-process)  
  - Each string is reversed one by one.  
  - Checks if the original string is a palindrome.  
  - Simple and easy to understand; suitable for small datasets.  

- **reversedstring_processes.py** → Parallel execution using multiprocessing  
  - Uses multiple CPU processes to reverse strings and check palindromes concurrently.  
  - Faster for large datasets or CPU-heavy operations.  

- **reversedstring_thread.py** → Concurrent execution using threading  
  - Uses multiple threads to reverse strings and check palindromes.  
  - Threads share memory; good for lightweight or I/O-bound tasks.  

- **screenshots/** → Contains screenshots showing outputs and performance comparison  

---
## Performance Comparison 
| Input Size  |  Process Time (s)| Thread Time (s)|
 | ---------- | ---------------- | --------------- | 
 | 5          | 0.98271          | 0.0022          | 
 | 10         | 0.37694          | 0.0041          |
 | 15         | 0.303615         | 0.0050          | 
 |  50        | 0.278867         | 0.0206          |

The performance comparison clearly shows that **threading is significantly faster than multiprocessing** for smaller input sizes because creating multiple processes has a higher overhead in Python. However, as input size increases, multiprocessing can become more efficient for CPU-intensive tasks, while threading remains ideal for lightweight operations like string manipulation.

## How Each Code Works

1. **Sequential Version**  
   - Loops through each string one by one.  
   - Reverses the string using `[::-1]` and checks if it's a palindrome.  

2. **Multiprocessing Version**  
   - Creates a process pool (`multiprocessing`) to handle strings in parallel.  
   - Each process returns the reversed string and palindrome status.  
   - Collects results and prints them after all processes finish.  

3. **Threading Version**  
   - Creates multiple threads (`threading.Thread`) for each string.  
   - Threads store results in a shared list.  
   - Uses `join()` to wait for all threads to finish before printing results.  


