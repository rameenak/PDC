from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome  

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Only rank 0 selects a string
if rank == 0:
    my_string = "racecar"  # Root process selects a string
    reversed_s, is_palindrome = reverse_and_check_palindrome(my_string)
    data_to_broadcast = (my_string, reversed_s, is_palindrome)
else:
    data_to_broadcast = None

# Broadcast the data from root to all processes
my_string, reversed_s, is_palindrome = comm.bcast(data_to_broadcast, root=0)
print(f"Process {rank}: Original='{my_string}', Reversed='{reversed_s}', Palindrome={is_palindrome}")
