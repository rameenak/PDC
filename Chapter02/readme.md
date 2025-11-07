# Chapter02 - Thread Synchronization: 

This project demonstrates different thread synchronization mechanisms in Python using the `threading` module.
Each example shows how multiple threads can run concurrently and how synchronization controls their execution.

We also include a **sequential version** without threads (`normal.py`) to compare runtime differences.

---

##  Files Overview

| File           | Concept           | Description                                                                  |
| -------------- | ----------------- | ---------------------------------------------------------------------------- |
| `normal.py`    | Sequential Run    | Runs multiple tasks sequentially (no threading).                             |
| `thread.py`    | Basic Threading   | Multiple threads run simultaneously without synchronization.                 |
| `lock.py`      | Lock              | Ensures only one thread can access a shared resource or print at a time.     |
| `rlock.py`     | RLock (Reentrant) | Allows a thread to acquire the same lock multiple times safely.              |
| `semaphore.py` | Semaphore         | Allows a limited number of threads to access a section of code concurrently. |
| `condition.py` | Condition         | Coordinates threads to run in a specific sequence using wait/notify.         |

---

## 1. `normal.py` — Sequential Execution

###  Description

This program runs multiple “animal” tasks sequentially without threads.
Each task waits for a random amount of time (1–5 seconds) before finishing.

### Key Points

* No threading used.
* Demonstrates sequential execution.
* Useful for comparing runtime with threaded versions.

###  Sample Output

```
Thread#1 Cow is running...
Thread#1 Cow finished at 2.83 seconds!
Thread#2 Tiger is running...
Thread#2 Tiger finished at 4.12 seconds!
Thread#3 Rabbit is running...
...
All finished in 34.56 seconds
```

---

##  1. `thread.py` — Basic Threading

###  Description

This program creates multiple threads (animals racing).
All threads run independently — they start, run, and finish in random order depending on their sleep times.

### Key Points

* Uses `threading.Thread` class.
* No synchronization — all threads print freely.
* Demonstrates parallelism.

### Sample Output

```
Thread#1 Cow is running...
Thread#2 Tiger is running...
Thread#3 Rabbit is running...
...
Thread#4 Dog finished at 2.83 seconds!
Thread#9 Turtle finished at 4.56 seconds!
End at ... 4.56 seconds
```

---

##  2. `lock.py` — Using Lock

### Description

Adds a **Lock** to control print statements, preventing overlapping outputs.

###  Key Points

* Uses `threading.Lock()`.
* Only one thread can enter the locked section at a time.
* Ensures clean, non-overlapping output.

### Sample Output

```
Thread#1 Cow is running...
Thread#2 Tiger is running...
...
Thread#8 Cheetah finished at 4.70 seconds!
Thread#3 Rabbit finished at 4.94 seconds!
End at ... 4.95 seconds
```

### 🔍 Difference from `thread.py`

* Without a lock, multiple threads print at the same time (mixed output).
* With a lock, print statements appear in order without mixing.

---

##  3. `rlock.py` — Using RLock (Reentrant Lock)

###  Description

Similar to a normal lock but allows the same thread to acquire the lock multiple times.

###  Key Points

* Uses `threading.RLock()`.
* Prevents self-deadlock when a thread re-enters a locked section (nested functions).
* Demonstrates nested locking safely.

### Sample Output

```
Thread#1 Cow is running...
Thread#1 Cow is warming up...
Thread#1 Cow finished at 2.31 seconds!
Thread#2 Tiger is running...
...
End at ... 4.87 seconds
```

###  Why RLock?

If you used a normal Lock here, the program would freeze (deadlock) because the same thread tries to lock again inside a nested function.

---

##  4. `semaphore.py` — Using Semaphore

### Description

A semaphore controls how many threads can access a section at once.
For example, only 3 threads can “run” at a time.

###  Key Points

* Uses `threading.Semaphore(3)`.
* At most 3 threads can print “running” at once.
* Demonstrates controlled concurrency.

###  Sample Output

```
Thread#1 Cow is running...
Thread#2 Tiger is running...
Thread#3 Rabbit is running...
(waiting threads start after one finishes)
...
End at ... 5.20 seconds
```

---

## 5. `condition.py` — Using Condition

###  Description

Threads wait for a condition to be met before continuing.
They run one by one in a specific sequence (controlled by a shared counter).

###  Key Points

* Uses `threading.Condition()`.
* Threads call `condition.wait()` until it’s their turn.
* The main thread or the previous thread calls `condition.notify_all()` to wake the next one.

###  Sample Output

```
Thread#1 Cow is running...
Thread#1 Cow finished at 1.82 seconds!
Thread#2 Tiger is running...
Thread#2 Tiger finished at 2.31 seconds!
Thread#3 Rabbit is running...
...
End at ... 25.50 seconds
```

---

## Summary of Differences

| Mechanism | Description                          | Parallel?    | Safe? | Used For                      |
| --------- | ------------------------------------ | ------------ | ----- | ----------------------------- |
| Normal    | Sequential execution                 | No           |  Yes | Compare threaded execution    |
| Thread    | Basic threading without control      | Yes          |  No  | Demonstrate concurrency       |
| Lock      | One thread at a time                 | Limited      |  Yes | Prevent data corruption       |
| RLock     | Re-entrant version of Lock           | Limited      |  Yes | Nested locking in same thread |
| Semaphore | Limit number of concurrent threads   | Limited      |  Yes | Resource-limited systems      |
| Condition | Threads wait for a signal to proceed | Sequential   |  Yes | Ordered execution / signaling |

---

## 🏁 How to Run

Run any file individually:

```bash
python normal.py
python thread.py
python lock.py
python rlock.py
python semaphore.py
python condition.py
```

Each program demonstrates a different **thread synchronization concept** in Python.



