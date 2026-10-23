import numpy as np
import matplotlib.pyplot as plt

# 2

def f2_sin(t, faza = 0):
    return np.sin(2*np.pi*400*t + faza)

axa_reala = np.linspace(0,1,20000)

fig, axs = plt.subplots(4)

fig.suptitle("Exercitiul 4.2")

for i in range(len(axs)):
    faza = np.pi/(i+1)
    axs[i].plot(axa_reala, f2_sin(axa_reala, faza))
    axs[i].set_title(f"faza = {faza}")
    axs[i].set_xlim([0,0.01])

plt.savefig("./lab2/fig/lab2_ex4_2_a.pdf")

plt.show()

# 2 b

def gama_SNR(snr, val_f2_sin, val_z):
    return (np.abs(np.linalg.norm(val_f2_sin)**2/(snr*(np.linalg.norm(val_z)**2))))**(1/2)

val_z = np.random.normal(size = 20000)

val_f2_sin = f2_sin(axa_reala)

snr = [0.1, 1, 10, 100]

fig, axs = plt.subplots(len(snr))

for i in range (len(snr)):
    val_gama = gama_SNR(snr[i], val_f2_sin, val_z)

    semnal_nou = val_f2_sin + val_gama*val_z 

    axs[i].set_title(f"SNR = {snr[i]}; Gama = {val_gama}")
    axs[i].plot(axa_reala, semnal_nou, color ="blue")
    axs[i].plot(axa_reala, val_f2_sin, color = "red")
    axs[i].set_xlim([0,0.01])

plt.savefig("./lab2/fig/lab2_ex4_2_b.pdf")

plt.show()