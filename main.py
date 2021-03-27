import os
from pathlib import Path
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tkt
# from ttkthemes import ThemedStyle, ThemedTk
from PIL import Image, ImageTk
from BrowseFiles import BrowseFiles
from SwapFace import SwapFace
from VideoSwap import VideoSwap
from OneWaySwap import OneWaySwap
import config
if(not os.path.exists(str(Path.home() / "OneDrive" / "Pictures" / "Face_Swap"))):
    os.chdir(str(Path.home() / "OneDrive" /"Pictures"))
    os.mkdir("Face_Swap")
    print("ossss")

root = Tk()     
# root.set_theme("plastik")  
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', focuscolor = "red", foreground='blue', background='red', font=('Helvetica', 20))
style.map('TButton', background=[('active','yellow')], focuscolor=[('active','yellow')])
style.configure('TCheckbutton', focuscolor = "#FFD800", foreground= 'black', background='#FFD800', font=('Helvetica', 15))
style.map('TCheckbutton', background=[('active','#FFD800')], indicatoron=[('pressed', 'red'), ('selected', 'red')])
style.configure('submit.TButton', foreground='black', background='#47C7EB', font=('Helvetica', 15))
style.map('submit.TButton', background=[('active','#C8D9CD')])
# C5E1E4
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen_resolution = "{}x{}+{}+{}".format(width, height, 0, 0)
root.title("Face Swap")
root.geometry(screen_resolution)
root.wm_iconbitmap("./Images/icon.ico")

load = Image.open("./Images/final.png")
load = load.resize((width, height), Image.LANCZOS)
render = ImageTk.PhotoImage(load)
# load.save("./Images/r.png")
# labels can be text or images
img = ttk.Label(root, image=render)
img.image = render
img.place(x=0, y=0)

# #new = Button(root, text="SNAPSHOT", activebackground="green", fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
# #new.bind("<Button-1>",nw)
# #new.place(x=670, y=400)

# app=Button(root,text="AVATARS",fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
# app.bind("<Button-1>",charselect)
# app.place(x=670,y=340)
# img = PhotoImage(file = "./Images/f.png")
view = tkt.ttk.Button(root, text="View")
view.place(x=473, y=250)
view.bind("<Button-1>",BrowseFiles)


# refSwap = Button(root, text="Reference Swap", fg="white", bg="blue", width=15, height=3, relief='ridge', borderwidth=3)
# refSwap.place(x=670, y=470)
# refSwap.bind("<Button-1>", lambda eff: SwapFace(eff, input_img))

# videoSwap = Button(root, text="Video Input", fg="white", bg="blue", width=15, height=3, relief='ridge', borderwidth=3)
# videoSwap.place(x=870, y=470)
# videoSwap.bind("<Button-1>", VideoSwap)

oneWaySwap = Button(root, text="One Way Swap", fg="white", bg="blue", width=15, height=3, relief='ridge', borderwidth=3)
oneWaySwap.place(x=670, y=270)
oneWaySwap.bind("<Button-1>", lambda eff: OneWaySwap(eff, 1))

twoWaySwap = Button(root, text="Two Way Swap", fg="white", bg="blue", width=15, height=3, relief='ridge', borderwidth=3)
twoWaySwap.place(x=870, y=270)
twoWaySwap.bind("<Button-1>", lambda eff: OneWaySwap(eff, 2))

root.mainloop()