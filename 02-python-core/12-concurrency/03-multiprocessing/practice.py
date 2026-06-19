from multiprocessing import Process


def task(name):
    for i in range(3):
        print(
            f"{name}: {i}"
        )


p1 = Process(
    target=task,
    args=("Process-1",)
)

p2 = Process(
    target=task,
    args=("Process-2",)
)

p1.start()
p2.start()

p1.join()
p2.join()

print("All processes completed")