import random, numpy
from threading import Thread

import matplotlib.pyplot as plt
from math import *

harmoniks = 8
maxfrequency = 1100
N1=256
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
    N = len(x)
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
    plt.plot(numpy.arange(N), fp, color='red')
    plt.grid('True', color='black')
    plt.show()


def calculatehalves(x):
    N=len(x)
    f1 = numpy.zeros(int(N / 2))

    def firsthalf(x2):
        N=len(x2)
        freal11 = [0 for i in range(int(N / 2))]
        freal12 = [0 for i in range(int(N / 2))]
        freal1 = [0 for i in range(N)]
        fimage11 = [0 for i in range(int(N / 2))]
        fimage12 = [0 for i in range(int(N / 2))]
        fimage1 = [0 for i in range(N)]
        for p in range(int(N / 2)):
            for m in range(int(N / 2)):
                freal11[p] += x2[2 * m + 1] * numpy.cos(4 * numpy.pi / N * p * m)
                fimage11[p] += x2[2 * m + 1] * numpy.sin(4 * numpy.pi / N * p * m)
                freal12[p] += x2[2 * m] * numpy.cos(4 * numpy.pi / N * p * m)
                fimage12[p] += x2[2 * m] * numpy.sin(4 * numpy.pi / N * p * m)
            freal1[p] = freal12[p] + freal11[p] * numpy.cos(2 * numpy.pi / N * p) - fimage11[p] * numpy.sin(
                2 * numpy.pi / N * p)
            fimage1[p] = fimage12[p] + fimage11[p] * numpy.cos(2 * numpy.pi / N * p) + freal11[p] * numpy.sin(
                2 * numpy.pi / N * p)
            f1[p] += (freal1[p] ** 2 + fimage1[p] ** 2) ** 0.5

    f2 = [0 for i in range(int(N / 2))]

    def secondhalf(x1):
        N = len(x1)
        freal111 = [0 for i in range(int(N / 2))]
        freal121 = [0 for i in range(int(N / 2))]
        freal11 = [0 for i in range(N)]
        fimage111 = [0 for i in range(int(N / 2))]
        fimage121 = [0 for i in range(int(N / 2))]
        fimage11 = [0 for i in range(N)]
        for p in range(int(N / 2)):
            for m in range(int(N / 2)):
                freal111[p] += x1[2 * m + 1] * numpy.cos(4 * numpy.pi / N * p * m)
                fimage111[p] += x1[2 * m + 1] * numpy.sin(4 * numpy.pi / N * p * m)
                freal121[p] += x1[2 * m] * numpy.cos(4 * numpy.pi / N * p * m)
                fimage121[p] += x1[2 * m] * numpy.sin(4 * numpy.pi / N * p * m)
            freal11[p + int(N / 2)] = freal121[p] - (
                    freal111[p] * numpy.cos(2 * numpy.pi / N * p) - fimage111[p] * numpy.sin(2 * numpy.pi / N * p))
            fimage11[p + int(N / 2)] = fimage121[p] - (
                    fimage111[p] * numpy.cos(2 * numpy.pi / N * p) + freal111[p] * numpy.sin(2 * numpy.pi / N * p))
            f2[p] += (freal11[p + int(N / 2)] ** 2 + fimage11[p + int(N / 2)] ** 2) ** 0.5

    t1 = Thread(target=firsthalf, args=(x,))
    t2 = Thread(target=secondhalf, args=(x,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    f = numpy.zeros(N)
    f = numpy.append(f1, f2)
    fig = plt.figure()
    plt.plot(numpy.arange(N), f, color='red')
    plt.grid('True', color='black')
    plt.show()


if __name__ == '__main__':
    xlen=[256, 512, 1024, 2048]
    for n in xlen:
        sigx = calculatelab1(n)
        calculatelab4(sigx)
        calculatehalves(sigx)
