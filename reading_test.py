import os
with open("storage/Notepad/weather.txt","r") as f:
    print (f.read())

files = os.listdir("storage/Notepad")
for i in files:
    print (i)