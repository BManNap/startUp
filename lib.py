from tkinter import *
import os
def openSSH(username, ip):
    os.system(f"gnome-terminal -- ssh {username}@{ip} & disown")
    pass
def openVsCode(loc=""):
    os.system(f"code {loc} & disown")
    pass
def openFireFox():
    os.system("firefox & disown")
    pass
def openSpotify():
    os.system("spotify & disown")
    pass
def openDiscord():
    os.system("discord & disown")
    pass