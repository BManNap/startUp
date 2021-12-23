from tkinter import *
import os
def openSSH(username, ip):
    os.system(f"gnome-terminal -- ssh {username}@{ip}")
    pass
def openVsCode(loc=""):
    os.system(f"code {loc}")
    pass
def openFireFox():
    os.system("firefox")
    pass
def openSpotify():
    os.system("spotify")
    pass