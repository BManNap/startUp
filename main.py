import tk
from lib import *
from tkinter import *

root = Tk()
root.geometry("500x500")
root.config(bg="#957DAD")

def main():
    piSSH = Button(root, text="Pi SSH", bg="#FEC8D8", highlightthickness = 0, bd = 0,command=lambda:openSSH("192.168.0.128"))
    piSSH.grid(row=1, column=1)
    pass

if __name__ == '__main__':
    main()
    root.mainloop()
