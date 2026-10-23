import numpy as np
import matplotlib.pyplot as plt 
import sounddevice as sdd

def f_sin(t):
    return np.sin(2*np.pi*t*200)

axa_es = np.linspace(0, 1, 1000)
axa_real = np.linspace(0, 1, 20000)

rez_real = f_sin(axa_real)
rez_full = f_sin(axa_es)

rez_part_1 = rez_full[::4]

rez_part_2 = rez_full[1::4]


fig, axs = plt.subplots(3)


axs[0].stem(axa_es, rez_full)
axs[0].plot(axa_es, rez_full)
axs[0].plot(axa_real, rez_real, color = "gray")

axs[1].stem(axa_es[::4], rez_part_1)
axs[1].plot(axa_es[::4], rez_part_1)
axs[1].plot(axa_real, rez_real)

axs[2].stem(axa_es[1::4], rez_part_2)
axs[2].plot(axa_es[1::4], rez_part_2)
axs[2].plot(axa_real, rez_real)

for ax in axs:
    ax.set_xlim([0, 0.025])

plt.savefig("./lab2/fig/lab2_ex4_7.pdf")

plt.show()

