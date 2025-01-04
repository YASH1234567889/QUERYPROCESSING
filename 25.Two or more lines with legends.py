import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 3, 5, 7, 11]
y3 = [1, 2, 3, 4, 5]
plt.plot(x, y1, label="Line 1 (y=x^2)", color="blue", linewidth=2)
plt.plot(x, y2, label="Line 2 (Prime Numbers)", color="red", linewidth=3)
plt.plot(x, y3, label="Line 3 (y=x)", color="green", linewidth=1)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Lines with Legends, Colors, and Widths")
plt.legend()
plt.show()
