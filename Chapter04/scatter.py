from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome  

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Only rank 0 prepares the array of strings
if rank == 0:
    strings_to_share = ["madam", "apple", "racecar", "python", "level", "noon", "hello", "eat", "world", "refer"]
else:
    strings_to_share = None

# Scatter the strings: each process gets one string
my_string = comm.scatter(strings_to_share, root=0)
reversed_s, is_palindrome = reverse_and_check_palindrome(my_string)
print(f"Process {rank}: Original='{my_string}', Reversed='{reversed_s}', Palindrome={is_palindrome}")
