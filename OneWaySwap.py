import os
from tkinter import *
from PIL import Image, ImageTk
import time
from VideoSwap import VideoSwap 
from BrowseFiles import BrowseFiles 
from SwapFace import SwapFace
import config 

x, y = 0, 0
def mouse_press(event, root):
    global x, y
    count = time.time()
    x, y = event.x, event.y

def mouse_motion(event, root):
    global x, y
    offset_x, offset_y = event.x - x, event.y - y  
    new_x = root.winfo_x() + offset_x
    new_y = root.winfo_y() + offset_y
    new_geometry = f"+{new_x}+{new_y}"
    root.geometry(new_geometry)

def Image1():
    var2.set(0)
def Video():
    var1.set(0)

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
    root2.overrideredirect(1)
    global var1
    global var2, c1, c2
    var1 = IntVar()
    var2 = IntVar()
    root2.wm_iconbitmap("./Images/icon.ico")
    root2.focus_set()
    root2.title(title)
    # root2.attributes("-alpha", 0.5)
    root2.wm_attributes("-transparentcolor", "#FFEBE0")
    load = Image.open("./Images/input_bg.png")
    load.thumbnail((400, 400), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)

    resolution=str(load.width)+'x'+str(load.height) + '+' + str(250) + '+'+ str(250)
    root2.geometry(resolution)

    img = Label(root2, image=render)
    img.image = render
    img.place(x=0, y=0)
    img.pack()

    c1 = ttk.Checkbutton(root2, text='Image', variable=var1, onvalue=1, offvalue=0, command=Image1)
    c1.pack()
    c2 = ttk.Checkbutton(root2, text='Video ', variable=var2, onvalue=1, offvalue=0, command=Video)
    c2.pack()
    view = ttk.Button(root2, text="Submit", command = lambda: Submit(store), style = "submit.TButton")
    view.place(relx=0.5, rely=0.67, anchor=CENTER)
    # view.pack()
    c1.place(relx=0.5, rely=0.4, anchor=CENTER)
    c2.place(relx=0.5, rely=0.52, anchor=CENTER)

    root2.bind("<B1-Motion>", lambda eff:mouse_motion(eff, root2))
    root2.bind("<Button-1>", lambda eff:mouse_press(eff, root2))
    root2.mainloop()

def OneWaySwap(event, select):
    OneWaySwapProcess("First Input", config.oneWaySwapInput1)
    OneWaySwapProcess("Second Input", config.oneWaySwapInput2)
    if select == 1:
        SwapFace(None, config.oneWaySwapInput1[0], config.oneWaySwapInput2[0], 1)
    else:
        ip1 = Image.open(config.oneWaySwapInput1[0])
        ip1.thumbnail((640, 480), Image.ANTIALIAS)

        ip2 = Image.open(config.oneWaySwapInput2[0])
        ip2.thumbnail((640, 480), Image.ANTIALIAS)

        images = [ ip1, ip2]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset += im.size[0]
        new_im.save('test.jpg')
        SwapFace(None, 'test.jpg', config.oneWaySwapInput2[0], 2)

    if(config.oneWaySwapInput1[1] == "video"):
        try: 
            os.remove(config.oneWaySwapInput1[0])
        except: pass
    if(config.oneWaySwapInput2[1] == "video"):
        try: 
            os.remove(config.oneWaySwapInput2[0])
        except: pass
    try:
        os.remove("test.jpg")
    except: pass