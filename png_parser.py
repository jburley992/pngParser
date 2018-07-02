from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkcolorpicker import askcolor
import tkinter as tk




def removePixels(filename, colorToRemove, newName):
    img = Image.open(filename)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == colorToRemove[0] and item[1] == colorToRemove[1] and item[2] == colorToRemove[2]:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(newName, "PNG")
    return img

class Window(object):
    def openFile(self):
        self.filename = fd.askopenfilename(parent=self.root)
        self.currentImage = ImageTk.PhotoImage(Image.open(self.filename))
        panel = tk.Label(self.root, image=self.currentImage)
        panel.pack()

    def getColor(self):
        #Gets standard RBG Colors
        colorToRemove = askcolor((255,255,0),self.root)[0]
        self.currentImage = removePixels(self.filename,colorToRemove,"null.png")

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Image Editor")
        self.root.geometry("400x400")

        self.menu = tk.Menu(self.root)
        self.menu.add_command(label="Load Image",command=self.openFile)
        self.menu.add_command(label="Remove Color",command=self.getColor)
        self.root.config(menu=self.menu)
        self.filename = 0
        self.currentImage = 0


def main():
    window = Window()
    window.root.mainloop()

main()
