from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
# create instance of tkinter
root = Tk()
# generate header title
root.title("TMC")
# Size of the window
# root.geometry("600x400")
root.minsize(300,300)
root.maxsize(600,400)

# define all customization
w = Label(root, text='GeeksForGeeks.org!')
# w.pack()
button = Button( root,text='Apply', width=25, bg='green' )
# button.pack()
# upload file
b1 = Button(root, text='Upload File',
   width=20,command = lambda:upload_file())
# 

b1.grid(row=1,column=1)

button.pack(side='bottom')

# functions
def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg'),('PNG Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =Button(root,image=img,padx='20', pady='20') # using Button
    b2.grid(row=1,column=1)


# executes  application
root.mainloop()
