import numpy
import matplotlib.pyplot as plt

def x(t ):
    return numpy.cos(520*numpy.pi*t + numpy.pi/3)

def y(t):
    return numpy.cos(280*numpy.pi*t - numpy.pi/3)

def z(t ):
    return numpy.cos(120*numpy.pi*t + numpy.pi/3)

# a
axa = numpy.linspace(0,0.03, 60)

#b
n=3

fig, axs = plt.subplots(n)
fig.suptitle("Titlu")
axs[0].plot(axa, x(axa))
axs[1].plot(axa, y(axa))
axs[2].plot(axa, z(axa))

for ax in axs.flat:
    ax.set_xlim([0, 0.03])

plt.savefig("./fig/lab1_ex1_b.pdf")

#c
axa_hz = numpy.linspace(0,1, 200)
axa_real = numpy.linspace(0,1, 20000)
n=3

fig, axs = plt.subplots(n)
fig.suptitle("Titlu")

axs[0].plot(axa_real, x(axa_real))
axs[0].stem(axa_hz, x(axa_hz))

axs[1].stem(axa_hz, y(axa_hz))
axs[1].plot(axa_real, y(axa_real))

axs[2].stem(axa_hz, z(axa_hz))
axs[2].plot(axa_real, z(axa_real))

for ax in axs.flat:
    ax.set_xlim([0, 0.05])

plt.savefig("./fig/lab1_ex1_c.pdf")

plt.show()