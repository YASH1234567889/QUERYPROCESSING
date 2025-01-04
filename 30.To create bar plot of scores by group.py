import matplotlib.pyplot as plt
import numpy as np
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]
x = np.arange(len(groups))
plt.figure(figsize=(10, 6))
plt.bar(x - 0.2, men_means, width=0.4, label='Men', color='blue', align='center')
plt.bar(x + 0.2, women_means, width=0.4, label='Women', color='green', align='center')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)
plt.legend()
plt.tight_layout()
plt.show()
