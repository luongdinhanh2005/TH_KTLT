print("luong dinh anh")
print("mssv235752021610008")
import math

# Khởi tạo vị trí ban đầu của robot tại (0,0)
pos = [0, 0]

# Sử dụng vòng lặp để nhận dữ liệu đầu vào
while True:
    s = input("Nhập lệnh di chuyển (hoặc bấm Enter để dừng): ")
    if not s:  # Nếu không có dữ liệu đầu vào thì thoát khỏi vòng lặp
        break

    # Tách chuỗi thành hướng di chuyển và số bước
    movement = s.split(" ")
    direction = movement[0].upper()  # Chuyển hướng thành chữ hoa
    steps = int(movement[1])  # Chuyển số bước thành kiểu số nguyên

    # Cập nhật vị trí của robot dựa vào hướng di chuyển
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps

# Tính khoảng cách từ vị trí hiện tại đến vị trí ban đầu
distance = int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2)))

# In ra kết quả
print(f"Khoảng cách từ vị trí hiện tại đến vị trí ban đầu là: {distance}")
