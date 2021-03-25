import cv2
import time
from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from fswap import RefFaceSwapping , TwoFaceSwapping

def SwapFace(event, input_img):
    face_swapping = RefFaceSwapping(reference_path='./Images/reference.png')
    img = face_swapping.load_img(input_img)
    img_swap = face_swapping(img)
    img_swap = cv2.cvtColor(img_swap, cv2.COLOR_BGR2RGB)
    timestr = time.strftime("%Y%m%d_%H%M%S")
    downloads_path = str(Path.home() / "OneDrive" /"Pictures" / "Face_Swap")
    img_path = downloads_path + "\\Face_Swap_" + timestr + ".jpeg"
    cv2.imwrite(img_path, img_swap)

    root1=Toplevel()
    width=800
    height=800
    root1.wm_iconbitmap("./Images/icon.ico")
    lo = Image.open(img_path)
    lo = lo.resize((width, height), Image.LANCZOS)
    ren = ImageTk.PhotoImage(lo)
    resolution=str(width)+'x'+str(height)
    root1.geometry(resolution)
    
    img12 = Label(root1, image=ren)
    img12.image = ren
    img12.place(x=0, y=0)
    
