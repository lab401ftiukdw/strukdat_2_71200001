import random
import timeit


def generate_list(n):
    batas_atas = n*100
    randomlist = random.sample(range(0, batas_atas), n)
    randomlist.sort()
    return randomlist


def cari_pasangan(data, target):
    for i in range(0, len(data)-1):
        for j in range(0, len(data)):
            if data[i]+data[j] == target:
                print("ketemu")
                return True
    return False


target = -100
for i in range(5000, 55000, 5000):
    data = generate_list(i)
    start = timeit.default_timer()
    hasil = cari_pasangan(data, target)
    end = timeit.default_timer()
    print('Ukuran ', i, ': ', end-start, ' second.')
