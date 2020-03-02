#Nathan Hinton
#The '#' at the begining of the line is a comment
#This is the default file

#This is an example menu for opening a file:

print('default cofig loading...')
print('for use from program not from the editor.')

filemenu = Menu(root)
root.config(menu = menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=opn)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=kill)

def opn(filepath):
    file = open(filepath, 'r')
    if file != '':
        txt = file.read()
        text.insert(INSERT, txt)
