print("luong dinh anh")
print("mssv235752021610008")
chuoi = input("Nhập chuỗi: ")
chuoi_khong_chu_so = ''.join([char for char in chuoi if not char.isdigit()])
print(chuoi_khong_chu_so)
