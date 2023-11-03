import random as ran
import time as t
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import lighting

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

def openLightstest():
    exec(open('lighting.py').read())

main = tk.Tk()

main.config(background=start_window_colour)

lightTest_btn = tk.Button(background=start_button_colour,
                          foreground=start_text_colour,
                          command=openLightstest,
                          text="Lighting test")
lightTest_btn.pack(pady=50)

exit_btn = tk.Button(background=start_button_colour,
                     foreground=start_text_colour,
                     command=close,
                     text="Quit")
exit_btn.pack(pady=100)


main.attributes('-fullscreen', True)
mainloop()
