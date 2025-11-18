import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

fig, ax = plt.subplots(figsize=(8, 6))
sigma = 10
window_size = 15
with open("measure_before.csv") as before:
    x_before, y_before = list(), list()
    for line in before.readlines():
        line = line.strip().split(',')
        x_before.append(line[0])
        y_before.append(line[1])
    x_before = np.array(x_before, dtype='float64')
    y_before = (np.array(y_before, dtype='float64') - .15) / .0118

    y_filtered_before = y_before - gaussian_filter1d(y_before, sigma)
    y_smooth_before = np.convolve(y_before, np.ones(window_size)/window_size, mode='same')
#ax.scatter(x_before, y_filtered_before, s=1)
#ax.scatter(x_before, np.convolve(y_before, np.ones(3000)/3000, mode='valid'))
#ax.scatter(x_before[13000:16000], y_before[13000:16000], s=1)
ax.scatter(x_before, y_smooth_before, s=1)

with open("measure_after.csv") as after:
    x_after, y_after = list(), list()
    for line in after.readlines():
        line = line.strip().split(',')
        x_after.append(line[0])
        y_after.append(line[1])
    x_after = np.array(x_after, dtype='float64')
    y_after = (np.array(y_after, dtype='float64') - .15) / .0118

    y_filtered_after = y_after - gaussian_filter1d(y_after, sigma)
#ax.scatter(x_after, y_filtered_after, s=1)
ax.grid(True, alpha=.3)

plt.show()
# x=(y-0.15)/0.0118
