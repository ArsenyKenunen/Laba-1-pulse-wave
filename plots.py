import matplotlib.pyplot as plt
import numpy as np


b = 0.14963690399777596
k = 0.011793942035391742

window_size = 15


def show_plot():
    plt.grid(True, alpha=.3)
    plt.xlabel("time, s")
    plt.show()
    plt.close()
    plt.figure(figsize=(11, 8))


def cut_above_threshold(active_array, copying_array, threshold):
    active_return, copying_return = list(), list()
    for i in range(len(active_array)):
        if active_array[i] >= threshold:
            active_return.append(active_array[i])
            copying_return.append(copying_array[i])
    return active_return, copying_return


plt.figure(figsize=(11, 8))

x, y = list(), list()
with open("measure_before.csv") as before:
    for line in before.readlines():
        line = line.strip().split(',')
        x.append(line[0])
        y.append(line[1])
x = np.array(x, dtype='float64')
y = (np.array(y, dtype='float64') - b) / k

trend_poly = np.poly1d(np.polyfit(x, y, 5))
y_trend = trend_poly(x)
y_smooth = np.convolve(y, np.ones(window_size) / window_size, mode='same')

plt.scatter(x, y_smooth, s=1)
plt.ylabel("blood pressure, mmHg")
plt.title("Blood pressure over time before physical activity")
show_plot()

y_cutted, x_cutted = cut_above_threshold(y_smooth - y_trend, x, -2)
plt.scatter(x_cutted, y_cutted, s=1)
plt.ylabel("delta pressure, mmHg")
plt.title("Blood pressure over time before physical activity: pulses")
show_plot()

y_diff = np.gradient(y_smooth, (max(x) - min(x)) / len(x))
plt.scatter(x, y_diff, s=1)
plt.ylabel("d(pressure)/dt, mmHg/s")
plt.title("Blood pressure over time before physical activity: diff pulses")
show_plot()


"""
x, y = list(), list()
with open("measure_after.csv") as after:
    for line in after.readlines():
        line = line.strip().split(',')
        x.append(line[0])
        y.append(line[1])
x = np.array(x, dtype='float64')
y = (np.array(y, dtype='float64') - b) / k

trend_poly = np.poly1d(np.polyfit(x, y, 5))
y_trend = trend_poly(x)
y_smooth = np.convolve(y, np.ones(window_size)/window_size, mode='same')

plt.scatter(x, y_smooth, s=1)
plt.ylabel("blood pressure, mmHg")
plt.title("Blood pressure over time after physical activity")
show_plot()

y_cutted, x_cutted = cut_above_threshold(y_smooth - y_trend, x, -2)
plt.scatter(x_cutted, y_cutted, s=1)
plt.ylabel("delta pressure, mmHg")
plt.title("Blood pressure over time after physical activity: pulses")
show_plot()
"""


plt.close()
