from PIL import Image
import cv2
import pytesseract
from textblob import TextBlob
import os
import shutil

dest="/home/aniket/Desktop/Projects/gif_extract/gif_data/"
op_dest="/home/aniket/Desktop/Projects/gif_extract/filtered_data/"

for i in range(107):
    ip=dest+str(i)+".webp"
    op=dest+"tmp.gif"
    
    # Open a WebP file
    img = Image.open(ip)

    # Save as a GIF file
    img.save(op, 'GIF', save_all=True, duration=1, loop=0)
    
    img.seek(0)
    img.save("tmp.png")
    
    img_cv2=cv2.imread("tmp.png")
    
    try:
        crop_img = img_cv2[0:170,200:470]
        txt = pytesseract.image_to_string(crop_img)
    except:
        txt=""
    
    word=txt.replace("\n", "")
    word=word.replace(" ", "")
    word = ''.join(filter(str.isalnum, word))
    word=word.lower()
    
    b = TextBlob(word)
    ans=str(b.correct())
    
    print("corrected text: "+ans)
    
    if(len(ans)>0):
        fname=op_dest+ans+".webp"
        shutil.copyfile(ip, fname)
    else:
        fname=op_dest+"unknown"+str(i)+".webp"
        shutil.copyfile(ip, fname)
