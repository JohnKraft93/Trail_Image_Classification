import tkinter as tk
from PIL import ImageTk, Image
import os

def reName(user):
    if directorySet:
        timeDate = Image.open(images[currentImg]).getexif()[36867].replace(":","-").replace(" ","--")
        
        if dog.get():
            photoName = user+"_"+number.get()+"_dogs"+dogSpinner.get()+"_"+timeDate+".JPG"
        else:
            photoName = user+"_"+number.get()+"_noDogs_"+timeDate+".JPG"
        
        print("renaming photo to:")
        print(photoName)
        
        os.rename(images[currentImg], currentDirectory + "/" + photoName)
        images[currentImg] = currentDirectory + "/" + photoName
        
        resetStuff()
        nextPhoto()
    
def setNum(val):
    number.delete(0,'end')      
    number.insert(0,val)     
    
def resetStuff():
    global dogCount
    setNum(1)
    dogSpinner.delete(0,'end')
    dogSpinner.insert(0,0)
    dog.set(0)
    dogCount = 0

def setPicture():
    global image, img, imgLabel
    
    image = Image.open(images[0])
    image = image.resize((imgHeight, imgWidth), Image.ANTIALIAS)
        
    img = ImageTk.PhotoImage(image)
    
    imgLabel = tk.Label(image=img, master=frame_1)
    imgLabel.pack()    
    
def destroyPic():
    global imgLabel
    imgLabel.destroy()

def nextPhoto():
    global currentImg
    global imgLabel
    if currentImg < len(images)-1:
        currentImg += 1
        print(images[currentImg])
        image = Image.open(images[currentImg])
        image = image.resize((imgHeight, imgWidth), Image.ANTIALIAS)
            
        img = ImageTk.PhotoImage(image)

        imgLabel.destroy()

        imgLabel = tk.Label(image=img, master=frame_1)
        imgLabel.image = img
        imgLabel.pack()
        resetStuff()
    
def prevPhoto():
    global currentImg
    global imgLabel
    if currentImg > 0:
        currentImg -= 1
        print(images[currentImg])
        image = Image.open(images[currentImg])
        image = image.resize((imgHeight, imgWidth), Image.ANTIALIAS)
            
        img = ImageTk.PhotoImage(image)
        
        imgLabel.destroy()
            
        imgLabel = tk.Label(image=img, master=frame_1)
        imgLabel.image = img
        imgLabel.pack()
        resetStuff()
    
def setDirectory():
    global currentDirectory
    global images, directorySet
    currentDirectory = directory.get("1.0", 'end-1c')
    try:
        images = os.listdir(currentDirectory)
        
        for i, image in enumerate(images):
            images[i] = currentDirectory + '/' + image
        
        if directorySet:
            destroyPic()
    except:
        images = []
        if directorySet:
            destroyPic()
    
    resetStuff()
    if len(images) > 0:
        directorySet = True
        setPicture()
    
currentImg = 0
currentDirectory = ""
directorySet = False
images = []
imgWidth = 1000
imgHeight = 500

root = tk.Tk()
title = tk.Label(text="label picture", width=120)
title.pack()

root.bind("1", lambda event: setNum(1))
root.bind("2", lambda event: setNum(2))
root.bind("3", lambda event: setNum(3))
root.bind("4", lambda event: setNum(4))
root.bind("5", lambda event: setNum(5))
root.bind("6", lambda event: setNum(6))
root.bind("7", lambda event: setNum(7))
root.bind("8", lambda event: setNum(8))
root.bind("9", lambda event: setNum(9))
root.bind("0", lambda event: setNum(0))
root.bind("d", lambda event: toggleDog())
root.bind("f", lambda event: plusDog())

def toggleDog():
    if dog.get():
        dog.set(0)
    else:
        dog.set(1)
    
dogCount = 0
def plusDog():
    global dogCount
    dogSpinner.delete(0,'end')
    dogCount+=1
    dogSpinner.insert(0,dogCount)

frame_1 = tk.Frame()
frame_2 = tk.Frame()
frame_3 = tk.Frame()
directoryFrame = tk.Frame()

directory = tk.Text(
    master=directoryFrame,
    height=1,
    width=69    
)
directory.pack(side=tk.LEFT)

search = tk.Button(
    master=directoryFrame,
    height=1,
    width=51,
    text = "visit",
    bg = "black",
    fg = "white",
    command = setDirectory
)
search.pack()

#buttons

mechanical = tk.Button(
    master=frame_2,
    text="mechanical",
    height=7,
    width=20,
    bg = "green",
    fg = "black",
    command= lambda: reName("mechanical")
)
mechanical.pack(side=tk.LEFT)

motorized = tk.Button(
    master=frame_2,
    text="motorized",
    height=7,
    width=20,
    bg = "green",
    fg = "black",
    command = lambda: reName("motorized")
)
motorized.pack(side=tk.LEFT)

nonMotorized = tk.Button(
    master=frame_2,
    text="nonMotorized",
    height=7,
    width=20,
    bg = "green",
    fg = "black",
    command= lambda: reName("nonmoterized")
)
nonMotorized.pack(side=tk.LEFT)

junk = tk.Button(
    master=frame_2,
    text="nobody",
    height=7,
    width=20,
    bg = "green",
    fg = "black",
    command= lambda: reName("nobody")
)
junk.pack(side=tk.LEFT)

number = tk.Spinbox(master=frame_2, from_=1, to=10, width=10)
number.pack(side=tk.LEFT)

dog = tk.IntVar()
dogs = tk.Checkbutton(
    master=frame_2,
    text="dog",
    variable=dog,
    width=20
)
dogs.pack(side=tk.LEFT)

dogSpinner = tk.Spinbox(master=frame_2, from_=0, to=10, width=10)
dogSpinner.pack(side=tk.LEFT)

prev = tk.Button(
    master=frame_3,
    text="<-----prev",
    height=4,
    width=60,
    bg = "white",
    fg = "black",
    command= prevPhoto
)
prev.pack(side=tk.LEFT)

next_ = tk.Button(
    master=frame_3,
    text="next----->",
    height=4,
    width=60,
    bg = "white",
    fg = "black",
    command= nextPhoto
)
next_.pack(side=tk.LEFT)

directoryFrame.pack()
frame_1.pack()
frame_2.pack()
frame_3.pack()

root.mainloop()