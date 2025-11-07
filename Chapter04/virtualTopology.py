from mpi4py import MPI
import numpy as np
from reserved_pal import reverse_and_check_palindrome  

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0, 0, 0, 0]
strings = ["madam", "apple", "racecar", "python", "level", "noon", "celebrate", "eat", "world", "refer"]

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    # Determine grid dimensions
    grid_row = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_row

    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    if rank == 0:
        print(f"Building a {grid_row} x {grid_column} grid topology:\n")

    # Create Cartesian communicator
    cartesian_communicator = comm.Create_cart(
        (grid_row, grid_column),
        periods=(True, True),
        reorder=True
    )

    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)

    # Find neighbors
    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

    # Assign a string to each process based on rank
    my_string = strings[rank % len(strings)]
    reversed_s, is_palindrome = reverse_and_check_palindrome(my_string)

    # Print Cartesian info + palindrome info
    print(f"Process = {rank} \n"
          f"Row = {my_mpi_row} Column = {my_mpi_col}\n"
          f"Neighbours: UP={neighbour_processes[UP]}, DOWN={neighbour_processes[DOWN]}, "
          f"LEFT={neighbour_processes[LEFT]}, RIGHT={neighbour_processes[RIGHT]}\n"
          f"String='{my_string}', Reversed='{reversed_s}', Palindrome={is_palindrome}\n")
