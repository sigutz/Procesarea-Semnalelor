import numpy as np
import sounddevice as sdd
import scipy.io.wavfile

fs = 44100

durata = 1

axa_hz = np.linspace(0,durata, durata*fs)

# a
def f_a(t):
    return np.sin(2*np.pi*400*t)

sd_array = f_a(axa_hz)

sdd.play(sd_array, fs)

sdd.wait()

# b

def f_b(t):
    return np.sin(2*np.pi*800*t)

sd_array = f_b(axa_hz)
sdd.play(sd_array, fs)
sdd.wait()

#c

def f_c(t):
    return 2*(t*240 - np.floor(1/2+t*240))

sd_array = f_c(axa_hz)
sdd.play(sd_array, fs)
sdd.wait()

#d
def f_d(t):
    return np.sign(np.sin(2*np.pi*300*t))

sd_array = f_d(axa_hz)
sdd.play(sd_array, fs)

rate = int(10e5)
scipy.io.wavfile.write("lab2_ex4_1.wav", rate, sd_array)

sdd.wait()
