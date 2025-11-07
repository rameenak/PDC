from mpi4py import MPI
from reserved_pal import reverse_and_check_palindrome  

comm = MPI.COMM_WORLD
rank = comm.rank

print(f"My rank is {rank}")

# Only ranks 1 and 5 communicate
if rank == 1:
    data_to_send = "madam" 
    destination = 5
    reversed_s, is_palindrome = reverse_and_check_palindrome(data_to_send)
    print(f"Process {rank}: Original='{data_to_send}', Reversed='{reversed_s}', Palindrome={is_palindrome}")

    # Correct sendrecv usage
    data_received = comm.sendrecv(sendobj=data_to_send, dest=destination, source=destination)

    print(f"Process {rank} sent '{data_to_send}' to process {destination}")
    print(f"Process {rank} received '{data_received}' from process {destination}")

elif rank == 5:
    data_to_send = "racecar"  
    destination = 1
    reversed_s, is_palindrome = reverse_and_check_palindrome(data_to_send)
    print(f"Process {rank}: Original='{data_to_send}', Reversed='{reversed_s}', Palindrome={is_palindrome}")

    # Correct sendrecv usage
    data_received = comm.sendrecv(sendobj=data_to_send, dest=destination, source=destination)

    print(f"Process {rank} sent '{data_to_send}' to process {destination}")
    print(f"Process {rank} received '{data_received}' from process {destination}")
