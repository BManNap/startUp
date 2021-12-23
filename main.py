from lib import *
from tkinter import *

root = Tk()
root.geometry("500x250")
root.config(bg="#957DAD")

def main():
    #title
    Name = Label(root, text="TeddyBear", height=1, width=25)
    Name.place(relx=0.5, rely=0.3, anchor=CENTER)
    
    #Terminal related openning
    piSSH = Button(root, text="Pi SSH",height=1, width=10, bg="#E0BBE4", highlightthickness =0, bd =0, highlightbackground="black", command=lambda:openSSH("pi", "192.168.0.128"))
    piSSH.place(relx = 0.4, rely = 0.4, anchor = CENTER)
    
    #editor related openning
    vsCode = Button(root, text="vsCode",height=1, width=10, bg="#FFA6C9", highlightthickness =0, bd =0, highlightbackground="black",command=lambda:openVsCode())
    vsCode.place(relx=0.4, rely=0.5, anchor=CENTER)

    #turn off related stuff
    turnOff = Button(root, text="Shutdown",height=1, width=10, bg="#FEC8D8", highlightthickness =0, bd =0, highlightbackground="black", command=lambda:shutdown())
    turnOff.place(relx = 0.6, rely = 0.6, anchor = CENTER)
    restart = Button(root, text="restart",height=1, width=10, bg="#FEC8D8", highlightthickness =0, bd =0, highlightbackground="black", command=lambda:shutdown("-r"))
    restart.place(relx = 0.4, rely = 0.6, anchor = CENTER)

if __name__ == '__main__':
    main()
    root.mainloop()
