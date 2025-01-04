import matplotlib.pyplot as plt
file_name = "C:/Users/heman/OneDrive/Documents/Query Processing/data.txt"
with open(file_name, "r") as file:
    lines = file.readlines()
x_values = list(map(int, lines[1].strip().split()))
y_values = list(map(int, lines[3].strip().split()))
plt.plot(x_values, y_values, color="green", marker="*")
plt.xlabel("X Axis (Input Values)")
plt.ylabel("Y Axis (Output Values)")
plt.title("Line Plot from File Data")
plt.legend()
plt.show()
