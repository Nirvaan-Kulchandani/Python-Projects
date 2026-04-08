# A Digital Clock

from tkinter import *
import datetime

root = Tk()
root.geometry("300x150")
root.title("Digital Clock")
root.config(bg="lime")

def update_clock():
    current_time = datetime.datetime.now()
    hr_time = current_time.hour
    min_time = current_time.minute
    sec_time = current_time.second

    clock_lbl.config(text=f"{hr_time:02}:{min_time:02}:{sec_time:02}")
    root.after(1000, update_clock)  # Update every second

hr_time = datetime.datetime.now().hour
min_time = datetime.datetime.now().minute
sec_time = datetime.datetime.now().second

clock_lbl = Label(root, font=("Algerian", 50), bg="brown", fg="aquamarine")
clock_lbl.pack(pady=20)
update_clock()  # Start the clock update loop
clock_lbl.config(text=f"{hr_time:02}:{min_time:02}:{sec_time:02}")


root.mainloop()