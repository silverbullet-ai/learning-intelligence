import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
sizes = [30, 20, 40, 10]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Pie Chart")

plt.show()