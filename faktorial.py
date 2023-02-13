import time
import sys


def faktorial_iteratif(n):
    hasil = 1
    for i in range(1, n+1):
        hasil = hasil * i
    return hasil


def faktorial_rekursif(n):
    if n == 1:
        return 1
    else:
        return n * faktorial_rekursif(n-1)


start = time.time()
faktorial_iteratif(900)
end = time.time()
print("iteratif", end-start)

start = time.time()
faktorial_rekursif(900)
end = time.time()
print("rekursif", end-start)
