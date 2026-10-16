import numpy as np
import matplotlib.pyplot as plt

# a
def f_a(t):
    return np.sin(2*np.pi*400*t)

axa_hz = np.linspace(0,1, 1600)
axa_real = np.linspace(0,1, 20000)


fig, axs = plt.subplots(1)

fig.suptitle("Exercițiul 2.a")

axs.plot(axa_real, f_a(axa_real))
axs.stem(axa_hz, f_a(axa_hz))

axs.set_xlim([0, 0.01])

plt.savefig("./fig/lab1_ex2_a.pdf")

#b 

def f_b(t):
    return np.sin(2*np.pi*800*t)

axa_hz = np.linspace(0,3, 9600)
axa_real = np.linspace(0, 3, 60000)

fig, axs = plt.subplots(1)
fig.suptitle("Exercițiul 2 b")

axs.plot(axa_real, f_b(axa_real))
axs.stem(axa_hz, f_b(axa_hz))

axs.set_xlim([0,0.01])

plt.savefig("./fig/lab1_ex2_b.pdf")


#c 

def f_c(t):
    return 2*(t*240 - np.floor(1/2+t*240))

axa_hz = np.linspace(0, 1, 1600)
axa_real = np.linspace(0, 1, 20000)

fig, axs = plt.subplots(1)

fig.suptitle("Exercițiul 2 c")

axs.plot(axa_real, f_c(axa_real))
axs.stem(axa_hz, f_c(axa_hz))

axs.set_xlim([0, 0.01])

plt.savefig("./fig/lab1_ex2_c.pdf")

#d

def f_d(t):
    return np.sign(np.sin(2*np.pi*300*t))

axa_real = np.linspace(0, 1, 20000)

fig, axs = plt.subplots(1)

fig.suptitle("Exerciuțiul 2 d - Square")

axs.plot(axa_real, f_d(axa_real))

axs.set_xlim([0,0.008])

plt.savefig("./fig/lab1_ex2_d.pdf")
plt.show()



# e

s2d = np.random.rand(128, 128)
plt.imshow(s2d)

plt.title("Exercitiul 2.e")

plt.savefig("./fig/lab1_ex2_e.pdf")

plt.show()


# f

s2d = np.ones((128, 128))

plt.imshow(s2d)

plt.title("Exercitiul 2.f")

plt.savefig("./fig/lab1_ex2_f.pdf")

plt.show()