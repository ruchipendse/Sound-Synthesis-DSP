from fft_function import FFT
from KS_algorithm import generate_note, write_WAV, playback_WAV
import tkinter as tk

'''Guitar string frequencies are
   E2 = 82(.41) Hz,
   A2 = 110 Hz,
   D3 = 147 (146.8) Hz,
   G3 = 196 Hz,
   B3 = 247 (246.9) Hz, and
   E4 = 330 (329.6) Hz.'''

song = ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']


def button1():
    playback_WAV('E2.wav')
    print("E2")


def button2():
    playback_WAV('A2.wav')
    print("A2")


def button3():
    playback_WAV('D3.wav')
    print("D3")


def button4():
    playback_WAV('B3.wav')
    print("B3")


def button5():
    playback_WAV('G3.wav')
    print("G3")


def button6():
    playback_WAV('E4.wav')
    print("E4")


def exit_app():
    print('Thank you for playing!')
    exit()


def all_buttons():
    for key in song:
        filename = key + '.wav'
        playback_WAV(filename)


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

b1 = tk.Button(frame, text="E2", fg="black", command=button1)
b1.pack(side=tk.LEFT, padx=10)
b2 = tk.Button(frame, text="A2", fg="black", command=button2)
b2.pack(side=tk.LEFT, padx=10)
b3 = tk.Button(frame, text="D3", fg="black", command=button3)
b3.pack(side=tk.LEFT, padx=10)
b4 = tk.Button(frame, text="G3", fg="black", command=button4)
b4.pack(side=tk.LEFT, padx=10)
b5 = tk.Button(frame, text="B3", fg="black", command=button5)
b5.pack(side=tk.LEFT, padx=10)
b6 = tk.Button(frame, text="E4", fg="black", command=button6)
b6.pack(side=tk.LEFT, padx=10)
b7 = tk.Button(frame, text="Play all", command=all_buttons)
b7.pack(side=tk.LEFT, padx=10)
b8 = tk.Button(frame, text="Exit", fg="black", command=exit_app)
b8.pack(side=tk.LEFT, padx=10)


root.mainloop()


''' The following is code for execution without the UI- 

for key in song:
   result = generate_note(key)
   filename = key + '.wav'
   playback_WAV(filename)
---------------------------------------------------------
# IMPORTANT! For first execution add:
# CODE FOR WRITING NEW .WAV FILES
# add this in the for loop
write_WAV(key, result)
___________________________________________________________
# CODE FOR GETTING FFT PLOTS
# initialize i before the for loop as -
# i = 1
# then inside for loop, put the following block of code
# fft_result = FFT(result)
# plt.figure(i)
# i += 1
# plt.plot(fft_result)
# plt.xlabel("n")
# plt.ylabel("X(n)")
____________________________________________________________
'''
