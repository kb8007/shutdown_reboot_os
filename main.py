import tkinter as tk
from tkinter import messagebox
import os

main_window = tk.Tk()
main_window.title('Shutdown/Reboot OS')
main_window.geometry('300x100+500+230')

def shutdown_button_action():
    os.system("shutdown now -h")

def reboot_button_action():
    os.system('reboot')

shutdown_button = tk.Button(main_window, text='Shutdown', command=shutdown_button_action)
shutdown_button.config(height=1, width=10)
shutdown_button.place(x=30, y=30)

reboot_button = tk.Button(main_window, text='Reboot', command=reboot_button_action)
reboot_button.config(height=1, width=10)
reboot_button.place(x=165, y=30)

main_window.mainloop()
