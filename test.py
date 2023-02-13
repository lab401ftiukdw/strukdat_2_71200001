import time

start = time.time()

# algoritma yg mau diukur
nilai = 0
n = 100
for i in range(n):
    for j in range(n):
        nilai += i * 2
# selesai

end = time.time()
selisih = end - start

print("waktu yg diperlukan", selisih)
