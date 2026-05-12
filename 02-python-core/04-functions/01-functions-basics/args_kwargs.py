def sum_all(*args):

    total = 0

    for num in args:
        total += num

    return total


print(sum_all(1, 2, 3, 4, 5))


def create_profile(**kwargs):

    for key, value in kwargs.items():
        print(f"{key} : {value}")


create_profile(
    name="Aahish",
    role="Developer",
    city="Patna"
)