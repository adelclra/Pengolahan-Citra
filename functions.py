from tkinter import *
from PIL import Image, ImageEnhance, ImageFilter, ImageTk
from tkinter import filedialog
import os

class ImageEditor:
    def __init__(self, canvas, crop_size_label, brightness_slider, contrast_slider, color_slider, sharpness_slider):
        self.canvas = canvas
        self.crop_size_label = crop_size_label
        self.brightness_slider = brightness_slider
        self.contrast_slider = contrast_slider
        self.color_slider = color_slider
        self.sharpness_slider = sharpness_slider

        self.original_img = Image.open(os.path.join(os.path.dirname(__file__), "logo.png"))
        self.img = self.original_img.resize((600, 700))
        self.outputImage = self.img
        self.original_format = self.original_img.format

        self.current_brightness = 1.0
        self.current_contrast = 1.0
        self.current_color = 1.0
        self.current_sharpness = 1.0

        self.rect = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.init_canvas_events()

    def init_canvas_events(self):
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def apply_adjustments(self):
        # Start with the original image
        self.outputImage = self.original_img.resize((600, 700))

        # Apply brightness
        enhancer = ImageEnhance.Brightness(self.outputImage)
        self.outputImage = enhancer.enhance(self.current_brightness)

        # Apply contrast
        enhancer = ImageEnhance.Contrast(self.outputImage)
        self.outputImage = enhancer.enhance(self.current_contrast)

        # Apply color
        enhancer = ImageEnhance.Color(self.outputImage)
        self.outputImage = enhancer.enhance(self.current_color)

        # Apply sharpness
        enhancer = ImageEnhance.Sharpness(self.outputImage)
        self.outputImage = enhancer.enhance(self.current_sharpness)

        self.display_image()

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
            self.outputImage = self.outputImage.crop(box)
            self.display_image()
            self.start_x, self.start_y, self.end_x, self.end_y = None, None, None, None
            self.canvas.delete(self.rect)
            self.rect = None
            self.crop_size_label.config(text="")

    def display_image(self):
        dispimage = ImageTk.PhotoImage(self.outputImage)
        self.canvas.create_image(0, 0, image=dispimage, anchor=NW)
        self.canvas.image = dispimage

    def brightness_callback(self, brightness_pos):
        self.current_brightness = float(brightness_pos)
        self.apply_adjustments()

    def contrast_callback(self, contrast_pos):
        self.current_contrast = float(contrast_pos)
        self.apply_adjustments()

    def sharpen_callback(self, sharpness_pos):
        self.current_sharpness = float(sharpness_pos)
        self.apply_adjustments()

    def color_callback(self, color_pos):
        self.current_color = float(color_pos)
        self.apply_adjustments()

    def rotate_left(self):
        self.outputImage = self.outputImage.rotate(90, expand=True)
        self.display_image()

    def rotate_right(self):
        self.outputImage = self.outputImage.rotate(-90, expand=True)
        self.display_image()

    def rotate_90deg(self):
        self.outputImage = self.outputImage.rotate(90, expand=True)
        self.display_image()

    def rotate_180deg(self):
        self.outputImage = self.outputImage.rotate(180, expand=True)
        self.display_image()

    def flip(self):
        self.outputImage = self.outputImage.transpose(Image.FLIP_LEFT_RIGHT)
        self.display_image()

    def scaling(self, width, height):
        self.outputImage = self.outputImage.resize((width, height), Image.LANCZOS)
        self.display_image()

    def scaling_image(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        self.scaling(width, height)

    def reset(self):
        self.current_brightness = 1.0
        self.current_contrast = 1.0
        self.current_color = 1.0
        self.current_sharpness = 1.0

        self.brightness_slider.set(1.0)
        self.contrast_slider.set(1.0)
        self.color_slider.set(1.0)
        self.sharpness_slider.set(1.0)

        self.apply_adjustments()

    def translate(self, x_translation, y_translation):
        self.outputImage = self.outputImage.transform(self.outputImage.size, Image.AFFINE, (1, 0, x_translation, 0, 1, y_translation))
        self.display_image()

    def apply_translation(self):
        try:
            x_translation = int(self.x_translation_entry.get())
            y_translation = int(self.y_translation_entry.get())
            self.translate(x_translation, y_translation)
        except ValueError:
            print("Invalid translation values")

    def change_image(self):
        imgname = filedialog.askopenfilename(title="Change Image")
        if imgname:
            self.original_img = Image.open(imgname)
            self.original_format = self.original_img.format
            self.reset()
            self.display_image()

    def save(self):
        filetypes = [
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg;*.jpeg"),
            ("BMP files", "*.bmp"),
            ("GIF files", "*.gif"),
            ("All files", "*.*")
        ]
        savefile = filedialog.asksaveasfilename(defaultextension=f".{self.original_format.lower()}", filetypes=filetypes)
        if savefile:
            self.outputImage.save(savefile, format=self.original_format)

    def close(self, mains):
        mains.destroy()