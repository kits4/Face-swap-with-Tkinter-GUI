import os
from tkinter import *
from VideoSwap import VideoSwap 
from BrowseFiles import BrowseFiles 
from SwapFace import SwapFace
import config 

def Image():
    c2.deselect()
def Video():
    c1.deselect()

def Submit(store):
    if(var2.get()):
        store[0] = VideoSwap(None)
        store[1] = "video"
    else:
        store[0] = BrowseFiles(None)
        store[1] = "image"
    root2.destroy()
    root2.quit()
        
    
def OneWaySwapProcess(title, store):
    global root2
    root2 = Toplevel()
    global var1
    global var2, c1, c2
    var1 = IntVar()
    var2 = IntVar()
    root2.geometry("400x400")
    root2.wm_iconbitmap("./Images/icon.ico")
    root2.focus_force()
    root2.title(title)
    c1 = Checkbutton(root2, text='Image',variable=var1, height = 3, width = 10, onvalue=1, offvalue=0, command=Image)
    c1.pack()
    c2 = Checkbutton(root2, text='Video',variable=var2, height = 3, width = 10, onvalue=1, offvalue=0, command=Video)
    c2.pack()
    view = Button(root2, text="View", fg="white", bg="blue", width=10, height=2, relief='ridge',borderwidth=7, command = lambda: Submit(store))
    view.place(x = 200, y = 200)
    c1.place(x = 200, y = 100)
    c2.place(x = 200, y = 160)
    root2.mainloop()

def OneWaySwap(event):
    OneWaySwapProcess("First Input", config.oneWaySwapInput1)
    OneWaySwapProcess("Second Input", config.oneWaySwapInput2)
    SwapFace(None, config.oneWaySwapInput1[0], config.oneWaySwapInput2[0])
    if(config.oneWaySwapInput1[1] == "video"):
        print("121212")
        try: 
            os.remove(config.oneWaySwapInput1[0])
        except: pass
    if(config.oneWaySwapInput2[1] == "video"):
        try: 
            os.remove(config.oneWaySwapInput2[0])
        except: pass
