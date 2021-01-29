import cv2
from tkinter import *
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from fswap import RefFaceSwapping , TwoFaceSwapping

def SwapFace(event):
    face_swapping = RefFaceSwapping(reference_path='./Images/reference.png')
    img = face_swapping.load_img('./Images/img.png')
    print(face_swapping)
    img_swap = face_swapping(img)
    cv2.imwrite("output.png", img_swap)

    root1=Toplevel()
    width=800
    height=800
    root1.wm_iconbitmap("./Images/icon.ico")
    lo = Image.open("output.png")
    lo = lo.resize((width, height), Image.LANCZOS)
    ren = ImageTk.PhotoImage(lo)
    resolution=str(width)+'x'+str(height)
    root1.geometry(resolution)
    
    img12 = Label(root1, image=ren)
    img12.image = ren
    img12.place(x=0, y=0)
    root1.mainloop()
