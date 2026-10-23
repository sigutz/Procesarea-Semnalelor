import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sdd

def f_sin_a(t):
    return np.sin(2*np.pi*200*t)

def f_sin_b(t):
    return np.sin(2*np.pi*800*t)

fs = 44100
durata = 1

axa_real = np.linspace(0, durata, durata*fs)
axa_sin_a = f_sin_a(axa_real)
axa_sin_b = f_sin_b(axa_real)
rezultat_sin = np.concatenate((axa_sin_a, axa_sin_b))

sdd.play(rezultat_sin, fs)
sdd.wait()

# e un bipait mult mai inalt care zgarie pe urechi