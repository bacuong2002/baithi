ten = str(input("Nhập Họ tên: "))
n = int(input("Nhập n : "))
print("Tên của bạn:", ten)
str1 = str(n)
str2 = str1[::-1]
if str1 == str2:
    print("đây là số thuần nghịch")
else:
    print("đây không là số thuần nghịch")