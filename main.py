from tkinter import *
import visual as v
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2

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

        self.c = Canvas(self.frame2, bg="violet")
        self.c.pack()

        self.main_lbl = Label(self.frame, text="Welcome to the Retrica!", font=v.FONT)
        self.main_lbl.grid(row=0, column=1, columnspan=1)
        # self.alatoo_logo = ImageTk.PhotoImage(file="logo.ico").subsample(2, 2)
        # self.logo= Label(self.frame2, image=self.alatoo_logo).grid(row=0, column=0, rowspan=1)

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
        self.filename = filedialog.askopenfilename()
        self.img = cv2.imread(self.filename)
        self.edited_image = cv2.imread(self.filename)
        self.filtered = cv2.imread(self.filename)
        self.display(self.edited_image)

    def refresh_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass

        self.c.unbind("<ButtonPress>")
        self.c.unbind("<B1-Motion>")
        self.c.unbind("<ButtonRelease>")
        self.display_image(self.edited_image)
        self.side_frame = Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))

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
        pass

    def save(self):
        pass

    def cancel(self):
        pass


    def display(self, image=None):
        if image is None:
            self.image = self.edited_image.copy()
        else:
            self.image=image

        self.image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        self.height, self.width, self.ch = self.image.shape()
        self.r = self.height/self.width

        self.new_w = self.width
        self.new_h = self.height

        self.new_img = ImageTk.PhotoImage(Image.fromarray(self.new_img))

        self.c.config(width=self.new_w, height=self.new_h)
        self.c.create_image(self.new_w/2, self.new_h/2, image=self.new_img)


root = Tk()
Canva(root)
root.mainloop()
