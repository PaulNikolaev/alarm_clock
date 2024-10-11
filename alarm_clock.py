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
            dt = now.replace(hour=hour, minute=minute, second=0)
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
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text='Установить новое напоминание.')


t = 0
music = False
window = Tk()
window.title('Будильник')
window.config(bg='white')

label = Label(window, text='Напоминание', font=('Arial', 16), bg='white')
label.pack(pady=10)
set_button = Button(window, text='Установить напоминание', width=25, font=('Arial', 14), command=set_reminder)
set_button.pack(padx=10, pady=(0, 10))

stop_button = Button(window, text='Остановить музыку', width=25, font=('Arial', 14), command=stop_music)
stop_button.pack(padx=10, pady=(0, 10))

check()

window.mainloop()
