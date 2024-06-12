from tkinter import *
from PIL import Image, ImageEnhance, ImageFilter, ImageTk
from tkinter import filedialog
import os



# Kode utama aplikasi
class ImageEditor:
    def __init__(self, panel):
        self.panel = panel
        self.original_img = Image.open(os.path.join(os.path.dirname(__file__), "logo.png"))
        self.img = self.original_img.resize((600, 700))
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

    def scaling(self, width, height):
        self.img = self.original_img.resize((width, height), Image.LANCZOS)
        self.outputImage = self.img
        self.display_image()

    def scaling_image():
        width = int(width_entry.get())
        height = int(height_entry.get())
        image_editor.resize(width, height)

    def crop(self):
        self.img = self.img.crop((200, 200, 300, 300))
        self.outputImage = self.img
        self.display_image()

    def reset(self):
        self.img = self.original_img.resize((600, 700))
        self.outputImage = self.img
        self.display_image()

    def translate(self, x_translation, y_translation):
        self.outputImage = self.img.transform(self.img.size, Image.AFFINE, (1, 0, x_translation, 0, 1, y_translation))
        self.display_image()

    def apply_translation():
        x_translation = int(x_translation_entry.get())
        y_translation = int(y_translation_entry.get())
        image_editor.translate(x_translation, y_translation)

    def change_image(self):
        imgname = filedialog.askopenfilename(title="Change Image")
        if imgname:
            self.original_img = Image.open(imgname)
            self.img = self.original_img.resize((600, 600))
            self.outputImage = self.img
            self.display_image()

    def save(self):
        savefile = filedialog.asksaveasfile(defaultextension=".jpg")
        if savefile:
            self.outputImage.save(savefile)

    def close(self, mains):
        mains.destroy()