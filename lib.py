from tk import *
import os
def openSSH(ip, password):
    os.system("gnome-terminal ssh pi@192.168.0.128 & disown")
    pass