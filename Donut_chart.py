import matplotlib.pyplot as plt
from matplotlib.patches import Circle  # Import Circle from patches

sizes = [25, 30, 10, 35]
labels = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

# Create a white circle in the center of the pie chart to make it a donut chart
circle = Circle((0, 0), 0.8, color='white')  # Create the Circle
ax.add_artist(circle)  # Add the Circle to the axes

ax.set_title('Donut Chart')
plt.show()
