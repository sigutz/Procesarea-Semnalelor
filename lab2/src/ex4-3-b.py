import scipy.io.wavfile
import sounddevice as sdd
import numpy as np

fs=44100

rate, sd_array = scipy.io.wavfile.read("lab2_ex4_1.wav")

sdd.play(sd_array, fs)

sdd.wait()