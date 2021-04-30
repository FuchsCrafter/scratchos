# ScratchOS setup file. 
# Copyright 2021 fuchscrafter.de, GNU GPL 3 license, support(at)fuchscrafter.de
# DONT TUCH ANYTHING IF YOU DONT KNOW EXACTLY WAHT YOU ARE DOING!

import tkinter as tk
import os, sys
import sqlite3
import time

# Logfile setup
logfile = open("SYSLOG.log", "w")
newtext = ("""
===========================================================================
SCRATCHOS
LOGFILE
Datum: """ + time.asctime() + """
===========================================================================
""")
logfile.writelines(newtext)
logfile.close()
def addlog(newtext):
    logfile = open("SYSLOG.log", "a")
    addtext = time.asctime(), " : ", newtext, "\n"
    logfile.writelines(addtext)
    logfile.close()
def copylog():
    logfile = open("SYSLOG.log", "r")
    tmplog = logfile.readlines()
    logfile.close()
    errlogf = open("system/crash.log", "w")
    errlogf.writelines(tmplog)
    errlogf.close()
    
# from sys32.logging import *

# Variablen
logourl = "system/assets/icon.png"
iconurl ="system/assets/icon.ico"
mainfont = "Arial"
datenpfad = "system/USERDATA"

# Begruessung
print("""
╭╮╭╮╭╮╭╮╭╮╭╮
┃┃┃┃┃┃┃┃┃┃┃┃
┃┃┃┃┃┣┫┃┃┃┃┃╭┳━━┳╮╭┳╮╭┳━━┳━╮       ╭━━━┳╮╭╮
┃╰╯╰╯┣┫┃┃┃┃╰╯┫╭╮┃╰╯┃╰╯┃┃━┫╭╮╮      ┣━━┃┃┃┃┃
╰╮╭╮╭┫┃╰┫╰┫╭╮┫╰╯┃┃┃┃┃┃┃┃━┫┃┃┃      ┃┃━━┫╰╯┃
 ╰╯╰╯╰┻━┻━┻╯╰┻━━┻┻┻┻┻┻┻━━┻╯╰╯      ╰━━━┻━━╯
 ██████╗░█████╗░██████╗░░█████╗░████████╗░█████╗░██╗░░██╗░░█████╗░░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░██║░██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██████╔╝███████║░░░██║░░░██║░░╚═╝███████║░██║░░██║╚█████╗░
░╚═══██╗██║░░██╗██╔══██╗██╔══██║░░░██║░░░██║░░██╗██╔══██║░██║░░██║░╚═══██╗
██████╔╝╚█████╔╝██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║░╚█████╔╝██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░╚════╝░╚═════╝░ """)
print("Benutzeroberfläche lädt...")
addlog("Laden der Benutzeroberfläche...")

def destroySetupscreen():
    setupscr.destroy()

def destroyLogin():
    loginscr.destroy()

# Datebank funktion
def addDemouser():
    global datenbankpfad
    datenbankpfad = datenpfad + "/USERS.db"
    addlog("Pfad der Datenbank:"+ datenbankpfad)

    if os.path.exists(datenbankpfad):
        addlog("Datenbank existiert schon, Nutzer werden nicht erzeugt")
    else:
        print("Die datenbank existiert nicht und wird deswegen erzeugt. Brechen sie das Programm nicht ab.")
        addlog("Nutzer werden erzeugt.")

        addlog("Datenbank wird erzeugt...")

        addlog("Verbindung zur Datenbank wir hergestellt")
        connection = sqlite3.connect(datenbankpfad)
        cursor = connection.cursor()
        addlog("Verbindung erfolgreich hergestellt")

        addlog("Datenbank wird erzeugt")
        sql = "CREATE TABLE user (" \
              "username TEXT," \
              "userkey INTEGER PRIMARY KEY, " \
              "password TEXT)"
        cursor.execute(sql)
        addlog("Datenbank wurde erzeugt.")

        addlog("Demo-Nutzer wird hinzugefügt")
        # Nutzer erzeugen
        sql = "INSERT INTO user VALUES ('ScratchOS', 12345, 'ScratchOS!')"
        cursor.execute(sql)
        connection.commit()
        addlog("Demo-Nutzer erfolgreich hinzugefügt.")

        print("""
        Die Datenbank wurde erzeugt. Es wurde ein Neuer Nutzer mit folgenden Daten angelegt:
            NUTZERNAME: ScratchOS
            PASSWORT: ScratchOS!
            NUTZER-ID: 12345
        Sie können sich nun mit diesen daten einloggen. Die Verbindung zur Datenbank wird jetzt geschlossen.       
        """)
        connection.close()
        addlog("Datenbank-Verbindung erfolgreich geschlossen.")

