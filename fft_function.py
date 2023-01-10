import numpy as np
from matplotlib import pyplot as plt


def FFT(signal):
    N = np.core.size(signal)
    for i in range(N, 65536):
        signal = np.append(signal, 0.)
    N = signal.shape[0]

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
