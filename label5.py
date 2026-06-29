from tkinter import *

root = Tk()

photo = PhotoImage(file=r"C:\Users\parke\OneDrive\바탕 화면\bug\logo.png")

w = Label(root, image = photo, justify = "left").pack(side = 'right')

message = """앙기모띠 무하하하하하하 야르
응
네
와우
네"""

w2 = Label(root, padx = 50, text = message).pack(side = "left")

root.mainloop()