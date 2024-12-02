print("luong dinh anh")
print("mssv235752021610008")
S = input("Nhập chuỗi: ")
for ch in S:
    if ch not in [' ', '\t']:  # Bỏ qua các ký tự không nhìn thấy
        print(ch)
