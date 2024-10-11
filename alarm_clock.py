from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


window = Tk()
window.title('Будильник')
window.config(bg='white')

label = Label(window, text='Напоминание', font=('Arial', 16), bg='white')
label.pack(pady=10)
set_button = Button(window, text='Установить напоминание', font=('Arial', 14), command=set)
set_button.pack(padx=10, pady=(0, 10))

window.mainloop()
