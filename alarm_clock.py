from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set_reminder():
    global t
    rem = sd.askstring('Время напоминания',
                       'Введите время в формате: чч:мм (в 24-часовом формате)').split(':')
    if rem:
        try:
            hour, minute = int(rem[0]), int(rem[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute)
            t = dt.timestamp()
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка: {e}!')


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
    window.after(10000, check)


def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()


t = 0
window = Tk()
window.title('Будильник')
window.config(bg='white')

label = Label(window, text='Напоминание', font=('Arial', 16), bg='white')
label.pack(pady=10)
set_button = Button(window, text='Установить напоминание', font=('Arial', 14), command=set_reminder)
set_button.pack(padx=10, pady=(0, 10))

check()

window.mainloop()
