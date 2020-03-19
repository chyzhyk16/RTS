import random, numpy

import matplotlib.pyplot as plt
from math import *

harmoniks = 8
maxfrequency = 1100
N=256
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


def calculatelab4(x):
    freal11 = [0 for i in range(int(N / 2))]
    freal12 = [0 for i in range(int(N / 2))]
    freal1 = [0 for i in range(N)]
    fimage11 = [0 for i in range(int(N / 2))]
    fimage12 = [0 for i in range(int(N / 2))]
    fimage1 = [0 for i in range(N)]
    fp = [0 for i in range(N)]
    for p in range(int(N / 2)):
        for m in range(int(N / 2)):
            freal11[p] += x[2 * m + 1] * numpy.cos(4 * numpy.pi / N * p * m)
            fimage11[p] += x[2 * m + 1] * numpy.sin(4 * numpy.pi / N * p * m)
            freal12[p] += x[2 * m] * numpy.cos(4 * numpy.pi / N * p * m)
            fimage12[p] += x[2 * m] * numpy.sin(4 * numpy.pi / N * p * m)
        freal1[p] = freal12[p] + freal11[p] * numpy.cos(2 * numpy.pi / N * p) - fimage11[p] * numpy.sin(
            2 * numpy.pi / N * p)
        fimage1[p] = fimage12[p] + fimage11[p] * numpy.cos(2 * numpy.pi / N * p) + freal11[p] * numpy.sin(
            2 * numpy.pi / N * p)
        freal1[p + int(N / 2)] = freal12[p] - (
                freal11[p] * numpy.cos(2 * numpy.pi / N * p) - fimage11[p] * numpy.sin(2 * numpy.pi / N * p))
        fimage1[p + int(N / 2)] = fimage12[p] - (
                fimage11[p] * numpy.cos(2 * numpy.pi / N * p) + freal11[p] * numpy.sin(2 * numpy.pi / N * p))
        fp[p] = (freal1[p] ** 2 + fimage1[p] ** 2) ** 0.5
        fp[p + int(N / 2)] = (freal1[p + int(N / 2)] ** 2 + fimage1[p + int(N / 2)] ** 2) ** 0.5
    fig = plt.figure()
    plt.plot(numpy.arange(256), fp, color='red')
    plt.grid('True', color='black')
    plt.show()


if __name__ == '__main__':
    sigx = calculatelab1(256)
    calculatelab4(sigx)
