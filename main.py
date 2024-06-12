from tkinter import *
import tkinter
from functions import ImageEditor
from tkinter import ttk
import subprocess

def open_whiteboard():
    subprocess.Popen(["python", "whiteboard.py"])

# Creating the window for image editor
mains = Tk()
space = " " * 215
screen_width = mains.winfo_screenwidth()
screen_height = mains.winfo_screenheight()
mains.geometry(f"{screen_width}x{screen_height}")
mains.title(f"{space}Image Editor")
mains.configure(bg='#102C57')

panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)

image_editor = ImageEditor(panel)
image_editor.display_image()

brightnessSlider = Scale(mains, label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=200,
                        resolution=0.1, command=image_editor.brightness_callback, bg="#344C64")
brightnessSlider.set(1)
brightnessSlider.configure(font=('poppins',11,'bold'),foreground='#ffffff')
brightnessSlider.place(x=1070, y=150)

contrastSlider = Scale(mains, label="Contrast", from_=0, to=2, orient=HORIZONTAL, length=200,
                    command=image_editor.contrast_callback, resolution=0.1, bg="#344C64")
contrastSlider.set(1)
contrastSlider.configure(font=('poppins',11,'bold'),foreground='#ffffff')
contrastSlider.place(x=1300, y=150)

sharpnessSlider = Scale(mains, label="Sharpness", from_=0, to=2, orient=HORIZONTAL, length=200,
                        command=image_editor.sharpen_callback, resolution=0.1, bg="#344C64")
sharpnessSlider.set(1)
sharpnessSlider.configure(font=('poppins',11,'bold'),foreground='#ffffff')
sharpnessSlider.place(x=1300, y=240)

colorSlider = Scale(mains, label="Colors", from_=0, to=2, orient=HORIZONTAL, length=200,
                    command=image_editor.color_callback, resolution=0.1, bg="#344C64")
colorSlider.set(1)
colorSlider.configure(font=('poppins',11,'bold'),foreground='#ffffff')
colorSlider.place(x=1070, y=240)

whiteboard_button = tkinter.Button(mains, text="Open Whiteboard", command=open_whiteboard, bg="#344C64")
whiteboard_button.configure(font=('poppins',11,'bold'),foreground='#ffffff')
whiteboard_button.place(x=860, y=490)

btnRotateLeft = Button(mains, text='Rotate Left', width=25, command=image_editor.rotate_left, bg="#344C64")
btnRotateLeft.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnRotateLeft.place(x=805, y=110)

btnRotateRight = Button(mains, text='Rotate Right', width=25, command=image_editor.rotate_right, bg="#344C64")
btnRotateRight.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnRotateRight.place(x=805, y=165)

btnRotate90deg = Button(mains, text='Rotate 90°', width=25, command=image_editor.rotate_90deg, bg="#344C64")
btnRotate90deg.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnRotate90deg.place(x=805, y=220)

btnRotate180deg = Button(mains, text='Rotate 180°', width=25, command=image_editor.rotate_180deg, bg="#344C64")
btnRotate180deg.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnRotate180deg.place(x=805, y=275)

reset_button = Button(mains, text="Reset", command=image_editor.reset, bg="#344C64", activebackground="#ffffff")
reset_button.configure(font=('poppins',10,'bold'),foreground='#ffffff')
reset_button.place(x=330, y=15)

btnChaImg = Button(mains, text='Change Image', width=25, command=image_editor.change_image, bg="#344C64", activebackground="#EBB9D4")
btnChaImg.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnChaImg.place(x=1160, y=100)

btnFlip = Button(mains, text='Mirror', width=25, command=image_editor.flip, bg="#344C64")
btnFlip.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnFlip.place(x=805, y=340)

width_label = Label(mains, text="Width:", bg="#344C64", fg="#ffffff", font=('poppins', 11, 'bold'))
width_label.place(x=1200, y=450)
width_entry = Entry(mains)
width_entry.place(x=1270, y=450)

height_label = Label(mains, text="Height:", bg="#344C64", fg="#ffffff", font=('poppins', 11, 'bold'))
height_label.place(x=1200, y=480)
height_entry = Entry(mains)
height_entry.place(x=1270, y=480)

btnScale = Button(mains, text='Resize', width=25, command=image_editor.scaling_image, bg="#344C64")
btnScale.configure(font=('poppins', 11, 'bold'), foreground='#ffffff')
btnScale.place(x=1160, y=510)

btnCrop = Button(mains, text='Crop', width=25, command=image_editor.crop, bg="#344C64")
btnCrop.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnCrop.place(x=805, y=400)

x_translation_label = Label(mains, text="X Translation:", bg="#344C64", fg="#ffffff", font=('poppins', 11, 'bold'))
x_translation_label.place(x=1155, y=340)
x_translation_entry = Entry(mains)
x_translation_entry.place(x=1290, y=340)

y_translation_label = Label(mains, text="Y Translation:", bg="#344C64", fg="#ffffff", font=('poppins', 11, 'bold'))
y_translation_label.place(x=1155, y=370)
y_translation_entry = Entry(mains)
y_translation_entry.place(x=1290, y=370)

btnTranslation = Button(mains, text='Translate', width=25, command=image_editor.apply_translation, bg="#344C64")
btnTranslation.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnTranslation.place(x=1160, y=400)

btnSave = Button(mains, text='Save', width=60, command=image_editor.save, bg="#344C64")
btnSave.configure(font=('poppins',11,'bold'),foreground='#ffffff')
btnSave.place(x=890, y=730)

mains.mainloop()