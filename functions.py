from tkinter import *
from PIL import Image, ImageEnhance, ImageFilter, ImageTk
from tkinter import filedialog
import os

class ImageEditor:
    def __init__(self, canvas, crop_size_label, panel):
        self.canvas = canvas
        self.crop_size_label = crop_size_label
        self.original_img = Image.open(os.path.join(os.path.dirname(__file__), "logo.png"))
        self.img = self.original_img.resize((600, 700))
        self.outputImage = self.img
        self.panel = panel

        self.rect = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_drag(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.end_x, self.end_y)
        width = abs(self.end_x - self.start_x)
        height = abs(self.end_y - self.start_y)
        self.crop_size_label.config(text=f"Width: {width}, Height: {height}")

    def on_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.crop_image()

    def crop_image(self):
        if self.start_x and self.start_y and self.end_x and self.end_y:
            box = (self.start_x, self.start_y, self.end_x, self.end_y)
            self.img = self.img.crop(box)
            self.outputImage = self.img
            self.display_image()
            self.start_x, self.start_y, self.end_x, self.end_y = None, None, None, None
            self.canvas.delete(self.rect)
            self.rect = None
            self.crop_size_label.config(text="")

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

    def resize(self, width, height):
        self.img = self.original_img.resize((width, height), Image.LANCZOS)
        self.outputImage = self.img
        self.display_image()
    
    def scaling_image(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        self.resize(width, height)

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