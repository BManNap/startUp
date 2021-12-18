from tkinter import *
import os
def openSSH(username, ip):
    os.system(f"gnome-terminal -- ssh {username}@{ip}")
    pass