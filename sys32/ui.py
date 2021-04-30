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
    sysui = tk.Tk(className=" ScratchOS") # setupscr ist das setup fenster
    sysui.geometry("1000x650") # Groesse des fensters
    tk.Tk.resizable(sysui, width=False, height=False) # fenster soll man nich verändern
    # Fenster mainloop
    # setupscr.iconbitmap('') 

    sysui.mainloop()

startUI()
