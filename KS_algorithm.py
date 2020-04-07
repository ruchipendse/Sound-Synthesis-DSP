import numpy as np
import pyaudio
import time
import random
import wave
from collections import deque

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

p = pyaudio.PyAudio()  # instantiate PyAudio object


# note must be a string object e.g. generate_note('E2') or >>>note = 'E2' >>>generate_note
def generate_note(note):
    frequency = GuitarNotes.get(note)
    N = int(sampling_rate / frequency)
    ring_buffer = []
    for string in range(6):
        ring_buffer.append(
            np.zeros(string_buffer_sizes[string], dtype=np.float32))
    ring_buffer[X] = np.random.uniform(
        1, -1, string_buffer_sizes[string])  # X is supposed to be the array in ring buffer corresponding to the frequency given
