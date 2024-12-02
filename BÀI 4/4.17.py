print("luong dinh anh")
print("mssv235752021610008")
def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

# Nhập số n
n = int(input("Nhập số n: "))

# In ra các số có tổng ước số lớn hơn chính nó
for i in range(1, n):
    if tong_uoc_so(i) > i:
        print(i)
