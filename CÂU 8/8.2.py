print("luong dinh anh")
print("mssv235752021610008")
import turtle

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("lightblue")

    pen = turtle.Turtle()
    pen.color("red")
    pen.pensize(2)

    pen.circle(50)

    window.mainloop()

draw_circle()
