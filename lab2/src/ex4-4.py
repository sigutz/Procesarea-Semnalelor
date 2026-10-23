import numpy as np
import matplotlib.pyplot as plt

def f_sin(t):
    return np.sin(2*np.pi*400*t)

def f_sawthoot(t):
    return 2*(t*240 - np.floor(1/2+ t*240))

axa_real = np.linspace(0, 1, 20000)

rez_sin = f_sin(axa_real)
rez_sawthoot = f_sawthoot(axa_real)
rez_com = rez_sawthoot + rez_sin

fig, axs = plt.subplots(3)

fig.suptitle("Sin + Sawthoot")

axs[0].plot(axa_real, rez_sin)
axs[0].set_title("sin")

axs[1].plot(axa_real, rez_sawthoot)
axs[1].set_title("sawthoot")

axs[2].plot(axa_real, rez_com)
axs[2].set_title("adunate")

for ax in axs:
    ax.set_xlim([0, 0.05])

plt.show()
plt.savefig("./lab2/fig/lab2_ex4_4.pdf")