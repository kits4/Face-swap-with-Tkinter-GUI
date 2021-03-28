from tkinter.filedialog import askopenfilename
from tkinter import *
from PIL import Image, ImageTk
def BrowseFiles(event, check):

    filename = askopenfilename(filetypes=(("Jpeg images","*.jpeg"),("PNG images","*.png"),("All Files","*.*")))

    if(check == "view"):
        root1=Toplevel()
        root1.focus_set()
        root1.wm_iconbitmap("./Images/icon.ico")
        lo = Image.open(filename)
        lo.thumbnail((640, 480), Image.ANTIALIAS)
        ren = ImageTk.PhotoImage(lo)
        width=ren.width()
        height=ren.height()
        resolution=str(width)+'x'+str(height)
        root1.geometry(resolution)
        img12 = Label(root1, image=ren)
        img12.image = ren
        img12.place(x=0, y=0)
    else:
        return filename