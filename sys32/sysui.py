# ScratchOS ui module.
# Copyright 2021 fuchscrafter.de, GNU GPL 3 license, support(at)fuchscrafter.de
# DONT TUCH ANYTHING IF YOU DONT KNOW EXACTLY WAHT YOU ARE DOING!

import tkinter as tk
import os, sys
import sqlite3
import time



def destroySetupscreen():
    sysui.destroy()

def startUI():
    # Startup-Benutzeroberflaeche
    global sysui
    sysui = tk.Tk() # setupscr ist das setup fenster
    sysui.title('ScratchOS')
    sysui.geometry("1000x650") # Groesse des fensters
    tk.Tk.resizable(sysui, width=False, height=False) # fenster soll man nich verändern

    topmenubar = tk.Frame(sysui, width="500px", height="10px", relief="sunken", bd=1)
    topmenubar.grid(row=0, column=0, columnspan=3, sticky="we")

    tk.Button(topmenubar, text="1").grid(row=0, column=0)
    tk.Button(topmenubar, text="2").grid(row=0, column=1)


    # Fenster mainloop
    # setupscr.iconbitmap('') 

    sysui.mainloop()

startUI()
