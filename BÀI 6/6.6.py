print("luong dinh anh")
print("mssv235752021610008")
class StringHandler:
    def get_String(self):
        self.user_string = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.user_string.upper())

# Ví dụ sử dụng
handler = StringHandler()
handler.get_String()
handler.print_String()
