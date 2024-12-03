print("luong dinh anh")
print("mssv235752021610008")
class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ' '.join(self.text.split()[::-1])

# Ví dụ sử dụng
reverser = ReverseWords('hello .py')
print("Chuỗi đảo ngược:", reverser.reverse())
