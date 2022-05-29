from tkinter import *
import visual as v
from PIL import Image, ImageTk
from tkinter import filedialog
import os

class Canva:
    def __init__(self, master):
        self.master = master

        self.frame = Frame(self.master)
        self.frame.pack()
        self.frame2 = Frame(self.master)
        self.frame2.pack()
        self.frame2.config(relief=RIDGE)
        self.frame_cancel = Frame(self.master)
        self.frame_cancel.pack()
        self.side_frame = Frame(self.frame2)
        self.side_frame.pack()
        self.side_frame.config(relief=GROOVE)

        self.c = Canvas(self.frame2, bg="violet", width=900, height=900)
        self.c.pack(side="right")

        self.main_lbl = Label(self.frame, text="Welcome to the Retrica!", font=v.FONT)
        self.main_lbl.grid(row=0, column=1, columnspan=1)

        self.btn1 = Button(self.frame2, text="Open file(only jpg, jpeg or png)", font=v.FONT2, bg=v.bg_1, command=self.upload)
        self.btn1.pack(side="top")
        self.btn_size = Button(self.frame2, text="Resize image to InstaSize", font=v.FONT2, bg=v.bg_1, command=self.size)
        self.btn_size.pack(side="bottom")
        self.btn_filter = Button(self.frame2, text="Apply fancy filter", font=v.FONT2, bg=v.bg_1, command=self.filter)
        self.btn_filter.pack(side="bottom")
        self.btn_rotate = Button(self.frame2, text="Rotate image", font=v.FONT2, bg=v.bg_1, command=self.rotate)
        self.btn_rotate.pack(side="bottom")
        self.btn_save = Button(self.frame2, text="Save image as", font=v.FONT2, bg=v.bg_1, command=self.save)
        self.btn_save.pack(side="bottom")
        self.btn_cancel = Button(self.frame_cancel, text="Cancel changes", font=v.FONT2, bg=v.bg_1, command=self.cancel)
        self.btn_cancel.pack(side="bottom")

    def upload(self):
        global path, img
        path = filedialog.askopenfilename(initialdir=os.getcwd())
        img = Image.open(path)
        img.thumbnail((1080, 1080))
        img1 = ImageTk.PhotoImage(img)
        self.c.create_image(500, 500, image=img1)
        self.c.image=img1

    def size(self):
        pass

    def filter(self):
        self.refresh_frame()
        self.btn_bw = Button(self.side_frame, text="Black and White", command=self.bw).pack(side="right")
        self.btn_sketch = Button(self.side_frame, text="Sketch", command=self.sketch).pack(side="right")
        self.btn_effect = Button(self.side_frame, text="Another filter", command=self.filter1).pack(side="right")

    def bw(self):
        pass

    def sketch(self):
        pass

    def filter1(self):
        pass

    def rotate(self):
        global path, img_rotated, img_rotated1
        img = Image.open(path)
        img.thumbnail((1080, 1080))
        img_rotated = img.transpose(Image.ROTATE_90)
        img_rotated1 = ImageTk.PhotoImage(img_rotated)
        self.c.create_image(500, 500, image=img_rotated1)
        self.c.image=img_rotated1

    def save(self):
        pass

    def cancel(self):
        pass



root = Tk()
Canva(root)
root.mainloop()
