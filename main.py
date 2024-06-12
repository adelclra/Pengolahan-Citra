import subprocess
from tkinter import *
import tkinter
from functions import ImageEditor
from tkinter import ttk

def open_whiteboard():
    subprocess.Popen(["python", "whiteboard.py"])

# Creating the window for image editor
mains = Tk()
space=(" ")*215
screen_width=mains.winfo_screenwidth()
screen_height = mains.winfo_screenheight()
mains.geometry(f"{screen_width}x{screen_height}")
mains.title(f"{space}Image Editor")
mains.configure(bg='#323946')

panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)

image_editor = ImageEditor(panel)
image_editor.display_image()

brightnessSlider = Scale(mains, label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=200,
                        resolution=0.1, command=image_editor.brightness_callback, bg="#1f242d")
brightnessSlider.set(1)
brightnessSlider.configure(font=('poppins',11,'bold'),foreground='white')
brightnessSlider.place(x=1070,y=15)

contrastSlider = Scale(mains, label="Contrast", from_=0, to=2, orient=HORIZONTAL, length=200,
                    command=image_editor.contrast_callback, resolution=0.1, bg="#1f242d")
contrastSlider.set(1)
contrastSlider.configure(font=('poppins',11,'bold'),foreground='white')
contrastSlider.place(x=1070,y=90)

sharpnessSlider = Scale(mains, label="Sharpness", from_=0, to=2, orient=HORIZONTAL, length=200,
                        command=image_editor.sharpen_callback, resolution=0.1, bg="#1f242d")
sharpnessSlider.set(1)
sharpnessSlider.configure(font=('poppins',11,'bold'),foreground='white')
sharpnessSlider.place(x=1070,y=165)

colorSlider = Scale(mains, label="Colors", from_=0, to=2, orient=HORIZONTAL, length=200,
                    command=image_editor.color_callback, resolution=0.1, bg="#1f242d")
colorSlider.set(1)
colorSlider.configure(font=('poppins',11,'bold'),foreground='white')
colorSlider.place(x=1070,y=240)

whiteboard_button = tkinter.Button(mains, text="Open Whiteboard", command=open_whiteboard, bg="#1f242d")
whiteboard_button.configure(font=('poppins',11,'bold'),foreground='white')
whiteboard_button.place(x=1070, y=315)

btnRotateLeft = Button(mains, text='Rotate Left', width=25, command=image_editor.rotate_left, bg="#1f242d")
btnRotateLeft.configure(font=('poppins',11,'bold'),foreground='white')
btnRotateLeft.place(x=805,y=110)

btnRotateRight = Button(mains, text='Rotate Right', width=25, command=image_editor.rotate_right, bg="#1f242d")
btnRotateRight.configure(font=('poppins',11,'bold'),foreground='white')
btnRotateRight.place(x=805,y=165)

btnRotate90deg = Button(mains, text='Rotate 90°', width=25, command=image_editor.rotate_90deg, bg="#1f242d")
btnRotate90deg.configure(font=('poppins',11,'bold'),foreground='white')
btnRotate90deg.place(x=805,y=220)

btnRotate180deg = Button(mains, text='Rotate 180°', width=25, command=image_editor.rotate_180deg, bg="#1f242d")
btnRotate180deg.configure(font=('poppins',11,'bold'),foreground='white')
btnRotate180deg.place(x=805,y=275)

reset_button = Button(mains, text="Reset", command=image_editor.reset, bg="black", activebackground="ORANGE")
reset_button.configure(font=('poppins',10,'bold'),foreground='white')
reset_button.place(x=380,y=15)

btnChaImg = Button(mains, text='Change Image', width=25, command=image_editor.change_image, bg="#1f242d", activebackground="ORANGE")
btnChaImg.configure(font=('poppins',11,'bold'),foreground='white')
btnChaImg.place(x=805,y=35)

btnFlip = Button(mains, text='Flip', width=25, command=image_editor.flip, bg="#1f242d")
btnFlip.configure(font=('poppins',11,'bold'),foreground='white')
btnFlip.place(x=805,y=340)

btnResize = Button(mains, text='Resize', width=25, command=image_editor.resize, bg="#1f242d")
btnResize.configure(font=('poppins',11,'bold'),foreground='white')
btnResize.place(x=805,y=405)

btnCrop = Button(mains, text='Crop', width=25, command=image_editor.crop, bg="#1f242d")
btnCrop.configure(font=('poppins',11,'bold'),foreground='white')
btnCrop.place(x=805,y=470)

btnSave = Button(mains, text='Save', width=25, command=image_editor.save, bg="black")
btnSave.configure(font=('poppins',11,'bold'),foreground='white')
btnSave.place(x=805,y=730)

btnClose = Button(mains, text='Close', command=lambda: image_editor.close(mains), bg="black", activebackground="ORANGE")
btnClose.configure(font=('poppins',10,'bold'),foreground='white')
btnClose.place(x=430,y=15)

mains.mainloop()

