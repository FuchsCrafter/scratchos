# ScratchOS logging module
# Copyright 2021 fuchscrafter.de, GNU GPL 3 license, support(at)fuchscrafter.de
# DONT TUCH ANYTHING IF YOU DONT KNOW EXACTLY WAHT YOU ARE DOING!


import time
import os, sys


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