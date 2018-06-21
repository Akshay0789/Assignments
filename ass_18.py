#1
def commando(x, y):
    fL.update({x:int(y)})
from tkinter import *
fL = {}
def commando(x, y):
    fL.update({x:int(y)})
    print(fL)
root = Tk()
root.title("Spam Words")
x = StringVar()
y = StringVar()
label_1 = Label(root, text="enter your name ", bg="#333333", fg="white")
label_2 = Label(root, text="enter your number, 1-10:", bg="#333333", fg="white")
entry_1 = Entry(root, textvariable=x)
entry_2 = Entry(root, textvariable=y)
label_1.grid(row=1)
label_2.grid(row=3)
entry_1.grid(row=2, column=0)
entry_2.grid(row=4, column=0)
but = Button(root, text="Execute", bg="#333333", fg="white", command=lambda :commando(x.get(), y.get()))
but.grid(row=5, column=0)
root.mainloop()

#2
from Tkinter import *
class Application(Frame):
    def main(self):
        self.filename = askopenfilename(filetypes=[("Jpeg","*.jpg")])
    def createWidgets(self):
        self.button = Button(root,text="Open",command=self.main)
        self.button.pack()
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = None
        self.pack()
        self.createWidgets()
root = Tk()
root.title("Image Manipulation Program")
app = Application(master=root)
app.mainloop()