import matplotlib.pyplot as plt  
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

info = np.arange(start = 0.0, stop = 5.0, step = 0.02)

plt.figure()
plt.subplot(211)
plt.title("Seno")
plt.ylabel('Max e Min')
plt.plot(info, np.sin(2*np.pi*info), 'r--')

plt.subplot(212)
plt.title("Coseno")
plt.ylabel('Max e Min')
plt.plot(info, np.cos(2*np.pi*info), 'r--')
plt.show()
