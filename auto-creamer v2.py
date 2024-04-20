import pygetwindow as gw
import time
import pyautogui
import threading
import keyboard
from tkinter import *

stop_spam = False

def is_discord_open():
    discord_windows = gw.getWindowsWithTitle('Discord')
    return len(discord_windows) > 0

def spam_hello_world():
    global stop_spam
    countdown_label.config(text='Spam Started')
    while not stop_spam:
        if is_discord_open():
            pyautogui.typewrite('Nigg8')
            pyautogui.press('enter')
        time.sleep(0.5)

def stop_program(): #easter egg
    global stop_spam
    keyboard.wait('5')
    stop_spam = True
    countdown_label.config(text='Spam Stopped')

def countdown():
    global stop_spam
    stop_spam = True
    if not is_discord_open():
        countdown_label.config(text='Open Discord')
        return
    for i in range(5, 0, -1):
        countdown_label.config(text=str(i))
        time.sleep(1)
    stop_spam = False
    countdown_label.config(text='')
    spam_thread = threading.Thread(target=spam_hello_world)
    spam_thread.start()


def start_spam():
    global spam_thread
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
root.protocol('WM_DELETE_WINDOW', on_closing)

start_button = Button(root, text='START', font=('Arial', 24), width=10, height=3, command=start_spam)
start_button.pack(pady=20)

countdown_label = Label(root, text='', font=('Arial', 24))
countdown_label.pack()


root.mainloop()