import numpy as np
import pyaudio
import time
import random
import wave
from matplotlib import pyplot as plt

# Guitar string frequencies are
# E2 = 82(.41) Hz,
# A2 = 110 Hz,
# D3 = 147 (146.8) Hz,
# G3 = 196 Hz,
# B3 = 247 (246.9) Hz, and
# E4 = 330 (329.6) Hz.

GuitarNotes = {'E2': 82, 'A2': 110, 'D3': 147, 'G3': 196, 'B3': 247, 'E4': 330}
# array containing buffer lengths for each frequency-
string_buffer_sizes = [82, 110, 147, 196, 247, 330]

sample_width = 2
channels = 1
sampling_rate = 44100
total_samples = 44100
dampening_factor = 0.995

# show plot of algorithm in action?
gShowPlot = False

p = pyaudio.PyAudio()  # instantiate PyAudio object


# note must be a string object e.g. generate_note('E2') or >>>note = 'E2' >>>generate_note
def generate_note(note):
    frequency = GuitarNotes.get(note)
    #N = int(sampling_rate / frequency)
    ring_buffer = np.random.uniform(-1, 1, frequency)
    output = np.zeros(total_samples, dtype=np.float32)

    # plot of flag set
    if gShowPlot:
        axline = plt.plot(ring_buffer)

    for i in range(total_samples):
        output[i] = ring_buffer[0]
        average = dampening_factor * 0.5 * (ring_buffer[0] + ring_buffer[1])
        ring_buffer = np.append(ring_buffer, average)
        ring_buffer = np.delete(ring_buffer, 0)
        # plot of flag set
        if gShowPlot:
            if i % 1000 == 0:
                axline.set_ydata(ring_buffer)
                plt.draw()

    # output = np.array(output * 32767, 'int16')
    # return output.tostring()


generate_note('E2')
