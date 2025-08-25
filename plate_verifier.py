import re
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

#function for geting data and checking with regex
def check_plate():
    part1 = entry1.get().strip()
    part2 = entry2.get().strip()
    part3 = entry3.get().strip()
    part4 = entry4.get().strip()

    plate = f"{part1}{part2}{part3}{part4}"
    pattern = r"^\d{2}[آ-ی]\d{3}\d{2}$"

    if re.match(pattern, plate):
        messagebox.showinfo("نتیجه", f"پلاک معتبر است:\n{plate}")
    else:
        messagebox.showerror("خطا!", "پلاک نامعتبر")


# window creation
window = tk.Tk()
window.title("Plate Checker")
window.geometry("1000x500")


# loading photo with PIL
plate_image = Image.open("plate.JPG")
plate_image = plate_image.resize((960, 400))
plate_image = ImageTk.PhotoImage(plate_image)

label_ = tk.Label(window, image=plate_image)
label_.place(x=20, y=20, width=960, height=400)


# entry
entry1 = tk.Entry(window, textvariable=tk.StringVar(), font=("B Traffic", 70))
entry1.place(x=120, y=60, width=150, height=320)
entry2 = tk.Entry(window, textvariable=tk.StringVar(), font=("B Traffic", 70))
entry2.place(x=270, y=60, width=140, height=320)
entry3 = tk.Entry(window, textvariable=tk.StringVar(), font=("B Traffic", 70))
entry3.place(x=410, y=60, width=340, height=320)
entry4 = tk.Entry(window, textvariable=tk.StringVar(), font=("B Traffic", 70))
entry4.place(x=780, y=125, width=160, height=250)


#Button for checking the plate
check_button = tk.Button(window, text="بررسی", font=("B Traffic", 20), command=check_plate)
check_button.place(x=10, y=420)


window.mainloop()
