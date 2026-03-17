import os
import threading, multiprocessing
from time import perf_counter

# CPU-heavy task
def count(n):
    while n > 0:
        n -= 1

def main():
    
    start = perf_counter() # get the start time using the performance counter from the time module
    
    print(f"[main pid={os.getpid()}] building workers...")

    # MULTI-THREADING (limited by the GIL for CPU-bound work)
    #
    # What's essential for correct behavior:
    # - `.start()` is required, otherwise the thread never runs.
    # - `.join()` is required if the main program must wait for completion (otherwise it may exit early).
    #
    # Why it's there:
    # - For CPU-heavy Python code, threads don't speed things up due to the GIL; they mostly interleave on one core.
    t1 = threading.Thread(target=count, args=(10**7,), name="t1")
    t2 = threading.Thread(target=count, args=(10**7,), name="t2")

    # MULTI-PROCESSING (bypasses the GIL)
    #
    # What's essential for correct behavior:
    # - `.start()` is required to actually launch the child process.
    # - `.join()` is required if you need deterministic completion before printing results/exiting.
    #
    # Why it's there:
    # - Each process has its own Python interpreter and memory space, so CPU-bound work can run in parallel on
    #   multiple cores and actually get faster (at the cost of higher overhead).
    p1 = multiprocessing.Process(target=count, args=(10**7,), name="p1")
    p2 = multiprocessing.Process(target=count, args=(10**7,), name="p2")

    print(f"[main pid={os.getpid()}] starting threads: {t1.name}, {t2.name}")
    t1.start()
    t2.start()

    print(f"[main pid={os.getpid()}] starting processes: {p1.name}, {p2.name}")
    p1.start()
    p2.start()

    print(f"[main pid={os.getpid()}] waiting for threads to finish (join)...")
    t1.join()
    t2.join()

    print(f"[main pid={os.getpid()}] waiting for processes to finish (join)...")
    p1.join()
    p2.join()

    elapsed = perf_counter() - start
    print(f"[main pid={os.getpid()}] done in {elapsed:.3f}s (threads + processes finished)")

if __name__ == "__main__":
    main()