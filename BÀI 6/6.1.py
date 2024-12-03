import math
print("luong dinh anh")
print("mssv235752021610008")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Ví dụ sử dụng
circle = Circle(5)
print("Diện tích hình tròn:", circle.area())
