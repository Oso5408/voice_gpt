import sys
import os
import tkinter 
from tkinter import *

window= tkinter.Tk()

window.title=("Voice gpt")
window.geometry=("800x600")

def run():
    os.system('voice_gpt.py')


start_btn = Button(window, text="start voice", bg="black", fg="white", command=run)
start_btn.grid(column=0 , row=0)

window.mainloop()