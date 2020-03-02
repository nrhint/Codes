##Nathan Hinton
#The text editing is based on a program called erinxPad found on github.com

print("This is ment for python 3. Due to changes in the tkinter package this will not work for python 2.")

#from tkinter import Tk, Menu, Text, Scrollbar
from tkinter import *

#Setup global vars needed...
root = Tk()
root.title('Text Editor')
menu = Menu(root)

text = Text(root, height=30, width=60, font = ("Arial", 10))
scroll = Scrollbar(root, command=text.yview)
scroll.config(command=text.yview)                  
text.config(yscrollcommand=scroll.set)           
scroll.pack(side=RIGHT, fill=Y)
text.pack()
root.resizable(0,0)

class textEditor:
    def __init__(self, filename = False, configFile = False, title = 'Text Editor'):
        if filename != False:
            try:
                self.file = open(filename)
            except FileNotFoundError:
                print('File to open not found. Making new file.')
                self.file = open(filename, 'w').close()
                self.file = open(filename)
        #Begin loading the configuration:
        root.title(title)
        if configFile != False:
            try:
                import configFile
            except ModuleNotFoundError:
                import defaultConfig
                print('Configuration file not found. Defaulting to the minimal interface')
        root.mainloop()
