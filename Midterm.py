from tkinter import *
window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

btn = Button(window, text="Click to Change Color", fg="Black", activebackground="Yellow")
btn.place(x=190, y=200)

window.mainloop()