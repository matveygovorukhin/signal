import numpy as np
import math
import random
from matplotlib import pyplot as plt

t = np.array([i/100 for i in range(3000)])

sin = np.array([math.sin(i) for i in t])

noised_sin = sin.copy()
for i in range(len(sin)):
    noised_sin[i] += random.randint(-10, 10) / 20

plt.plot(noised_sin)

def median_filt(sign, window):
    filt = []
    wind = sign[:window]
    for i in range(len(sign) - window):
        temp = sorted(wind)
        median = temp[window//2]
        filt.append(median)
        wind = wind[1:]
        wind = np.append(wind, sign[i+window])
    return filt
plt.plot(median_filt(noised_sin, 20))
plt.plot(sin, c = 'r')
plt.show()
