from tkinter import *

def button_clicked() :
    print("버튼 클릭야르")


root = Tk()
root.geometry("300x200")

button = Button(root, text="클릭해볼테냐", command=button_clicked)

button.pack()

root.mainloop()
