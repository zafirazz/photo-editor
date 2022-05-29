from tkinter import *
import visual as v
from PIL import Image, ImageTk
from PIL.ImageFilter import CONTOUR, SMOOTH, BLUR
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

        self.c = Canvas(self.frame2, bg="violet", width=900, height=900)
        self.c.pack(side="right")

        self.main_lbl = Label(self.frame, text="Welcome to the Retrica!", font=v.FONT)
        self.main_lbl.grid(row=0, column=1, columnspan=1)
        self.logo = ImageTk.PhotoImage(file='alatoologo.jpeg')
        self.logo_lbl = Label(self.frame, image=self.logo)
        self.logo_lbl.grid(row=0, column=0, rowspan=5)

        self.btn1 = Button(self.frame2, text="Open file(only jpg, jpeg or png)", font=v.FONT2, bg=v.bg_1, command=self.upload)
        self.btn1.pack(side="top")
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

    def filter(self):
        self.btn_bw = Button(self.frame2, text="Black and White", command=self.bw).pack(side="right")
        self.btn_sketch = Button(self.frame2, text="Sketch", command=self.sketch).pack(side="right")
        self.btn_effect = Button(self.frame2, text="Smooth", command=self.filter1).pack(side="right")
        self.btn_blur = Button(self.frame2, text="Blur", command=self.filter2).pack(side="right")

    def bw(self):
        global path, img_ed, img_ed1
        img = Image.open(path)
        img.thumbnail((1080, 1080))
        img_ed = img.convert("L")
        img_ed1 = ImageTk.PhotoImage(img_ed)
        self.c.create_image(500, 500, image=img_ed1)
        self.c.image = img_ed1

    def sketch(self):
        global path, img_sketch, img_sketch1
        img = Image.open(path)
        img.thumbnail((1080, 1080))
        img_sketch = img.filter(CONTOUR)
        img_sketch1 = ImageTk.PhotoImage(img_sketch)
        self.c.create_image(500, 500, image=img_sketch1)
        self.c.image = img_sketch1

    def filter1(self):
        global path, img_sm, img_sm1
        img = Image.open(path)
        img.thumbnail((1080, 1080))
        img_sm = img.filter(SMOOTH)
        img_sm1 = ImageTk.PhotoImage(img_sm)
        self.c.create_image(500, 500, image=img_sm1)
        self.c.image=img_sm1

    def filter2(self):
        global path, img_bl, img_bl1
        img = Image.open(path)
        img.thumbnail((1080, 1080))
        img_bl = img.filter(BLUR)
        img_bl1 = ImageTk.PhotoImage(img_bl)
        self.c.create_image(500, 500, image=img_bl1)
        self.c.image = img_bl1

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
    #     saveas = self.filename.split(".")[-1]
    #     filename =filedialog.askopenfilename()
    #     filename = filename + "." + saveas
    #
    #

    def cancel(self):
        pass



root = Tk()
root.title("Retrica de")
Canva(root)
root.mainloop()
