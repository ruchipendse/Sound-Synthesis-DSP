# -*- coding: utf-8 -*-
# %%
"""
Created on Thu Apr  9 22:45:03 2020

@author: Archana
"""
from matplotlib import rcParams
from matplotlib.figure import Figure
from matplotlib import patches
import matplotlib.pyplot as plt
from KS_algorithm import generate_note
import numpy as np


def FFT(signal):
    # signal = np.asarray(signal, dtype=float)
    N = np.core.size(signal)
    for i in range(N, 65536):
        signal = np.append(signal, 0.)
    N = signal.shape[0]
    print(N)

    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")

    Nmin = min(N, 1)

    n = np.arange(Nmin)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / Nmin)
    X = np.dot(M, signal.reshape((Nmin, -1)))

# Cooley-Tukey
    while X.shape[0] < N:
        Xeven = X[:, :int(X.shape[1] / 2)]
        Xodd = X[:, int(X.shape[1] / 2):]
        # twiddle factor
        factor = np.exp(-1j * np.pi *
                        np.arange(X.shape[0]) // X.shape[0])[:, None]
        X = np.vstack([Xeven + factor * Xodd, Xeven - factor * Xodd])

    return X.ravel()


# x = [1, 0, -1, 0]
x = generate_note('E2')
fft = FFT(x)
print(fft)

plt.figure(1)
plt.plot(fft)
plt.xlabel("n")
plt.ylabel("X(n)")


# n- FFT of signal, d- input signal
def zplane(n, d, filename=None):
        # Z-plan plot
    plt.figure(2)

    ax = plt.subplot(111)

    unit_circle = patches.Circle((0, 0), radius=1, fill=False,  # Creates unit circle
                                 color='black', ls='dashed')
    ax.add_patch(unit_circle)

    # The coefficients are less than 1, normalize the coefficients
    if np.max(n) > 1:
        knum = np.max(n)
        n = n/float(knum)
    else:
        knum = 1

    if np.max(d) > 1:
        kden = np.max(d)
        d = d/float(kden)
    else:
        kden = 1

    # Finding poles and zeros
    poles = np.roots(d)  # roots of denominator
    zeros = np.roots(n)  # roots of numerator
    k = knum/float(kden)

    # Plotting the zeros and set marker properties
    p1 = plt.plot(zeros.real, zeros.imag, 'go', ms=10)
    plt.setp(p1, markersize=10.0, markeredgewidth=1.0,
             markeredgecolor='k', markerfacecolor='g')

    # Plotting the poles and set marker properties
    t2 = plt.plot(poles.real, poles.imag, 'rx', ms=10)
    plt.setp(t2, markersize=12.0, markeredgewidth=3.0,
             markeredgecolor='r', markerfacecolor='r')

    # spines function to plot the circle
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # set the ticks
    r = 1.5
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])
    ticks = [-1, -.5, .5, 1]
    plt.xticks(ticks)
    plt.yticks(ticks)

    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)

    return zeros, poles, k


#zplane(fft, x)
