import tkinter as tk
from PIL import Image, ImageTk
import os
import visual

class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def open_frame(self):
        self.lift()

class PhotoEditor(App):
    def __init__(self, *args, **kwargs):
        App.__init__(self, *args, **kwargs)


root = tk.Tk()
root.geometry("1000x1000")
root.title("Retrica de")
root.iconbitmap("/home/marbelle/photo_editor/alatoologo.ico")
root.mainloop()