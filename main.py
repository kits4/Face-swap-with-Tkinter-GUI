from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from BrowseFiles import browseFile
from SwapFace import SwapFace

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen_resolution = "{}x{}+{}+{}".format(width, height, 0, 0)
root.title("Face Swap")
root.geometry(screen_resolution)
root.wm_iconbitmap("./Images/icon.ico")

load = Image.open("./Images/final.png")
load = load.resize((width, height), Image.LANCZOS)
render = ImageTk.PhotoImage(load)

# labels can be text or images
img = Label(root, image=render)
img.image = render
img.place(x=0, y=0)

# #new = Button(root, text="SNAPSHOT", activebackground="green", fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
# #new.bind("<Button-1>",nw)
# #new.place(x=670, y=400)

# app=Button(root,text="AVATARS",fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
# app.bind("<Button-1>",charselect)
# app.place(x=670,y=340)

view = Button(root, text="View", fg="white", bg="blue", width=15, height=3, relief='ridge',borderwidth=7)
view.place(x=400, y=300)
view.bind("<Button-1>",browseFile)

refSwap = Button(root, text="Reference Swap", fg="white", bg="blue", width=15, height=3, relief='ridge', borderwidth=3)
refSwap.place(x=670, y=470)
refSwap.bind("<Button-1>", SwapFace)

root.mainloop()