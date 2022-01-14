tendem = str(input("Nhap ten dem: "))
ten=str(input("Nhap ten: "))
n = int(input("Nhap n : "))
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return total
print(tendem)
print("Tổng", n, "là", totalDigitsOfNumber(n))