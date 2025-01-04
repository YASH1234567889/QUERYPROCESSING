import matplotlib.pyplot as plt
x = [0, 10, 20, 30, 40, 50]
y = [0, 20, 40, 60, 80, 90]
plt.figure(figsize=(10, 6))
plt.plot(x, y, color="blue")
plt.xlabel("X Axis (Input Values)")
plt.title("Line Plot Example")
plt.legend()
plt.show()
