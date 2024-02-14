from math import sin as sin
from matplotlib import pyplot as plt
import numpy as np
import random


def median_filt(signal, window_size):
    window = np.asarray(signal[0:window_size])
    filt = np.asarray(window[:window_size//2])

    for i in range(len(signal) - window_size):
        # print(int(i/len(signal)*100), '%')
        temp = np.sort(window)
        median = temp[window_size//2]
        filt = np.append(filt, median)
        window = window[1:]
        window = np.append(window, signal[i+window_size])
    filt = np.append(filt, signal[len(signal) - window_size//2 - window_size%2:])
    return filt

def arith_mean_filt(signal, window_size):
    window = np.asarray(signal[0:window_size])
    filt = np.asarray(window[:window_size//2])
    for i in range(len(signal) - window_size):
        # print(int(i/len(signal)*100), '%')
        mean = np.sum(window) / window_size
        filt = np.append(filt, mean)
        window = window[1:]
        window = np.append(window, signal[i + window_size])
    filt = np.append(filt, signal[len(signal) - window_size // 2  - window_size%2:])
    return filt

x = np.array([i/10 for i in range(1000)])
y = np.array([sin(x[i]) for i in range(1000)])

noised_sin = np.copy(y)
for i in range(len(y)):
    # noised_sin[i] += random.randint(-10, 10) / 40
    noised_sin[i] += np.random.normal(0, 0.2)

fig, ax=plt.subplots(figsize=(16, 12))
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')
ax.set_xlabel("ширина окна")
ax.set_ylabel("отклонение от идеала")

# ax.plot(x, noised_sin, label = 'noised')

best_filt = []
best_window = 0
best_delta = 1000000000
d_arr_median = []
d_arr_mean = []
for q in range(3, 30):
    result_median = arith_mean_filt(noised_sin, q)
    result_mean = median_filt(noised_sin, q)
    delta_median = np.array([])
    delta_mean = np.array([])
    for w in range(len(y)):
        delta_median = np.append(delta_median, abs(result_median[w] - y[w]))
        delta_mean = np.append(delta_mean, abs(result_mean[w] - y[w]))
    d_median = np.sum(delta_median) / len(y)
    d_mean = np.sum(delta_mean) / len(y)
    if d_median <= d_mean:
        best_filt.append('median')
    else:
        best_filt.append('mean')
    if min(d_mean, d_median) < best_delta:
        best_delta = min(d_mean, d_median)
        best_window = q
    d_arr_median.append(d_median)
    d_arr_mean.append(d_mean)


print('best window ', best_window)
print('----------')
for i in range(3, 30):
    print('best filter for window ', i, ': ' , best_filt[i-3])


result_median = arith_mean_filt(noised_sin, 20)
# ax.plot([i for i in range(3, 30)], d_arr_median, label = 'median filter')
# ax.plot([i for i in range(3, 30)], d_arr_mean, label = 'mean filter')
# ax.plot(x, y, c = 'purple',  label = 'ideal', linewidth = 2)
# ax.plot(x, result_median, label = 'filtered', linewidth = 2)
ax.legend(prop={'size': 30})
plt.savefig('windows.png')
plt.show()