import numpy as np
import simpleaudio as sa
import wave
from matplotlib import pyplot as plt


GuitarNotes = {'E2': 82, 'A2': 110, 'D3': 147, 'G3': 196, 'B3': 247, 'E4': 330}
sample_width = 2
channels = 1
sampling_rate = 44100
total_samples = 44100
dampening_factor = 0.995

# show plot of algorithm in action
show_plot = False

# note must be a string object e.g. generate_note('E2') or >>>note = 'E2' >>>generate_note


def generate_note(note):
    frequency = GuitarNotes.get(note)
    ring_buffer = np.random.uniform(1, -1, frequency)
    output = np.zeros(total_samples, dtype='float32')

    # plot of flag set
    if show_plot:
        axline, = plt.plot(ring_buffer)

    for i in range(total_samples):
        output[i] = ring_buffer[0]
        average = dampening_factor * 0.5 * (ring_buffer[0] + ring_buffer[1])
        ring_buffer = np.append(ring_buffer, average)
        ring_buffer = np.delete(ring_buffer, 0)
        # plot of flag set
        if show_plot:
            if (49*frequency < i) and (i < 50*frequency):
                axline.set_ydata(ring_buffer)
                plt.draw()

    return output


# Write WAV file for audio
def write_WAV(filename, data):
    # Add appropriate extension to filename
    filename = filename + '.wav'

    # Open file in write mode
    file = wave.open(filename, 'wb')

    # Set file parameters
    file.setparams((channels, sample_width, sampling_rate,
                    total_samples, 'NONE', 'noncompressed'))

    # Convert data to string and enter into file
    data = np.array(data * 32767, 'int16')
    file.writeframes(data.tostring())
    # Close file
    file.close()

# Function to play NUMPY ARRAY


def playback_array(sequence):
    # Convert numpy array to byte stream for PyAudio, and scale to a int16 value
    sequence = np.array(sequence * 32767, 'int16')   # 32767 = (2^15) - 1

    # Start Playback
    # play_buffer((audio_data, num_channels, bytes_per_sample, sample_rate))
    play_obj = sa.play_buffer(sequence, channels, sample_width, sampling_rate)

    # Wait for playback to finish before exiting
    play_obj.wait_done()


# Function to play WAV file from Folder
def playback_WAV(fname):
    path = "****" + fname # ENTER PATH FOR AUDIO FILES INSIDE DOUBLE QUOTES
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    # play_obj.wait_done()
