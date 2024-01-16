from tkinter import Tk, Label, Button
from tkinter import ttk

class root_window:

    def _init_(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("900x500+40+40")

if __name__=="_main_":
    root=Tk()
    root_class= root_window(root)
    root.mainloop()
