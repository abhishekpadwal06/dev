import pandas as pd
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

index = count()

def animate(i):
    data = pd.read_csv('/home/abhishek44/Documents/MAIN DEV/Dev/Data Analysis/Matplotlib/Plotting Live Data in Real-time/data.csv')

    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1', linewidth=2)
    plt.plot(x, y2, label='Channel 2', linewidth=2)

    plt.legend(loc='upper left')

ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()