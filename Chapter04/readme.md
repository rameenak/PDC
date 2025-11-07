# Chapter 04

This repository contains **MPI programs implemented using `mpi4py`** in Python.
Each program demonstrates a different MPI communication pattern while integrating a **palindrome check** using the `reverse_and_check_palindrome` function.

---

## **Overview**

Each script demonstrates a different MPI communication pattern, including:

* **Point-to-Point Communication (`Send/Recv`)**
* **Collective Communication (`Alltoall`, `Gather`, `Scatter`, `Reduce`, `Broadcast`)**
* **Cartesian Topology**

All string-based examples include a **palindrome check** using the `reverse_and_check_palindrome` function from `reserved_Pal.py`.

---

## **Scripts and Descriptions**

### **1. `alltoall.py` – All-to-All Communication**

* Each process sends its reversed string to all others and receives all reversed strings.
* **Example Output:**

```
Process 0: Original='madam', Reversed='madam', Palindrome=True
Process 0 received all reversed strings: ['madam', 'elppa', 'racecar', 'nohtyp']
Process 2: Original='racecar', Reversed='racecar', Palindrome=True
Process 2 received all reversed strings: ['madam', 'elppa', 'racecar', 'nohtyp']
Process 1: Original='apple', Reversed='elppa', Palindrome=False
Process 1 received all reversed strings: ['madam', 'elppa', 'racecar', 'nohtyp']
Process 3: Original='python', Reversed='nohtyp', Palindrome=False
Process 3 received all reversed strings: ['madam', 'elppa', 'racecar', 'nohtyp']
```

### **2. `boardcast.py` – Broadcast**

* Root process broadcasts a string to all processes.
* Each process prints its string and palindrome status.

```
Process 0: Original='racecar', Reversed='racecar', Palindrome=True
Process 1: Original='racecar', Reversed='racecar', Palindrome=True
Process 2: Original='racecar', Reversed='racecar', Palindrome=True
Process 3: Original='racecar', Reversed='racecar', Palindrome=True
```

### **3. `deadlockproblems.py` – Point-to-Point with Deadlock**

* Demonstrates potential deadlock with `send`/`recv`.
* Fixed using `sendrecv()`.
* Strings are sent between processes and palindrome is checked.

```
My rank is 3
My rank is 0
My rank is 2
My rank is 4
My rank is 1
Process 1: Original='madam', Reversed='madam', Palindrome=True
Process 1 sent 'madam' to process 5
Process 1 received 'racecar' from process 5
My rank is 5
Process 5: Original='racecar', Reversed='racecar', Palindrome=True
Process 5 sent 'racecar' to process 1
Process 5 received 'madam' from process 1
```

### **4. `gather.py` – Gather**

* Each process sends string + palindrome info to root.
* Root prints all received data.

```
Rank 0 gathering data from other processes:

Process 0: Original='madam', Reversed='madam', Palindrome=True
Process 1: Original='apple', Reversed='elppa', Palindrome=False
Process 2: Original='racecar', Reversed='racecar', Palindrome=True
Process 3: Original='python', Reversed='nohtyp', Palindrome=False
Process 4: Original='level', Reversed='level', Palindrome=True
```

### **5. `helloworld_mpi.py` – Hello World**

* Each process prints a hello message along with string and palindrome check.

```
Hello world from process 3: Original='python', Reversed='nohtyp', Palindrome=False
Hello world from process 4: Original='level', Reversed='level', Palindrome=True
Hello world from process 0: Original='madam', Reversed='madam', Palindrome=True
Hello world from process 2: Original='racecar', Reversed='racecar', Palindrome=True
Hello world from process 1: Original='apple', Reversed='elppa', Palindrome=False
```

### **6. `pointToPointCommunication.py` – Point-to-Point**

* Demonstrates sending/receiving data between specific ranks.
* Strings are checked for palindrome before sending.

```
My rank is: 0
Process 0 sending data 10000000 to process 4
My rank is: 7
My rank is: 5
My rank is: 1
Process 1: Original='madam', Reversed='madam', Palindrome=True
Process 1 sending data 'madam' to process 8
My rank is: 3
My rank is: 6
My rank is: 8
Process 8 received data = 'madam', Reversed='madam', Palindrome=True
My rank is: 4
Process 4 received data = 10000000
My rank is: 2
```

### **7. `reduction.py` – Reduction**

* Counts total number of palindromes across all processes using `reduce()`.

```
Process 8: Original='world', Reversed='dlrow', Palindrome=False
Process 6: Original='hello', Reversed='olleh', Palindrome=False
Process 7: Original='eat', Reversed='tae', Palindrome=False
Process 2: Original='racecar', Reversed='racecar', Palindrome=True
Process 0: Original='madam', Reversed='madam', Palindrome=True

**Total number of palindromes among all processes: 4**
Process 4: Original='level', Reversed='level', Palindrome=True
Process 3: Original='python', Reversed='nohtyp', Palindrome=False
Process 5: Original='noon', Reversed='noon', Palindrome=True
Process 1: Original='apple', Reversed='elppa', Palindrome=False
```

