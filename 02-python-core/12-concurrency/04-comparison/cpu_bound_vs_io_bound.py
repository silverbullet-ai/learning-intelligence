import time


def io_task():
    time.sleep(2)


def cpu_task():
    total = 0

    for i in range(10_000_000):
        total += i

    return total


start = time.time()

io_task()

print(
    f"I/O Task Time: {time.time() - start:.2f}"
)

start = time.time()

cpu_task()

print(
    f"CPU Task Time: {time.time() - start:.2f}"
)