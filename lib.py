from tkinter import *
import os
def openSSH(username, ip):
    os.system(f"gnome-terminal -- ssh {username}@{ip}")
    pass
def openVsCode(loc=""):
    os.system(f"code {loc}")
    pass
def shutdown(extraS=""):
    global disCoke
    os.system(f"gnome-terminal -- sudo -S apt-get update & sudo -S apt-get upgrade & sudo shutdown {extraS}")
    disCoke = Label(text="Shutdown started")
    disCoke.place(relx=0.8, rely=0.3, anchor=CENTER)
    pass
def cancelShutdown():
    os.system("shutdown -c")
    disCoke.place_forget()
    pass
def openFireFox():
    os.system("firefox")
    pass
def openSpotify():
    os.system("spotify")
    pass