

'''
MIT License

Copyright (c) 2022 Vertinski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''






import io
import pyautogui
from PIL import ImageGrab, Image, ImageFont, ImageDraw
import time
from fastapi import FastAPI
import base64






data = ''
iteration = 0
length = 0

print("Screengrab is active!")

def screengrab():
    global data, iteration, length
    
    myscreen = ImageGrab.grab(xdisplay="")
            
    width, height = myscreen.size
    newsize = (int(width / 2), int(height / 2))
    myscreen = myscreen.resize(newsize)

    x, y = pyautogui.position()

    draw = ImageDraw.Draw(myscreen)

    font = ImageFont.truetype(r'arialbd.ttf', 30)

    text = '↑'   #symbol for mouse cursor

    draw.text((int(x/2)-6, int(y/2)-9), text, font = font, fill="#000000")
    draw.text((int(x/2)-7, int(y/2)-10), text, font = font, fill="#CDCDCD")


    buf = io.BytesIO()
    myscreen.save(buf, format='JPEG') #save image data to a temporary buffer
    byte_im = buf.getvalue()


    data = base64.b64encode(byte_im)   #encode image data as base64
    length = (len(data) / 1024)   #data size in Kb(🤔🤔🤔)

    iteration += 1   #each iteration uses some of the key
    time.sleep(0.05)


app = FastAPI()

@app.get("/")
async def root():
    screengrab()
    return {"content": data,
            "size": length,
            "iteration": iteration}


### TODO: add + customize the API endpoints









