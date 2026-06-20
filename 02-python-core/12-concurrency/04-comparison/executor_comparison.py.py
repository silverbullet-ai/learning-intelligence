from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor
)


def square(num):
    return num * num


numbers = [1, 2, 3, 4, 5]


with ThreadPoolExecutor() as executor:
    results = executor.map(
        square,
        numbers
    )

print(
    "ThreadPoolExecutor:",
    list(results)
)


if __name__ == "__main__":

    with ProcessPoolExecutor() as executor:
        results = executor.map(
            square,
            numbers
        )

    print(
        "ProcessPoolExecutor:",
        list(results)
    )