import numpy as np
import matplotlib.pyplot as plt

axa_reala = np.linspace(0,1,20000)


# 1
A = 2
f = 400

def f_sin(t):
    return A*np.sin(2*np.pi*t*f + np.pi/2)

def f_cos(t):
    return A*np.cos(2*np.pi*t*f)

fig, axs = plt.subplots(2)

fig.suptitle("cos(t) = sin(wt + pi/2)")

axs[0].set_title("sin")
axs[0].plot(axa_reala, f_sin(axa_reala))

axs[1].set_title("cos")
axs[1].plot(axa_reala, f_cos(axa_reala))

for ax in axs:
    ax.set_xlim([0, 0.01])

plt.savefig("./lab2/fig/lab2_ex4_1.pdf")
plt.show()