### **8. `scatter.py` – Scatter**

* Root process scatters strings to all processes.
* Each process prints received string and palindrome status.

```
Process 1: Original='apple', Reversed='elppa', Palindrome=False
Process 2: Original='racecar', Reversed='racecar', Palindrome=True
Process 4: Original='level', Reversed='level', Palindrome=True
Process 6: Original='hello', Reversed='olleh', Palindrome=False
Process 0: Original='madam', Reversed='madam', Palindrome=True
Process 3: Original='python', Reversed='nohtyp', Palindrome=False
Process 5: Original='noon', Reversed='noon', Palindrome=True
Process 8: Original='world', Reversed='dlrow', Palindrome=False
Process 9: Original='refer', Reversed='refer', Palindrome=True
Process 7: Original='eat', Reversed='tae', Palindrome=False
```

### **9. `virtualTopology.py` – Cartesian Topology**

* Each process computes neighbors in a 2D grid and prints string, reversed string, and palindrome.

```
Process = 1 
Row = 0 Column = 1
Neighbours: UP=7, DOWN=4, LEFT=0, RIGHT=2
String='apple', Reversed='elppa', Palindrome=False

Process = 7 
Row = 2 Column = 1
Neighbours: UP=4, DOWN=1, LEFT=6, RIGHT=8
String='eat', Reversed='tae', Palindrome=False

Process = 4 
Row = 1 Column = 1
Neighbours: UP=1, DOWN=7, LEFT=3, RIGHT=5
String='level', Reversed='level', Palindrome=True

Process = 2
Row = 0 Column = 2
Neighbours: UP=8, DOWN=5, LEFT=1, RIGHT=0
String='racecar', Reversed='racecar', Palindrome=True

Process = 5
Row = 1 Column = 2
Neighbours: UP=2, DOWN=8, LEFT=4, RIGHT=3
String='noon', Reversed='noon', Palindrome=True

Building a 3 x 3 grid topology:

Process = 0
Row = 0 Column = 0
Neighbours: UP=6, DOWN=3, LEFT=2, RIGHT=1
String='madam', Reversed='madam', Palindrome=True

Process = 8
Row = 2 Column = 2
Neighbours: UP=5, DOWN=2, LEFT=7, RIGHT=6
String='world', Reversed='dlrow', Palindrome=False

Process = 3 
Row = 1 Column = 0
Neighbours: UP=0, DOWN=6, LEFT=5, RIGHT=4
String='python', Reversed='nohtyp', Palindrome=False

Process = 6
Row = 2 Column = 0
Neighbours: UP=3, DOWN=0, LEFT=8, RIGHT=7
String='celebrate', Reversed='etarbelec', Palindrome=False
```

---

## **Summary Table**

| Script Name                    | MPI Communication Type       | Description & Output Summary                                                                 |
| ------------------------------ | ---------------------------- | -------------------------------------------------------------------------------------------- |
| `alltoall.py`                  | All-to-All (`Alltoall`)      | Sends and receives reversed strings among all processes. Palindrome check included.          |
| `boardcast.py`                 | Broadcast (`Bcast`)          | Root broadcasts string; all processes print string and palindrome status.                    |
| `deadlockproblems.py`          | Point-to-Point (`Send/Recv`) | Demonstrates potential deadlock. Strings sent between ranks; palindrome checked.             |
| `gather.py`                    | Gather (`Gather`)            | Collects string + palindrome info at root.                                                   |
| `helloworld_mpi.py`            | Point-to-Point / Demo        | Each process prints hello message with string and palindrome status.                         |
| `pointToPointCommunication.py` | Point-to-Point (`Send/Recv`) | Rank-to-rank communication. Strings and numbers sent; palindrome checked.                    |
| `reduction.py`                 | Reduction (`Reduce`)         | Counts total number of palindromes using sum reduction.                                      |
| `scatter.py`                   | Scatter (`Scatter`)          | Root scatters strings; each process prints received string and palindrome status.            |
| `virtualTopology.py`           | Cartesian Topology           | Computes neighbors in grid; prints rank, neighbors, string, reversed string, and palindrome. |

---

## **Usage**

Run any program using `mpiexec` with the desired number of processes:

```bash
mpiexec -n <num_processes> python <script_name>.py
```

**Example:**

```bash
mpiexec -n 4 python alltoall.py
```

---

## **Dependencies**

* Python 3.x
* [`mpi4py`](https://mpi4py.readthedocs.io/)

Install via pip:

```bash
pip install mpi4py
```

* **Microsoft MPI (MS-MPI)** installed for Windows.

---

This README documents all MPI Python programs in **Chapter 04**, their communication types, and their outputs including palindrome checks.


