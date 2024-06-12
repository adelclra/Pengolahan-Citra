from tkinter import *
from PIL import Image, ImageEnhance, ImageFilter, ImageTk
from tkinter import filedialog
import os



# Kode utama aplikasi
class ImageEditor:
    def __init__(self, panel):
        self.panel = panel
        self.img = Image.open("logo.png").resize((600, 700))
        self.outputImage = self.img

    def display_image(self):
        dispimage = ImageTk.PhotoImage(self.outputImage)
        self.panel.configure(image=dispimage)
        self.panel.image = dispimage

    def brightness_callback(self, brightness_pos):
        brightness_pos = float(brightness_pos)
        enhancer = ImageEnhance.Brightness(self.img)
        self.outputImage = enhancer.enhance(brightness_pos)
        self.display_image()

    def contrast_callback(self, contrast_pos):
        contrast_pos = float(contrast_pos)
        enhancer = ImageEnhance.Contrast(self.img)
        self.outputImage = enhancer.enhance(contrast_pos)
        self.display_image()

    def sharpen_callback(self, sharpness_pos):
        sharpness_pos = float(sharpness_pos)
        enhancer = ImageEnhance.Sharpness(self.img)
        self.outputImage = enhancer.enhance(sharpness_pos)
        self.display_image()

    def color_callback(self, color_pos):
        color_pos = float(color_pos)
        enhancer = ImageEnhance.Color(self.img)
        self.outputImage = enhancer.enhance(color_pos)
        self.display_image()

    def rotate_left(self):
        self.img = self.img.rotate(-90)
        self.outputImage = self.img
        self.display_image()

    def rotate_right(self):
        self.img = self.img.rotate(90)
        self.outputImage = self.img
        self.display_image()

    def rotate_90deg(self):
        self.img = self.img.rotate(90)
        self.outputImage = self.img
        self.display_image()

    def rotate_180deg(self):
        self.img = self.img.rotate(180)
        self.outputImage = self.img
        self.display_image()

    def flip(self):
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.outputImage = self.img
        self.display_image()

    def resize(self):
        self.img = self.img.resize((500, 350))
        self.outputImage = self.img
        self.display_image()

    def crop(self):
        self.img = self.img.crop((200, 200, 300, 300))
        self.outputImage = self.img
        self.display_image()

    def reset(self):
        self.img = Image.open("logo.png").resize((600, 700))
        self.outputImage = self.img
        self.display_image()

    def change_image(self):
        imgname = filedialog.askopenfilename(title="Change Image")
        if imgname:
            self.img = Image.open(imgname).resize((600, 600))
            self.outputImage = self.img
            self.display_image()

    def save(self):
        savefile = filedialog.asksaveasfile(defaultextension=".jpg")
        if savefile:
            self.outputImage.save(savefile)
    
    def close(self, mains):
        mains.destroy()
