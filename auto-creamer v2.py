import pygetwindow as gw
import sys
import os
import time
import pyautogui
import threading
import keyboard
from tkinter import *

stop_spam = False

def spam_hello_world():
    global stop_spam
    start_button.config(state='disabled')
    countdown_label.config(text='Spam Started')
    while not stop_spam:
        pyautogui.typewrite('Nigg8')
        pyautogui.press('enter')
        time.sleep(0.5)

def stop_program(): #easter egg
    global stop_spam
    keyboard.wait('5')
    stop_spam = True
    countdown_label.config(text='Spam Stopped')
    start_button.config(state='normal')  

def countdown():
    global stop_spam
    stop_spam = False
    for i in range(5, 0, -1):
        countdown_label.config(text=str(i))
        time.sleep(1)
    countdown_label.config(text='')
    spam_hello_world()


def start_spam():
    global spam_thread, stop_spam
     
    countdown_thread = threading.Thread(target=countdown)
    countdown_thread.start()
    stop_program_thread = threading.Thread(target=stop_program)
    stop_program_thread.start() 
        
def on_closing():
    global stop_spam
    stop_spam = True
    root.destroy()
  

root = Tk()
root.title('Auto Creamer V2')
root.configure(bg='#212121')
root.protocol('WM_DELETE_WINDOW', on_closing)
root.geometry('400x300')
root.resizable(False, False)
if getattr(sys, 'frozen', False):
    icon_directory = os.path.join(sys._MEIPASS, 'icon.ico')
else:
    icon_directory = 'icon.ico'
root.iconbitmap(icon_directory)

title_label = Label(root, text='Auto Creamer V2', font=('Segoe UI', 20), fg='white', bg='#212121')
title_label.place(relx=0.5, rely=0.3, anchor='center')

# Create the button
button_font = ("Segoe UI", 18)
button_bg = "#212121"
button_fg = "white"
button_hover_bg = "#333333"
button_hover_shadow = "#888888"
button_outline = 'black'

start_button = Button(root, text='START', font=button_font, bg=button_bg, fg=button_fg, activebackground=button_hover_bg, activeforeground=button_fg, borderwidth=2, relief='groove', command=start_spam)
start_button.place(relx=0.5, rely=0.5, anchor='center')

author_text = Label(root, text='Created by Panos and Tom', font=('Segoe UI', 10), fg='white', bg='#212121')
author_text.pack(side='bottom', pady=5)

countdown_label = Label(root, text='', font=('Segoe UI', 20), bg='#212121', fg='white')
countdown_label.place(relx=0.5, rely=0.7, anchor='center')

root.mainloop()