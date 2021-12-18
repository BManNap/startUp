from tkinter import *
import os
def openSSH(ip):
    os.system(f"gnome-terminal -- ssh pi@{ip}")
    pass