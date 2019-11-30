from tkinter import *

class Main:
    def __init__(self,master):
        
        def sv():
            filenm = open("more.py","w")
            filenm.write(self.editor.get("1.0",END))
            filenm.close()
            
        def opn():
            fi= open("more.py","r")
            self.editor.delete("1.0",END)
            self.editor.insert(1,fi.read())
            fi.close()
        
        self.master = master
        master.title("more ide")
        
        self.w = Label(master,text= "more ide v0.0.1")
        self.w.pack()
        
        self.editor = Text(master,width="200",height="200")
        self.editor.pack()
        
        self.mb = Menu(master)
        self.mb.add_command(label="Save!", command=sv)
        self.mb.add_command(label="open!", command=opn)
        root.config(menu=self.mb)
        
root = Tk()
gui = Main(root)
root.mainloop()
