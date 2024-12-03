import tkinter as tk  # Thư viện Tkinter để tạo giao diện đồ họa

print("luong dinh anh")
print("mssv235752021610008")
import tkinter as tk

def on_button_click():
    print("Button clicked!")

window = tk.Tk()
window.title("My Window")

button = tk.Button(window, text="Click Me", command=on_button_click, bg="blue", fg="white")
button.pack(pady=20)

window.mainloop()
