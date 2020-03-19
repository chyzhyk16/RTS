import random, numpy

import matplotlib.pyplot as plt
from math import *

harmoniks = 8
maxfrequency = 1100

midfrequency = maxfrequency / harmoniks


def calculatelab1(points):
    amplitude = [random.randint(1, 10) for i in range(harmoniks)]
    faza = [random.randint(1, 360) for i in range(harmoniks)]
    xlist = numpy.array([[(amplitude[n] * sin(midfrequency * (n + 1) * t + faza[n])) for t in range(points)] for n in
                         range(0, harmoniks)], float)
    singlex = numpy.zeros(points)
    for i in range(harmoniks):
        singlex = singlex + xlist[i]
    return singlex


def calculatelab3(x):
    N = x.shape[0]
    n = numpy.arange(N)
    k = n.reshape((N, 1))
    M = numpy.exp(-2j * numpy.pi * k * n / N)
    spectr = numpy.dot(M, x)
    rx = []
    ix = []
    for i in range(len(spectr)):
        rx.append(spectr[i].real)
        ix.append(spectr[i].imag)
    fp = numpy.array([sqrt(r ** 2 + i ** 2) for (r, i) in zip(rx, ix)])
    fig = plt.figure()
    plt.plot(numpy.arange(256), fp, color='red')
    plt.grid('True', color='black')
    plt.show()


if __name__ == '__main__':
    sigx = calculatelab1(256)
    calculatelab3(sigx)
