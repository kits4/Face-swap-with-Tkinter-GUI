from tkinter.filedialog import askopenfilename

def browseFile(event):

    filename = askopenfilename(filetypes=(("Jpeg images","*.jpg"),("PNG images","*.png"),("All Files","*.*")))
    print(filename)
    # root1=Toplevel()
    # root1.wm_iconbitmap("icon.ico")
    # lo = Image.open(filename)
    # ren = ImageTk.PhotoImage(lo)
    # width=ren.width()
    # height=ren.height()
    # resolution=str(width)+'x'+str(height)
    # root1.geometry(resolution)
    # img12 = Label(root1, image=ren)
    # img12.image = ren
    # img12.place(x=0, y=0)
    # root1.mainloop()