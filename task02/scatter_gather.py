from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Process 0 has the initial array
if rank == 0:
    data = [10, 20, 30, 40]
else:
    data = None

# Scatter the array: each process receives one element
recv_data = comm.scatter(data, root=0)

# Each process multiplies its received element by 2
result = recv_data * 2

# Gather the results back to process 0
gathered_data = comm.gather(result, root=0)

# Process 0 prints the final result
if rank == 0:
    print("Gathered data at process 0:", gathered_data)
