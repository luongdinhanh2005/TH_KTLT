print("luong dinh anh")
print("mssv235752021610008")
import math

def Tinh(R):
    # Kiểm tra nếu bán kính là số dương
    if R > 0:
        # Tính chu vi hình tròn: C = 2 * π * R
        chu_vi = 2 * math.pi * R
        # Tính diện tích hình tròn: A = π * R^2
        dien_tich = math.pi * R ** 2
        print(f"Chu vi hình tròn với bán kính {R} là: {chu_vi:.2f}")
        print(f"Diện tích hình tròn với bán kính {R} là: {dien_tich:.2f}")
    else:
        print("Bán kính phải là một số dương.")

# Nhập giá trị bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính của hình tròn: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
