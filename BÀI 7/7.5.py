print("luong dinh anh")
print("mssv235752021610008")
def append_text_to_file(file_path, text):
    with open(file_path, 'a', encoding='utf-8') as file:  # Thêm encoding='utf-8'
        file.write(text + '\n')  # Thêm một dòng mới
    print("Nội dung đã thêm vào tệp.")

# Ví dụ sử dụng
append_text_to_file('file.txt', 'Nội dung mới')  # Thay 'file.txt' và nội dung bạn muốn thêm
