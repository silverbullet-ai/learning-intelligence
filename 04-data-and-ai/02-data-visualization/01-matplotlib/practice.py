import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker="o")

plt.xlabel("Number")
plt.ylabel("Square")
plt.title("Squares of Numbers")

plt.grid(True)

plt.show()