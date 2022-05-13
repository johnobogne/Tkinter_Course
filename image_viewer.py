from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pathlib import Path

root = Tk()
root.title('Image Viewer')

'''frame = ttk.Frame(root, width=1280, height=720, padding=10)
frame.pack(fill='both', expand=True)'''

images = []
directory = 'D:\Libraries\John\Pictures\Pinterest'
pathlist = Path(directory).glob('*.*')

for path in pathlist :
    images.append(ImageTk.PhotoImage(Image.open(path)))

def previous() :
    imageDisplay.grid_forget()
    global currentImage
    currentImage-=1
    display(currentImage)

def next() :
    imageDisplay.grid_forget()
    global currentImage
    currentImage+=1
    display(currentImage)

def display(counter):
    global imageDisplay
    imageDisplay = Label(image=images[counter])
    imageDisplay.grid(row=0, column=0, columnspan=3)
    root.eval('tk::PlaceWindow . center')

currentImage = 0

backButton = Button(root, text='<', command=lambda: previous()).grid(row=1, column=0)
nextButton = Button(root, text='>', command=lambda: next()).grid(row=1, column=2)
exitButton = Button(root, text='Close', command=root.quit).grid(row=1, column=1)

display(currentImage)

root.mainloop()
