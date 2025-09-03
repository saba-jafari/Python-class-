from PIL import ImageTk, Image
import tkinter as tk
from tkinter import *

def get_data():
    pass
#window creation
window = tk.Tk()
window.title("Plate Checker")
window.geometry("1000x200")

#loading photo with PIL
plate_image = Image.open("plate.jpg")
plate_image = ImageTk.PhotoImage(plate_image)

label_ = tk.Label(window, image=plate_image)
label_.place(x=50, y=20, width=400, height=150)

Button(window, image=plate_image, command=get_data).place(x=20, y=20)












window.mainloop()

