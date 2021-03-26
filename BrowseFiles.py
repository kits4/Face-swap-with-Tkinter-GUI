from tkinter.filedialog import askopenfilename

def BrowseFiles(event):

    filename = askopenfilename(filetypes=(("Jpeg images","*.jpeg"),("PNG images","*.png"),("All Files","*.*")))
    print(filename)
    return filename
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