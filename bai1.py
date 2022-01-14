ten = str(input("Nhap ten: "))
n = int(len(ten))
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print("Ten cua ban la:",ten)
print("ki tu".format(ten, n))
print(d)