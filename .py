import random as ran
import time as t
from tkinter import *
import tkinter as tk
from tkinter import messagebox

start_window_colour = "#121212"
start_text_colour = "#FFFFFF"
start_button_colour = "#404040"
start_frame_colour = "#282828"

def close():
    quit_message = messagebox.askyesno("askquetion", "are you sure?")

    if quit_message == True:
        main.destroy()
    else:
        pass    

main = tk.Tk()

main.config(background=start_window_colour)

exit_btn = tk.Button(background=start_button_colour,
                     foreground=start_text_colour,
                     command=close)
exit_btn.pack(pady=100)

mainloop()
