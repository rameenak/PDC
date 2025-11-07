from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
strings = ["madam", "apple", "racecar", "python", "level"]

# Each process picks a string based on its rank
my_string = strings[rank % len(strings)]
reversed_s, is_palindrome = reverse_and_check_palindrome(my_string)
all_reversed_strings = comm.allgather(reversed_s)
print(f"Process {rank}: Original='{my_string}', Reversed='{reversed_s}', Palindrome={is_palindrome}")
print(f"Process {rank} received all reversed strings: {all_reversed_strings}")
