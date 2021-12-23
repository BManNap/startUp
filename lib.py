from tkinter import *
import os
def openSSH(username, ip):
    os.system(f"gnome-terminal -- ssh {username}@{ip}")
    pass
def openVsCode(loc=""):
    os.system(f"code {loc}")
    pass
def shutdown(extraS=""):
    os.system(f"gnome-terminal -- echo EL501179 | sudo -S apt-get update & sudo -S apt-get upgrade & sudo shutdown {extraS} ")
    pass
def openFireFox():
    os.system("firefox")
    pass
def openSpotify():
    os.system("spotify")
    pass