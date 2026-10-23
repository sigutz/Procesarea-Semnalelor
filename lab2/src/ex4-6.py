import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sdd

fs = 41000
durata = 1

def f_a(t):
    return np.sin(2*np.pi*t*(fs/2))

def f_b(t):
    return np.sin(2*np.pi*t*(fs/4))

def f_c(t):
    return np.sin(2*np.pi*t*0)

axa_reala = np.linspace(0, durata, durata*fs)

fig, axs = plt.subplots(3)

rez_f_a = f_a(axa_reala)
rez_f_b= f_b(axa_reala)
rez_f_c = f_c(axa_reala)

axs[0].plot(axa_reala, rez_f_a)
sdd.play(rez_f_a, fs)

axs[1].plot(axa_reala, rez_f_b)
sdd.play(rez_f_a, fs)

axs[2].plot(axa_reala, rez_f_c)
sdd.play(rez_f_c, fs)

for ax in axs:
    ax.set_xlim([0, 0.01])

sdd.wait()

plt.savefig("./lab2/fig/lab2_ex4_6.pdf")

plt.show()


#la frecvente mari nu se mai aude nimic :///