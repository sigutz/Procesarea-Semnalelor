import numpy as np
import matplotlib.pyplot as plt

def pade(a):
    return (a-(7*a**3)/60)/(1+a**2/20) 

inf = np.pi/-2

sup = np.pi/2

fs = 1000

axa = np.arange(inf, sup, 1/fs)

fig, axs = plt.subplots(4)

axs[0].plot(axa, np.sin(axa), color = "red")
axs[0].plot(axa, axa, color = "blue")

axs[1].plot(axa, np.abs(np.sin(axa) - axa))

axs[2].plot(axa, np.sin(axa), color = "red")
axs[2].plot(axa, axa, color = "blue")
axs[2].plot(axa, pade(axa), color = "orange")
axs[2].set_xlim(([-0.1, 0.1]))

axs[3].plot(axa, np.abs(pade(axa) - axa))
axs[3].set_yscale('log')


plt.savefig("./lab2/fig/lab2_ex4_8.pdf")
plt.show()