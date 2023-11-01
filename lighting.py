import tkinter as tk
import random
import time
from tkinter import *

def S1_set_green():
    lightbar_S1.config(background=flag_state1)
def S2_set_green():
    lightbar_S2.config(background=flag_state1)
def S3_set_green():
    lightbar_S3.config(background=flag_state1)    

def S1_set_yellow():
    lightbar_S1.config(background=flag_state2)
def S2_set_yellow():
    lightbar_S2.config(background=flag_state2)
def S3_set_yellow():
    lightbar_S3.config(background=flag_state2) 

def set_red():
    lightbar_S1.config(background=flag_state3)
    lightbar_S2.config(background=flag_state3)
    lightbar_S3.config(background=flag_state3)

def clear_red():
    lightbar_S1.config(background=flag_state2)
    lightbar_S2.config(background=flag_state2)
    lightbar_S3.config(background=flag_state2)
    
def All_green():
    lightbar_S1.config(background=flag_state1)
    lightbar_S2.config(background=flag_state1)
    lightbar_S3.config(background=flag_state1)
    
def Flag_test():
    ()

start_window_colour = "#121212"
start_text_colour = "#FFFFFF"
start_button_colour = "#404040"
start_frame_colour = "#282828"

flag_state1 = "green"
flag_state2 = "yellow"
flag_state3 = "red"

window = tk.Tk()

window.config(background=start_window_colour)

lightbar_S1 = tk.Label(width=60, height=3,
                    background=flag_state2,
                    bd=2)
lightbar_S1.grid(row=0, column=0)

lightbar_S2 = tk.Label(width=60, height=3,
                    background=flag_state2,
                    bd=2)
lightbar_S2.grid(row=0, column=1)

lightbar_S3 = tk.Label(width=60, height=3,
                    background=flag_state2,
                    bd=2)
lightbar_S3.grid(row=0, column=2)

spacer = Label(text=" ",
               height=5,
               background=start_window_colour)
spacer.grid(row=1)

flagSetGreen_btn1 = tk.Button(background=start_button_colour,
                             text="Green Flag",
                             foreground=start_text_colour,
                             command=S1_set_green)
flagSetGreen_btn1.grid(row=2, column=0)

flagSetGreen_btn2 = tk.Button(background=start_button_colour,
                             text="Green Flag",
                             foreground=start_text_colour,
                             command=S2_set_green)
flagSetGreen_btn2.grid(row=2, column=1)

flagSetGreen_btn3 = tk.Button(background=start_button_colour,
                             text="Green Flag",
                             foreground=start_text_colour,
                             command=S3_set_green)
flagSetGreen_btn3.grid(row=2, column=2)

spacer = Label(text=" ",
               height=5,
               background=start_window_colour)
spacer.grid(row=3)

flagSetYellow_btn1 = tk.Button(background=start_button_colour,
                             text="Yellow Flag",
                             foreground=start_text_colour,
                             command=S1_set_yellow)
flagSetYellow_btn1.grid(row=4, column=0)

flagSetYellow_btn2 = tk.Button(background=start_button_colour,
                             text="Yellow Flag",
                             foreground=start_text_colour,
                             command=S2_set_yellow)
flagSetYellow_btn2.grid(row=4, column=1)

flagSetYellow_btn3 = tk.Button(background=start_button_colour,
                             text="Yellow Flag",
                             foreground=start_text_colour,
                             command=S3_set_yellow)
flagSetYellow_btn3.grid(row=4, column=2)

spacer = Label(text=" ",
               height=5,
               background=start_window_colour)
spacer.grid(row=5)

flagSetRed_btn = tk.Button(background=start_button_colour,
                             text="Red Flag",
                             foreground=start_text_colour,
                             command=set_red)
flagSetRed_btn.grid(row=6, column=1)

flagClearRed_btn = tk.Button(background=start_button_colour,
                             text="All Yellow Flag",
                             foreground=start_text_colour,
                             command=clear_red)
flagClearRed_btn.grid(row=6, column=0)

FlagSetGreenAll_btn = tk.Button(background=start_button_colour,
                                text="All Green Flag",
                                foreground=start_text_colour,
                                command=All_green)
FlagSetGreenAll_btn.grid(row=6, column=2)

spacer = Label(text=" ",
               height=5,
               background=start_window_colour)
spacer.grid(row=7)

FlagTest_btn = tk.Button(background=start_button_colour,
                         text="Flag Test",
                         foreground=start_text_colour,
                         command=Flag_test)
FlagTest_btn.grid(row=8, column=1)

window.attributes('-fullscreen', True)
mainloop()