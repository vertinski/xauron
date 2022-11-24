

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






import os
import subprocess
import time





p0 = subprocess.Popen(["uvicorn screengrab:app --header Access-Control-Allow-Origin:* --host 0.0.0.0 --reload"], shell=True)

print('starting web server on port 8888.....')
p2 = subprocess.Popen(["python3 -m http.server 8888"], shell=True)


time.sleep(1)

print()
input('Press Enter to stop streaming......')

p0.terminate()
p2.terminate()

print()
print('screen grab and web server stopped......')
print()








