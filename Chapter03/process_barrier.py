import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
from reversed_string import reverse_and_check_palindrome  # ✅ import your palindrome function

def test_with_barrier(synchronizer, serializer):
    """Function that waits on a barrier before printing palindrome results."""
    name = multiprocessing.current_process().name
    synchronizer.wait()  # Wait until all processes reach this point
    now = time()

    strings = ["madam", "apple", "racecar", "python", "level"]
    results = [reverse_and_check_palindrome(s) for s in strings]

    with serializer:  # Ensure clean output (one process prints at a time)
        print(f"\n[{datetime.fromtimestamp(now)}] {name} started:")
        for s, (rev, is_pal) in zip(strings, results):
            print(f"{s} → {rev} | Palindrome: {is_pal}")
        print(f"{name} finished.\n")

def test_without_barrier():
    """Function that runs immediately without waiting on a barrier."""
    name = multiprocessing.current_process().name
    now = time()

    strings = ["noon", "banana", "rotor"]
    results = [reverse_and_check_palindrome(s) for s in strings]

    print(f"\n[{datetime.fromtimestamp(now)}] {name} started (no barrier):")
    for s, (rev, is_pal) in zip(strings, results):
        print(f"{s} → {rev} | Palindrome: {is_pal}")
    print(f"{name} finished.\n")

if __name__ == '__main__':
    multiprocessing.freeze_support()  
    synchronizer = Barrier(2)  # Two processes will wait here
    serializer = Lock()

    # Processes using barrier synchronization
    Process(name='P1 - with_barrier', target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    Process(name='P2 - with_barrier', target=test_with_barrier,
            args=(synchronizer, serializer)).start()

    # Processes running independently (no barrier)
    Process(name='P3 - without_barrier', target=test_without_barrier).start()
    Process(name='P4 - without_barrier', target=test_without_barrier).start()
