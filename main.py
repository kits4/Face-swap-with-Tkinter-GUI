from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Face Swap")
root.geometry('1600x1000')
root.wm_iconbitmap("icon.ico")

load = Image.open("final.png")
render = ImageTk.PhotoImage(load)

# labels can be text or images
img = Label(root, image=render)
img.image = render
img.place(x=0, y=0)


#new = Button(root, text="SNAPSHOT", activebackground="green", fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
#new.bind("<Button-1>",nw)
#new.place(x=670, y=400)

app=Button(root,text="AVATARS",fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
app.bind("<Button-1>",charselect)
app.place(x=670,y=340)

view = Button(root, text="View", fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
view.place(x=670, y=600)
view.bind("<Button-1>",browseFile)

Filters = Button(root, text="Filters", fg="white", bg="blue", width=15, height=3,relief='ridge',borderwidth=7)
Filters.place(x=670, y=470)
Filters.bind("<Button-1>",lol33)

root.mainloop()