import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to update the position of the point in each frame


def update(frame):
    point.set_data(frame, frame)


# Create a figure and axis
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create the point to animate
point, = ax.plot(0, 0, marker='o', color='r')

# Create an animation object
ani = animation.FuncAnimation(fig, update, frames=range(10), interval=500)

# Display the animation (this will open a window)
plt.show()
