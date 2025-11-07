from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome  

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
strings = ["madam", "apple", "racecar", "python", "level", "noon", "hello", "eat", "world"]


my_string = strings[rank % len(strings)]
reversed_s, is_palindrome = reverse_and_check_palindrome(my_string)

print(f"Process {rank}: Original='{my_string}', Reversed='{reversed_s}', Palindrome={is_palindrome}")

# For reduction, send 1 if palindrome, 0 if not
palindrome_flag = 1 if is_palindrome else 0

# Reduce (sum) number of palindromes to root process
total_palindromes = comm.reduce(palindrome_flag, op=MPI.SUM, root=0)

if rank == 0:
    print(f"\nTotal number of palindromes among all processes: {total_palindromes}")

