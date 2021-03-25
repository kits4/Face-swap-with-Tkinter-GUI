import os
import cv2
import time
from pathlib import Path
from SwapFace import SwapFace

def VideoSwap(event):
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    while 1:
       ret, frame = cap.read()
       cv2.imshow('img', frame)
       k = cv2.waitKey(10) & 0xff
       if k == 27:
           break
       end_time = time.time()
       elapsed = end_time - start_time
       if int(elapsed) > 10:
           cv2.destroyWindow("img")
           timestr = time.strftime("%Y%m%d_%H%M%S")
           downloads_path = str(Path.home() / "Downloads")
           img_path = downloads_path + "\\video_input_" + timestr + ".jpeg"
           cv2.imwrite(img_path, frame)
           SwapFace(None, img_path)
           break
    print("hiiiii")
    try: 
        os.remove(img_path)
    except: pass
    cap.release()