import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [5, 7, 3, 8]

plt.bar(categories, values)

plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")

plt.show()