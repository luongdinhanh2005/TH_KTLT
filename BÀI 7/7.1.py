print("luong dinh anh")
print("mssv235752021610008")
def reverse_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content[::-1])  # Đảo ngược nội dung

# Ví dụ sử dụng
reverse_file_content('file.txt')  # Thay 'file.txt' bằng tên file của bạn