# Setupscreen funktion
def setupscreen():
    # Startup-Benutzeroberflaeche
    global setupscr
    setupscr = tk.Tk(className=" ScratchOS Startup screen") # setupscr ist das setup fenster
    addlog("Setup: Fenster geladen.")
    setupscr.geometry("500x250") # Groesse des fensters
    addlog("Setup: Fenstergröße festgelegt.")
    tk.Tk.resizable(setupscr, width=False, height=False) # fenster soll man nich verändern
    addlog("Setup: Fenstergröße als nicht veränderbar festgelegt.")
    addlog("Setup: Fenster geladen.")


    # Logo definieren und packen
    addlog("Setup: Logo laden...")
    setuplogo = tk.Label(setupscr)
    logo = tk.PhotoImage(file=logourl)
    addlog("Setup: Logo geladen.")
    addlog("Setup: Logo anzeigen...")
    setuplogo["image"] = logo
    setuplogo.pack()
    addlog("Setup: Logo fertig gepackt.")

    # Labels definieren und packen
    addlog("Setup: Labels laden...")
    tk.Label(setupscr, text="ScratchOS", font="Arial 15 bold").pack(pady=0, padx=0)
    tk.Label(setupscr, text="Willkommen!", font="Arial 11").pack(pady=0, padx=0)
    addlog("Setup: Labels geladen")

    # Login laden

    addlog("Setup: Loginbutton wird geladen...")
    btn = tk.Button(text="LOGIN", font="Arial 12", bd=2, command=destroySetupscreen)
    btn.pack()
    addlog("Setup: Loginbutton geladen.")

    tk.Label(setupscr, text="Website: http://scratchos.fuchscrafter.de", font="Arial 11").pack(pady=20, padx=0)

    # Fenster mainloop
    addlog("Setup: Fenster Mainloop ausführen")
    # setupscr.iconbitmap('') 

    setupscr.mainloop()

# Loginscreen funktion
def loginscreen():
    # Login-Benutzeroberflaeche
    global loginscr
    loginscr = tk.Tk(className="ScratchOS login") # loginscr ist das login fenster
    addlog("Login: Fenster geladen.")
    loginscr.geometry("500x300") # Groesse des fensters
    addlog("Login: Fenstergröße festgelegt.")
    tk.Tk.resizable(loginscr, width=False, height=False) # fenster soll man nich verändern
    addlog("Login: Fenstergröße als nicht veränderbar festgelegt.")
    addlog("Login: Fenster geladen.")

    # Logo definieren und packen
    addlog("Login: Logo laden...")
    loginlogo = tk.Label(loginscr)
    logo = tk.PhotoImage(file=logourl)
    addlog("Login: Logo geladen.")
    addlog("Login: Logo anzeigen...")
    loginlogo["image"] = logo
    loginlogo.pack()
    addlog("Login: Logo fertig gepackt.")

    # Labels definieren und packen
    addlog("Login: Labels laden...")
    tk.Label(loginscr, text="ScratchOS", font="Arial 15 bold").pack(pady=0, padx=0)
    global anzeige
    anzeige = tk.Label(loginscr, text="", font="Arial 11")
    anzeige.pack(pady=0, padx=0)
    addlog("Login: Labels geladen")

    # Eingaben
    global uname_e 
    global pswd_e

    tk.Label(loginscr, text="Nutzername: ", font="Arial 10").pack(pady=0, padx=0)
    uname_e = tk.Entry(loginscr)
    uname_e.pack()

    tk.Label(loginscr, text="Passwort: ", font="Arial 10").pack(pady=0, padx=0)
    pswd_e = tk.Entry(loginscr, show="*")
    pswd_e.pack()

    tk.Label(loginscr, text=" ", font="Arial 10").pack(pady=0, padx=0)

    btn = tk.Button(text="LOGIN!", command=loginfn, font="Arial 12 bold")
    btn.pack()

    loginscr.mainloop()

def loginfn():
    global loginSuccesfull
    loginSuccesfull = False
    try:
        enteredUname = uname_e.get()
        enteredPswd = pswd_e.get()
    except:
        enteredUname = " "
        enteredPswd = " "


    connection = sqlite3.connect(datenbankpfad)
    cursor = connection.cursor()
    
    try:
        sql = "SELECT password FROM user WHERE username = ?"
        cursor.execute(sql, (enteredUname,))
        for dsatz in cursor:
            password = dsatz[0]
        connection.close()
    except:
        print("Fehler!")

    if (enteredPswd == password):
        loginSuccesfull = True
        destroyLogin()
    else:
        anzeige["text"] = "Login inkorrekt!"
        loginSuccesfull = False

def checkpswd():
    if loginSuccesfull:
        startos()
    else:
        addlog("Unerwarteter Fehler! Bitte melde diesen Fehler auf dem Discord oder Auf GitHub. Eine Fehlerdatei wurde erzeugt.")
        anzeige["text"] = "Unerwarteter Fehler! Bitte melde \n diesen Fehler auf dem \n Discord oder Auf GitHub.\n Eine Fehlerdatei wurde \n erzeugt."
        print("Unerwarteter Fehler! Bitte melde \n diesen Fehler auf dem \n Discord oder Auf GitHub.\n Eine Fehlerdatei wurde \n erzeugt.")
        copylog()
        sys.exit(0)

def startos():
    destroyLogin()

# =========================================================================================================
# Main programm
setupscreen()
addDemouser()
loginscreen()
