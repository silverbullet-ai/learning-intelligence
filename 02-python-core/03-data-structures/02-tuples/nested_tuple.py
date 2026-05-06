nested = (
    (1, 2, 3),
    ("A", "B", "C"),
    (True, False)
)

print(nested[1][2])

for sub_tuple in nested:
    for item in sub_tuple:
        print(item)