print("luong dinh anh")
print("mssv235752021610008")
# Nhập chuỗi các số cách nhau bởi dấu phẩy
so_dau_vao = input("Nhập các số cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số và chuyển sang kiểu int
danh_sach_so = list(map(int, so_dau_vao.split(',')))

# Lọc các số lẻ
so_le = [str(num) for num in danh_sach_so if num % 2 != 0]

# In các số lẻ, cách nhau bởi dấu phẩy
print(",".join(so_le))
