
from tkinter import *
from tkinter.ttk import Notebook
from PIL import ImageTk, Image



class MenuBar(Menu):
    def __init__(self,root):
        Menu.__init__(self, root)
        file = Menu(self, tearoff=False)
        file.add_command(label="New")  
        self.add_cascade(label="File",underline=0, menu=file)
        
class DrawCanvas(Canvas):
    def __init__(self,root):
        Canvas.__init__(self,root)
        can = Canvas(root,width=1000,height=700,bg='white',border=1,highlightbackground='#e8e7ec')
        can.grid(row=1,column=0,sticky='nsew')

class ToolBoxTab(Notebook):
    def __init__(self,root):
        Notebook.__init__(self,root)
        tab = Notebook(root,width=1000,height=85)
        tab.grid(row=0,column=0,sticky='ew')
        tab_frame1 = Frame(tab,width=1000,height=100,bg='#f0f0f0')
        tab_frame1.pack(fill='both',expand=1)
        tab.add(tab_frame1,text='Grey Tab')

        tab_button1 = Button(tab_frame1,width=10,height=5,text='3')
        tab_button1.grid(row=0,column=0,rowspan=1)
        btn_image = PhotoImage(file='./download.png')
        tab_button2 = Button(root,image=btn_image)
        tab_button2.grid(row=0,column=1)

class main_page(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)
        DrawCanvas(self)
        ToolBoxTab(self)


if __name__ == "__main__":
    root=main_page()
    root.title('Link Budget Caluclator')
    root.iconbitmap('./gui_icon.ico')
    root.geometry('1500x900')
    root.minsize(300,0)
    root.configure(bg='#e8e7ec')

    # Grid.rowconfigure(root,1,weight=1)
    Grid.columnconfigure(root,0,weight=1)

    root.mainloop()